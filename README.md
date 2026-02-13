# 🚀 Microservices Deployment on AWS EKS

![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)

A production-ready 3-tier microservices application deployed on AWS EKS with Kubernetes orchestration, featuring persistent storage, health checks, and service mesh communication.

## 📋 Table of Contents
- [Overview](#-overview)
- [Architecture](#-architecture)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Prerequisites](#-prerequisites)
- [Quick Start](#-quick-start)
- [Deployment](#-deployment)
- [Verification](#-verification)
- [Access](#-access)
- [Troubleshooting](#-troubleshooting)
- [Cleanup](#-cleanup)

## 🎯 Overview

This project demonstrates a complete microservices architecture deployed on AWS EKS (Elastic Kubernetes Service). The application consists of a frontend UI, a RESTful Flask API backend, and a MySQL database with persistent storage. All components are containerized, orchestrated by Kubernetes, and feature production-grade health checks and service discovery.

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         AWS EKS Cluster                       │
│                                                               │
│  ┌─────────────┐      ┌─────────────┐      ┌─────────────┐  │
│  │  Frontend   │─────▶│   Backend   │─────▶│    MySQL    │  │
│  │   (Nginx)   │      │   (Flask)   │      │   (8.0)     │  │
│  └─────────────┘      └─────────────┘      └─────────────┘  │
│        │                     │                     │         │
│        ▼                     ▼                     ▼         │
│  NodePort:30080       NodePort:30500       ClusterIP:3306   │
│                                                   │           │
│                                            ┌──────▼──────┐   │
│                                            │  PVC (5Gi)  │   │
│                                            │  EBS (gp2)  │   │
│                                            └─────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### Components

| Component | Technology | Service Type | Port | Description |
|-----------|------------|--------------|------|-------------|
| **Frontend** | Nginx | NodePort | 30080 | Static web UI serving the application interface |
| **Backend** | Flask API | NodePort | 30500 | RESTful API handling business logic |
| **Database** | MySQL 8.0 | ClusterIP | 3306 | Persistent data storage with PVC |

## ✨ Features

- 🔄 **Service Mesh Communication**: Seamless inter-service communication using Kubernetes services
- 💾 **Persistent Storage**: MySQL data persisted using PersistentVolumeClaims backed by AWS EBS
- 🏥 **Health Checks**: Readiness and liveness probes for backend and database reliability
- 🔒 **Secret Management**: Kubernetes secrets for sensitive database credentials
- ⚙️ **ConfigMaps**: Environment-specific configurations managed via ConfigMaps
- 🌐 **NodePort Access**: External access to frontend and backend services
- 📦 **Containerized**: All services packaged as Docker images and pushed to Docker Hub
- 🔧 **Infrastructure as Code**: Complete Kubernetes manifests for reproducible deployments

## 🛠️ Tech Stack

**Infrastructure & Orchestration**
- Kubernetes (Container Orchestration)
- AWS EKS (Managed Kubernetes)
- AWS EC2 (Worker Nodes)
- AWS EBS (Persistent Volumes)

**Application**
- Docker (Containerization)
- Flask (Backend API Framework)
- MySQL 8.0 (Relational Database)
- Nginx (Frontend Web Server)

**Tools**
- `kubectl` - Kubernetes CLI
- `eksctl` - EKS management CLI
- `aws` - AWS CLI
- `docker` - Container management

## 📁 Repository Structure

```
.
├── backend/                # Flask API application
│   ├── app.py             # Main Flask application
│   └── Dockerfile         # Backend container image
├── frontend/              # Web UI
│   ├── index.html         # Frontend page
│   └── Dockerfile         # Frontend container image
├── database/              # Database initialization
│   └── init.sql           # MySQL schema and seed data
└── k8s/                   # Kubernetes manifests
    ├── 00-namespace.yaml  # Namespace definition
    ├── 01-secret.yaml     # Database credentials
    ├── 02-configmap.yaml  # Application configuration
    ├── 03-mysql.yaml      # MySQL deployment & service
    ├── 04-backend.yaml    # Backend deployment & service
    └── 05-frontend.yaml   # Frontend deployment & service
```

## 📋 Prerequisites

- **AWS Account** with EKS cluster access
- **Docker Hub Account** for image storage
- **Tools Installed**:
  - [AWS CLI](https://aws.amazon.com/cli/)
  - [eksctl](https://eksctl.io/)
  - [kubectl](https://kubernetes.io/docs/tasks/tools/)
  - [Docker](https://www.docker.com/)

## 🚀 Quick Start

### 1️⃣ Build and Push Docker Images

Replace `YOUR_DOCKERHUB_USERNAME` with your actual Docker Hub username.

```bash
# Build and push backend
cd backend
docker build -t YOUR_DOCKERHUB_USERNAME/microservices-backend:v1 .
docker push YOUR_DOCKERHUB_USERNAME/microservices-backend:v1
cd ..

# Build and push frontend
cd frontend
docker build -t YOUR_DOCKERHUB_USERNAME/microservices-frontend:v1 .
docker push YOUR_DOCKERHUB_USERNAME/microservices-frontend:v1
cd ..
```

### 2️⃣ Update Image Names in Manifests

**PowerShell:**
```powershell
(Get-Content k8s/04-backend.yaml) -replace 'YOUR_DOCKERHUB_USERNAME','<your-username>' | Set-Content k8s/04-backend.yaml
(Get-Content k8s/05-frontend.yaml) -replace 'YOUR_DOCKERHUB_USERNAME','<your-username>' | Set-Content k8s/05-frontend.yaml
```

**Bash/Linux:**
```bash
sed -i 's/YOUR_DOCKERHUB_USERNAME/<your-username>/g' k8s/04-backend.yaml
sed -i 's/YOUR_DOCKERHUB_USERNAME/<your-username>/g' k8s/05-frontend.yaml
```

## 🎯 Deployment

Deploy all components to your EKS cluster in the correct order:

```bash
# Apply Kubernetes manifests
kubectl apply -f k8s/00-namespace.yaml
kubectl apply -f k8s/01-secret.yaml
kubectl apply -f k8s/02-configmap.yaml
kubectl apply -f k8s/03-mysql.yaml
kubectl apply -f k8s/04-backend.yaml
kubectl apply -f k8s/05-frontend.yaml
```

## ✅ Verification

Check the deployment status:

```bash
# Check all resources
kubectl get all -n microservices

# Check pods
kubectl get pods -n microservices

# Check services
kubectl get svc -n microservices

# Check persistent volumes
kubectl get pvc -n microservices
```

### Expected Output

- ✅ All pods in `Running` state
- ✅ `frontend-service` exposed on NodePort `30080`
- ✅ `backend-service` exposed on NodePort `30500`
- ✅ `mysql-pvc` status: `Bound`

## 🌐 Access

### Get Node Public IP

```bash
kubectl get nodes -o wide
```

### Application URLs

- **Frontend**: `http://<NODE_PUBLIC_IP>:30080`
- **Backend API**: `http://<NODE_PUBLIC_IP>:30500/api/users`

### Alternative: Port-Forward (If Security Group Blocks NodePort)

```bash
# Forward frontend
kubectl port-forward -n microservices svc/frontend-service 8080:80

# Forward backend (in another terminal)
kubectl port-forward -n microservices svc/backend-service 30500:5000
```

Then access:
- **Frontend**: `http://localhost:8080`
- **Backend API**: `http://localhost:30500/api/users`

## 🔧 Troubleshooting

### MySQL Pod Stuck in Pending

Check PVC and StorageClass:

```bash
kubectl get pvc -n microservices
kubectl get storageclass
```

**Solution**: Ensure `storageClassName: gp2` is set in `k8s/03-mysql.yaml` and re-apply:

```bash
kubectl delete -f k8s/03-mysql.yaml
kubectl apply -f k8s/03-mysql.yaml
```

### Pods CrashLoopBackOff

Check logs:

```bash
kubectl logs -n microservices <pod-name>
kubectl describe pod -n microservices <pod-name>
```

### Service Not Accessible

1. Verify security group allows NodePort traffic (30000-32767)
2. Check pod health:
   ```bash
   kubectl get pods -n microservices -o wide
   ```
3. Test service internally:
   ```bash
   kubectl run -it --rm debug --image=busybox --restart=Never -n microservices -- sh
   # Inside the pod:
   wget -O- http://backend-service:5000/api/users
   ```

## 🧹 Cleanup

Delete the entire EKS cluster and all resources:

```bash
eksctl delete cluster --name microservices-cluster --region us-east-1
```

Or delete only the application resources:

```bash
kubectl delete namespace microservices
```

## 📸 Screenshots

For documentation purposes, capture:
- ✅ `kubectl get nodes` - Cluster nodes
- ✅ `kubectl get pods -n microservices` - Running pods
- ✅ `kubectl get svc -n microservices` - Services
- ✅ Application UI in browser
- ✅ User creation and listing functionality
- ✅ Docker Hub repository with images
- ✅ AWS EKS cluster console

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

Built with ❤️ as a demonstration of Kubernetes microservices architecture on AWS EKS.

---

**⭐ If you found this project helpful, please consider giving it a star!**
