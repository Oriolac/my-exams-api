# My Exams API

## How to use
### Running
The first time, you must run the images.
```bash
docker-compose build
```
```bash
docker-compose up
```

### DB Migration
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

### Testing
```bash
docker-compose exec web python manage.py test apps.api.tests
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
- [] Create and exam on the WS after uploading the csv file to your RMI server.
- [] Students should validate its ID bfore starting an exam. It receives, in exchange, server's connection details.
- [] Store grades on the WS.
