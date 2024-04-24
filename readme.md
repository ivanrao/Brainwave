# Brainwave

## Run backend
Install dependencies:
```
pip install -r requirements.txt
```

Run server:
```
uvicorn main:app
```

## Run database (mongoDb) with Docker
Run this command on a terminal to pull the latest mongoDb image and create and run the container:
```
docker run --name mongodb -p 27017:27017 -d mongodb/mongodb-community-server:latest
```

