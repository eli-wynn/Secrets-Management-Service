# Secrets-Management-Service
Internal services often need to store sensitive values such as API keys and credentials. This project implements a backend service that securely stores secrets with encryption at rest, strict access controls, and audit logging. The project is based on the AWS Secrets Manager and is essentially a very simplified version of it.

## Tech Stack
- Backend: Python + FastAPI
- Database: PostgreSQL
- Auth: JWT (Access tokens)
- Deployment: Docker
- Testing: Pytest


## High-level Architecture
Client → FastAPI → Auth Middleware → Service Layer → DB
                                → Crypto Layer
                                → Audit Logger

## Database Schema
Users
- id
- username
- password_hash
- role (user | admin)
- created_at

Secrets
- id
- encrypted_value
- owner_id
- created_at

