# 🏍️ MotoLog: Vehicle Maintenance Tracker

Backend service for tracking motorcycle maintenance history with automated data retrieval.

## 🚀 Features
* **Smart Vehicle Entry:** Automatically fetches vehicle details (Year, Make, Model) by VIN using **NHTSA API integration**.
* **Maintenance History:** Full CRUD (Create, Read, Update, Delete) for service records.
* **Cost Tracking:** Logging parts and service costs per vehicle.
* **MVC Architecture:** Built with Django 5 using MVT pattern, adhering to Git Flow principles (Feature Branch Workflow).

## 🛠️ Tech Stack
* **Language:** Python 3.12
* **Framework:** Django 5.x
* **Database:** SQLite (Dev) / PostgreSQL (Ready)
* **Integrations:** REST API (US Dept. of Transportation)
* **Tools:** Git Flow, Pip

## ⚙️ How to Run
1.  Clone the repo:
    ```bash
    git clone [https://github.com/Dimarik1986/moto-log-backend.git](https://github.com/Dimarik1986/moto-log-backend.git)
    ```
2.  Install dependencies:
    ```bash
    pip install django requests
    ```
3.  Run migrations and server:
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```