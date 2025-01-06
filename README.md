# Multi-Service Blog Platform

This project is a simple blog platform built using Docker & AWS. It consists of three microservices: User Service, Blog Service, and Comment Service, each with its own database schema in PostgreSQL.

## Project Overview

The platform allows users to register, login, and manage profiles. It also enables the creation, retrieval, updating, and deletion of blog posts, along with the ability to add and list comments for these posts.

## Services

1.  **User Service:**
    *   Handles user authentication and profile management using JWT for authentication and bcrypt for password hashing.
    *   **Endpoints:**
        *   `POST /register`: Register a new user.
        *   `POST /login`: Authenticate a user and get a JWT token.
        *   `GET /users/<id>`: Retrieve user details.
        *   `PUT /users/<id>`: Edit an existing user.
        *   `DELETE /users/<id>`: Delete a specific user.
2.  **Blog Service:**
    *   Manages blog posts with support for pagination when listing posts.
    *   **Endpoints:**
        *   `POST /blogs`: Create a new blog post.
        *   `GET /blogs`: List all blog posts with pagination.
        *   `GET /blogs/<id>`: Fetch a specific blog post.
        *   `PUT /blogs/<id>`: Edit an existing blog post.
        *   `DELETE /blogs/<id>`: Delete a specific blog post.
3.  **Comment Service:**
    *   Handles comments for blog posts in a flat structure.
    *   **Endpoints:**
        *   `POST /comments`: Add a comment to a blog post.
        *   `GET /comments?post_id=<id>`: List comments for a specific blog post.

4.  **Database Service:**
    *   Uses PostgreSQL to store data for all services. Each service uses its own schema to maintain separation of concerns (`users`, `blogs`, and `comments`).

## Technologies

*   **Backend:** Python 3.8+ with Flask framework.
*   **Database:** PostgreSQL
*   **Containerization:** Docker
*   **Orchestration:** Docker Compose
*   **Cloud Deployment:** AWS (EC2 for containers, RDS PostgreSQL)
*   **Authentication:** JWT
   
## Getting Started

### Prerequisites

*   Python 3.8+
*   Docker and Docker Compose
*   AWS account (for cloud deployment)

### Local Development Setup

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd blog-platform
    ```

2.  **Create and configure `.env` file:**
    *   Copy `.env.example` to `.env`.
    *   Edit the `.env` file and provide your PostgreSQL credentials, and JWT secret:

        ```
        POSTGRES_USER=blog_user
        POSTGRES_PASSWORD=blog_password
        POSTGRES_DB=blog_db
        POSTGRES_HOST=db
        POSTGRES_PORT=5432
        JWT_SECRET=your_secret_key
        ```

3.  **Build and run the project with Docker Compose:**

    ```bash
    docker-compose up --build
    ```

    This command will build the Docker images and start all services, including the PostgreSQL database, on your local machine.

4.  **Access the services:**
    *   User service: `http://localhost:5000`
    *   Blog service: `http://localhost:5001`
    *   Comment service: `http://localhost:5002`
