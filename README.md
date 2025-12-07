# 🚀 Visitor Counter App — Flask + Redis + Docker Compose

A fully containerised web application that tracks visitor counts using a Flask backend and a Redis datastore.
Built using a learn-by-doing DevOps approach, following real debugging, containerisation, and orchestration workflows.

---

## 📸 Screenshots (Development → Debugging → Dockerisation → Compose)

### **1️⃣ Environment Setup**

Installing Flask <img width="959" src="https://github.com/user-attachments/assets/c2ea2eb7-0d83-4be5-b305-b0958961e907" />

Installing Redis <img width="959" src="https://github.com/user-attachments/assets/7bb514ba-243b-4cad-834f-1f7dc705ef18" />

Pinging Redis <img width="959" src="https://github.com/user-attachments/assets/adf21ed1-8ca2-49af-b582-53501bedae9b" />

---

### **2️⃣ Flask Application Development**

HTML Template <img width="959" src="https://github.com/user-attachments/assets/0531bd69-ac1e-48ff-a178-bf83c2f2f8ac" />

Flask app code <img width="959" src="https://github.com/user-attachments/assets/b2cbb9c2-31d7-4163-97eb-4df41a91972c" />

Running the Flask app locally <img width="959" src="https://github.com/user-attachments/assets/a6883c33-7cf5-41d2-9434-3e14aa219242" />

---

### **3️⃣ Connecting Redis (and Debugging Errors)**

Initial Redis error <img width="959" src="https://github.com/user-attachments/assets/1f1bb092-7efa-4f21-9359-5469214b059e" />

Investigating the issue <img width="959" src="https://github.com/user-attachments/assets/5b733983-6558-41ad-a48c-72f2d0c46015" />

Updating Flask to use Redis container hostname <img width="959" src="https://github.com/user-attachments/assets/f4620278-e9a3-456f-b118-b51fc891fc1e" />

App running successfully with Redis connected <img width="959" src="https://github.com/user-attachments/assets/45656c15-f201-48ec-a6a2-5970fc0b2451" />

Redis value in CLI <img width="959" src="https://github.com/user-attachments/assets/dd66a532-08df-49d3-b08d-ad78ccf24e5e" />

---

### **4️⃣ Dockerisation**

Requirements <img width="959" src="https://github.com/user-attachments/assets/aa5b5975-2bdf-44c7-b9a5-cb2af09b7712" />

Dockerfile <img width="959" src="https://github.com/user-attachments/assets/1ce98ea1-c2a5-4e14-9819-876e9938d9e0" />

Building the Docker image <img width="959" src="https://github.com/user-attachments/assets/9ed17f29-97ce-4ff5-bb61-63e1501f4504" />

Image in Docker Desktop <img width="959" src="https://github.com/user-attachments/assets/771f7d61-dbe2-48a9-b9cb-27a6e998933e" />

Running the container (before Compose networking) <img width="959" src="https://github.com/user-attachments/assets/4a4ddb90-6391-4887-82ed-1ec9a6f8228a" />

Expected internal server error before Redis container <img width="815" src="https://github.com/user-attachments/assets/33dccf9d-25fe-440f-ae82-de115b7081c4" />

---

### **5️⃣ Docker Compose (Final Working System)**

docker-compose.yml <img width="959" src="https://github.com/user-attachments/assets/f5d28433-098d-49a0-895d-58b0099065d4" />

Compose services starting <img width="959" src="https://github.com/user-attachments/assets/253f0b8e-67fd-4429-b4f5-3307e93b3b09" />

Containers communicating properly <img width="959" src="https://github.com/user-attachments/assets/5c68cb69-9640-463b-9e49-b49e6cf11d66" />

Final working visitor counter <img width="959" src="https://github.com/user-attachments/assets/2cae3d81-9611-4c16-96a1-c521dc21e131" />

---

# 🧩 Overview

This project implements a simple microservice-style architecture:

* **Flask** handles the web UI and routes
* **Redis** stores the persistent visit counter
* **Docker** containerises the app
* **Docker Compose** orchestrates multi-container execution

Each page refresh increments a Redis key and displays the updated count.

---

## 🏗️ Architecture Diagram

```
              +-------------------------+
              |     Browser Client      |
              |   http://localhost:5000 |
              +-----------+-------------+
                          |
                          v
                  +-------+--------+
                  |     Flask      |
                  |  (Web App)     |
                  +-------+--------+
                          |
                 Docker Internal Network
                          |
                  +-------+--------+
                  |     Redis      |
                  | (Data Store)   |
                  +----------------+
```

---

## 🗂️ Project Structure

```
.
├── app.py
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── templates/
│   └── index.html
├── images/
└── README.md
```

---

# 🚀 Running the Project

### 1️⃣ Clone the repo

```
git clone https://github.com/NufanNoushad/i-count-docker-app.git
cd i-count-docker-app
```

### 2️⃣ Start via Docker Compose

```
docker compose up --build
```

### 3️⃣ View in browser

Visit → **[http://localhost:5000](http://localhost:5000)**

### 4️⃣ Check Redis manually

```
docker exec -it i-count-redis redis-cli
GET visits
```

---

# 📘 What I Learned

* How to build and run Flask web apps
* Redis fundamentals (`INCR`, `GET`, connection handling)
* Why containers cannot use `localhost` to talk to each other
* How Docker Compose provides service discovery and networking
* Debugging Python, Redis, and Docker errors
* Container image creation & optimisation
* Using SSH keys for GitHub to avoid HTTPS token issues

---

# 🌟 Future Enhancements

* Add Nginx reverse proxy (`nginx → flask → redis`)
* Multi-stage Dockerfile to reduce image size
* Deployment to cloud (AWS EC2)
* Automated CI/CD pipeline with GitHub Actions
* `/api/visits` JSON endpoint
* `/reset` button to clear the counter


