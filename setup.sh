#!/bin/bash

# Root project directory
mkdir -p custom-data-processing

# Backend structure
mkdir -p backend/app/api/v1/endpoints
mkdir -p backend/app/core
mkdir -p backend/app/db/models
mkdir -p backend/app/services
mkdir -p backend/app/workers
mkdir -p backend/app/utils
mkdir -p backend/tests
mkdir -p backend/alembic/versions

# Frontend structure
mkdir -p frontend/public
mkdir -p frontend/src/components
mkdir -p frontend/src/pages
mkdir -p frontend/src/services

# Root files
touch .gitignore
# touch README.md
touch .env
touch docker-compose.yml

# Backend files
touch backend/Dockerfile
touch backend/requirements.txt
touch backend/alembic/env.py
touch backend/app/api/v1/__init__.py
touch backend/app/api/v1/dependencies.py
touch backend/app/api/v1/endpoints/__init__.py
touch backend/app/core/config.py
touch backend/app/core/security.py
touch backend/app/db/base.py
touch backend/app/db/session.py
touch backend/app/main.py
touch backend/app/__init__.py

# Frontend files
touch frontend/Dockerfile
touch frontend/package.json
touch frontend/webpack.config.js
touch frontend/src/App.js
touch frontend/src/index.js
