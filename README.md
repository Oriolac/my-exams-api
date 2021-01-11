# My Exams API
Exams management API built with Django and Django Rest Framework.
## How to use
### Running
The first time, you must build the images using.
```bash
docker-compose build
```
In order to run the container, you must:
```bash
docker-compose up
```
You can run the container in detach mode:
```bash
docker-compose up -d
```
### DB Migration
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

### Testing
```bash
docker-compose exec web python manage.py test apps.api.tests.AllInOneTestCas
```

## Specifications
### Basic Functions
- [X] Generates a unique key for the new uploaded exam if it does not exist.
- [X] Store in the global directory exams description, date, time and location.
- [X] Modify exam's description
- [X] Delete exam
- [X] Search exam content using the key or searching them using textual description
- [X] Download exam information.
- [x] List all exams information

### Advanced Functions
- [X] Upload grades to an exam
- [X] Download student's grades
- [X] Manage student's access
- [X] Store and retrieve all of your exams' information in a database in your web services server.
- [X] Use a Data source in order to manage data information.

### Integration Functions
- [X] Create and exam on the WS after uploading the csv file to your RMI server.
- [X] Students should validate its ID bfore starting an exam. It receives, in exchange, server's connection details.
- [X] Store grades on the WS.
