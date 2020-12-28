# My Exams API

## How to use
### Running
```bash
docker-compose up --build
```

### DB Migration
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```
