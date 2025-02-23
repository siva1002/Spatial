## Steps to Run the Application

### 1. Clone the Repository
```sh
git clone  https://github.com/siva1002/spad.git
cd master
```

### 2. Configure Environment Variables
Copy the `.env.example` file to `.env` and update the necessary variables.
```sh
cp .env.example .env
```

### 3. Build and Start the Containers
```sh
docker compose up --build -d
```
This command:
- Builds the Docker image
- Starts the containers in detached mode


### 5. Create a Superuser (Optional)
```sh
docker compose exec django python manage.py createsuperuser
```
Follow the prompts to create an admin user.


### 7. Access the Application
- Open your browser and navigate to: `http://localhost:8000`
- Admin panel: `http://localhost:8000/admin`

## Stopping and Removing Containers
To stop the running containers:
```sh
docker-compose down
```
To stop and remove all containers, networks, and volumes:
```sh
docker-compose down -v
```

### Author: Sivasuruli

