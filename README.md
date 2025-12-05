# Automated Deployment of a Web Application with Database Backend

## Project Summary

This project shows the automated deployment of a simple web application connected to a separate database backend using **Ansible** and **Docker**. The goal is to showcase a structured approach using Ansible roles, secure handling of sensitive data via Ansible Vault, and containerized application deployment. It also includes building a custom Docker image for the application and orchestrating deployment through Ansible.

---

## Requirements

1. **Ansible Roles**

   * **Database Role**: Configure and install the database server.
   * **Web Application Role**: Set up the web application and ensure it connects to the database.

2. **Secure Sensitive Data**

   * Use **Ansible Vault** to encrypt database credentials and other secrets.

3. **Docker Integration**

   * Build a custom Docker image for the web application.
   * Optionally, push the image to a container registry if external access is required.

4. **Automated Deployment**

   * Deploy the web application container.
   * Connect the web app to the database container ensuring proper communication.

5. **Documentation**

   * Provide clear instructions and explanations for deployment and testing.

---

## 📂 Simplified structure of project

```
.
├──ansible/
│    ├── inventory.ini
│    ├── playbook.yml
│    └── roles/
│        ├── db/               # Database setup
│        ├── docker/           # Docker installation & configuration
│        └── web/              # Web app deployment
│
├──app/
│    ├── backend/             # Flask app source code & Dockerfile
│    │   ├── dependencies.txt
│    │   └── main.py
│    ├── compose.yaml          # Docker Compose definition
│    └── proxy/                # Nginx reverse proxy
│        └── Dockerfile
│
└──README.md
```

---

## Setup & Deployment Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/natigw/Ansible-devops-project
   cd devops-ansible
   ```

2. **Configure Inventory**

   * Edit `ansible/inventory.ini` with target server IP and user credentials.

   ```ini
   [webserver]
   server ansible_host*<your-server-ip> ansible_user=root ansible_ssh_private_key_file=~/.ssh/id_rsa
   ```

3. **Ansible Vault**

   * Ensure sensitive variables are encrypted using Ansible Vault.
   * For grading purposes, provide the vault password securely. \
    
    ℹ️ Note: for grading, the Ansible Vault password for this project is: test (Please use this password when prompted).

4. **Run the Playbooks**

   ```bash
   ansible-playbook playbook.yml --ask-vault-pass
   ```

   * This will:

     * Install Docker and required dependencies.
     * Set up the database container and network.
     * Build the custom Docker image for the web app.
     * Deploy the application container and Nginx (if configured).

5. **Verify Deployment**

   * Open the web application in a browser:

   ```
   http://<your-server-ip>/
   ```

   * Confirm that the app can communicate with the database.
   * Optionally, SSH into the server and run:

   ```bash
   docker ps
   ```

   * Ensure both application and database containers are running.

---

## Screenshot from web-app
<img width="2880" height="1620" alt="image" src="https://github.com/user-attachments/assets/24195491-d3d5-4dbc-be89-bcab5354c084" />

