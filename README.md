# 🚀 Microservices Deployment on AWS EKS

![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)

A production-ready 3-tier microservices application deployed on AWS EKS with Kubernetes orchestration, featuring persistent storage, health checks, and service mesh communication.


## 🎯 Overview

This project demonstrates a complete microservices architecture deployed on AWS EKS (Elastic Kubernetes Service). The application consists of a frontend UI, a RESTful Flask API backend, and a MySQL database with persistent storage. All components are containerized, orchestrated by Kubernetes, and feature production-grade health checks and service discovery.

## 🏗️ Architecture

 <img width="533" height="1573" alt="Untitled Diagram drawio (6)" src="https://github.com/user-attachments/assets/02e9ea93-280f-4740-9d93-118fe138881c" />


 

## Component Details

| Component | Type | Port/Access | Description |
|-----------|------|-------------|-------------|
| **Frontend** | Nginx | NodePort: 30080 | Web server serving static content |
| **Backend** | Flask | NodePort: 30500 | Python API handling business logic |
| **Database** | MySQL 8.0 | ClusterIP: 3306 | Persistent data storage |
| **Storage** | EBS (gp2) | 5Gi | Persistent volume for MySQL data |

## Network Flow

1. **User → Frontend**: External HTTP traffic on port 30080
2. **User → Backend**: Direct API access on port 30500
3. **Frontend → Backend**: Internal API communication
4. **Backend → Database**: SQL queries over internal network (port 3306)
5. **Database → Storage**: Data persisted to EBS volume via PVC

## Service Types

- **NodePort**: Exposes services externally (Frontend & Backend)
- **ClusterIP**: Internal-only access (MySQL)
- **PVC**: Persistent Volume Claim ensures data survives pod restartsce

### Components

| Component | Technology | Service Type | Port | Description |
|-----------|------------|--------------|------|-------------|
| **Frontend** | Nginx | NodePort | 30080 | Static web UI serving the application interface |
| **Backend** | Flask API | NodePort | 30500 | RESTful API handling business logic |
| **Database** | MySQL 8.0 | ClusterIP | 3306 | Persistent data storage with PVC |



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
│   ├── app.py              # Main Flask application
│   └── Dockerfile          # Backend container image
│   └── requirements.txt    # requirements     
├── frontend/               # Web UI
│   ├── index.html          # Frontend page
│   └── Dockerfile          # Frontend container image
├── database/               # Database initialization
│   └── init.sql            # MySQL schema and seed data
└── k8s/                    # Kubernetes manifests
│    ├── 00-namespace.yaml  # Namespace definition
│    ├── 01-secret.yaml     # Database credentials
│    ├── 02-configmap.yaml  # Application configuration
│    ├── 03-mysql.yaml      # MySQL deployment & service
│    ├── 04-backend.yaml    # Backend deployment & service
│    └── 05-frontend.yaml   # Frontend deployment & service
└──screenshots.md/          # deployment screenshots for the project
```



## Documentation formatting and structure assisted by AI tools
