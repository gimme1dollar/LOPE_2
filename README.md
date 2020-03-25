# Cross

> LOPE Management Website

## Setup
### Development
After setting up your own virtual environment, follow the next instructions
``` bash
# install dependencies
npm install && pip install -r requirements.txt

# setup for database
python manage.py makemigrations
python manage.py migrate

# serve frontend at localhost:8080 and backend at localhost:8000
npm run dev
python manage.py runserver

# serve backend and frontend at localhost:8000
npm run build
python manage.py runserver
```

### Test
```bash
# run unit tests
npm run unit

# run e2e tests
npm run e2e

# run all tests
npm test
```

### Production
After writing you own `docker-compose.yml`, follow the instructions.
```bash
# build docker image
docker-compose build

# run docker container at background
docker-compose up -d

# stop docker container
docker-compose stop
```

