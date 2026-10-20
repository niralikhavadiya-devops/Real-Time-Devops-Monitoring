# Real-Time DevOps Monitoring System

An end-to-end DevOps monitoring project demonstrating application
containerization, Kubernetes deployment, metrics collection,
visual monitoring, CI, and alerting.

## 🚀 Project Overview

This project deploys a Flask application using Docker and Kubernetes
and monitors application CPU and memory usage using Prometheus and Grafana.

## 🏗️ Architecture

Flask Application
        ↓
Docker
        ↓
Kubernetes
        ↓
Prometheus
        ↓
Grafana
        ↓
CPU / Memory Monitoring
        ↓
Grafana Alerting

## 🛠️ Technologies Used

- Python
- Flask
- Docker
- Kubernetes
- Kind
- Prometheus
- Grafana
- GitHub Actions
- PowerShell

## 📊 Monitoring

The application exposes Prometheus metrics through:

/metrics

Metrics include:

- CPU usage
- Memory usage

## 🚨 Alerting

Configured a Grafana alert for high CPU usage.

Alert condition:

CPU usage > 80%

The alert lifecycle was tested successfully:

Normal → Firing → Normal

## 🔄 CI

GitHub Actions automatically checks the application on push and pull requests.

## 🐳 Docker

The application is containerized using Docker.

## ☸️ Kubernetes

The application is deployed to a local Kubernetes cluster using Kind.

Health checks are configured using the `/health` endpoint.

## 📈 Grafana

Grafana dashboards visualize real-time CPU and memory metrics collected by Prometheus.

## 👩‍💻 Author

Nirali Khavadiya