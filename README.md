📁 prompt-nexus-frontend/
├── 🏗️ Standalone Components
├── 🎨 Material Design UI
├── 🔄 Reactive Forms & HTTP Client
├── 🛣️ Router with Lazy Loading
├── 🎯 Services & Dependency Injection
└── 📱 Responsive Design

📁 prompt-backend/
├── 🐍 Django REST API
├── 🗄️ PostgreSQL ORM Models
├── 🔥 Redis View Counting
├── 🛡️ CORS & Security Middleware
└── 🚀 Gunicorn WSGI Server

🗄️ PostgreSQL (Primary Data Store)
├── Prompts Table
├── Users Table
└── Relations & Constraints

🔥 Redis (Caching & Analytics)
├── Prompt View Counts
├── Session Storage
└── Real-time Metrics

🐳 Docker Multi-Container Setup
├── 🎯 Frontend (Nginx:80)
├── 🔧 Backend (Gunicorn:8000)
├── 🗄️ Database (PostgreSQL:5432)
└── 🔥 Cache (Redis:6379)

📋 Prerequisites
Docker & Docker Compose

Git for version control

4GB+ RAM for smooth operation

# Build and start all services
docker-compose up --build -d

# View running services
docker-compose ps

# Check logs
docker-compose logs -f

# Check all containers are running
docker ps

# Expected output:
# prompt-nexus-frontend-1
# prompt-nexus-backend-1  
# prompt-nexus-db-1
# prompt-nexus-redis-1


# Service	URL	Port	Purpose
Frontend	http://localhost:4200	4200	Angular Application
Backend API	http://localhost:8000	8000	Django REST API
PostgreSQL	localhost:5432	5432	Database
Redis	localhost:6379	6379	Caching


📊 API Endpoints
Prompts Management

# Method	Endpoint	Description
GET	/api/prompts/	List all prompts
GET	/api/prompts/{id}/	Get prompt details + increment views
POST	/api/prompts/	Create new prompt

Frontend Security
CORS Configuration - Controlled API access

XSS Protection - Angular built-in sanitization

HTTPS Ready - Production SSL configuration

Backend Security
CSRF Protection - Django security middleware

SQL Injection Prevention - Django ORM

Redis Security - Internal network isolation

# Start with Docker 
In the Root D:\prompt-nexus-challenge
Command: docker-compose up --build

# Manual Start
Frontend: D:\prompt-nexus-challenge\prompt-nexus-frontend
Command: ng serve --open

Backend: D:\prompt-nexus-challenge\prompt-backend
Command: python manage.py makemigrations

# Attached Postgres17 db backup in Root

# Connect backend with redis memurai

# Angular Version
├─┬ @angular/animations@21.0.1
│ └── @angular/core@21.0.1 deduped
├─┬ @angular/build@21.0.1
│ └── @angular/core@21.0.1 deduped
├─┬ @angular/cdk@21.0.1
│ └── @angular/core@21.0.1 deduped
├─┬ @angular/common@21.0.1
│ └── @angular/core@21.0.1 deduped
├── @angular/core@21.0.1
├─┬ @angular/forms@21.0.1
│ └── @angular/core@21.0.1 deduped
├─┬ @angular/material@21.0.1
│ └── @angular/core@21.0.1 deduped
├─┬ @angular/platform-browser@21.0.1
│ └── @angular/core@21.0.1 deduped
├─┬ @angular/platform-server@21.0.1
│ └── @angular/core@21.0.1 deduped
├─┬ @angular/router@21.0.1
│ └── @angular/core@21.0.1 deduped
└─┬ @angular/ssr@21.0.1
  └── @angular/core@21.0.1 deduped

# Node = v24.11.1 LTS
# Python Django Version = 5.2.8