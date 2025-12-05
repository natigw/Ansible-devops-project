# Ansible Project: Web Application with Database Backend

This project demonstrates the automated deployment of a three-tier web application (Flask + MySQL + Nginx) using **Ansible**, **Docker**, and **GitLab CI/CD**.

It is designed to meet the requirements of deploying a web application with a separate database backend, securing secrets with Ansible Vault, and utilizing custom Docker images.

## 📋 Project Overview

The project provisions a full stack environment on a target server:
* **Web Application**: A custom Python Flask app that connects to a database.
* **Database**: A MySQL 8.0 container running in a secure, private network.
* **Reverse Proxy/Load Balancer**: Nginx configured to route traffic to the application.
* **Automation**: Ansible Roles handle the entire configuration management and deployment.

### ✅ Objectives & Features Met

This project fulfills the following assignment requirements:

| Requirement | Implementation Details |
| :--- | :--- |
| **Ansible Roles** | Organized into `roles/db` (Database), `roles/web` (Application), and `roles/docker` (Infrastructure). |
| **Ansible Vault** | Sensitive data (DB passwords, Registry creds) is encrypted in `secret.yml` files. |
| **Docker Integration** | Custom Dockerfile created for the Flask backend; image building and pushing automated via Ansible. |
| **App Deployment** | Full stack deployment including network creation and container orchestration. |
| **CI/CD** | GitLab CI/CD pipeline (`.gitlab-ci.yml`) automates deployment on push. |
| **Load Balancer** | Nginx configured as a reverse proxy entry point. |

## 📂 Project Structure

    devops-ansible-main/
    ├── .gitlab-ci.yml           # CI/CD Pipeline configuration
    ├── ansible/
    │   ├── ansible.cfg          # Local Ansible config
    │   ├── inventory.ini        # Target server inventory
    │   ├── playbook.yml         # Main playbook
    │   └── roles/
    │       ├── db/              # Role: MySQL setup & Private Network
    │       ├── docker/          # Role: Docker Engine installation
    │       └── web/             # Role: App deployment, Secrets, Nginx
    └── app/
        ├── backend/             # Flask Source Code & Dockerfile
        ├── proxy/               # Nginx Configuration & Dockerfile
        └── compose.yaml         # Docker Compose definition

## 🛠 Prerequisites

1.  **Ansible**: Installed on the control node (Version 2.9+ recommended).
2.  **Git**: To clone the repository.
3.  **SSH Access**: Password-less SSH access to the target server.
4.  **Target OS**: Linux (Debian/Ubuntu/CentOS compatible).

## 🚀 Step-by-Step Deployment Guide

### 1. Clone the Repository
Clone the project code to your local machine (Control Node):

    git clone https://gitlab.com/kematian05/devops-ansible.git
    cd devops-ansible

### 2. Configure Inventory
Edit the `ansible/inventory.ini` file. Replace the example IP with your target server's IP address and ensure the user has `sudo` privileges.

    [webserver]
    webserver ansible_host=your-server-ip ansible_user=root ansible_ssh_private_key_file=~/.ssh/id_rsa

### 3. Ansible Vault (Secrets)
This project uses Ansible Vault to secure database passwords and Docker Registry credentials.

> **ℹ️ Note for Grading:**
> The Ansible Vault password for this project is: **`test`**
> *(Please use this password when prompted).*

### 4. Run the Playbook
Execute the deployment using `ansible-playbook`. You must provide the vault password to decrypt the secrets.

    cd ansible
    ansible-playbook playbook.yml --ask-vault-pass

*Enter the password mentioned above when prompted.*

**What the Playbook does:**
1.  **System Prep**: Installs Docker and required Python modules.
2.  **Database**: Sets up the `app_backend` private network and starts the MySQL container.
3.  **Build & Deploy**: Builds the custom Flask image, pushes it (if registry is configured), creates the secrets file on the host, and starts the Nginx/Flask stack.

## 🧪 Testing & Verification

Once the playbook completes successfully, verify the application status.

**1. Access the Web Application**
Open your browser and navigate to your server's IP:
    
    http://<your-server-ip>/

**Expected Result:** You should see a page listing "Blog post #1", "Blog post #2", etc. This confirms:
* Nginx is accepting traffic on port 80.
* Flask is running.
* Flask successfully connected to MySQL and fetched data.

**2. Verify Backend Connections (Optional)**
You can verify the containers on the server:

    ssh root@<your-server-ip>
    docker ps

You should see containers for `proxy`, `backend`, and `db` all in `Up` status.

## 🔄 CI/CD Integration

This repository includes a `.gitlab-ci.yml` file. If hosted on GitLab with a configured Runner:
1.  Add a CI/CD Variable `ANSIBLE_VAULT_PASSWORD_B64` containing the base64 encoded vault password.
2.  Any push to the `main` branch will automatically trigger the `deploy_webserver` job, running the Ansible playbook against the infrastructure.

## 📄 License

This project is submitted for the DevOps Ansible assignment.