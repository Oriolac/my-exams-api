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

## Specifications
### Basic Functions
- [] Generates a unique key for the new uploaded exam if it does not exist.
- [] Store in the global directory exams description, date, time and location.
- [] Modify exam's description
- [] Delete exam
- [] Search exam content using the key or searching them using textual description
- [] Download exam information.
- [x] List all exams information

### Advanced Functions
- [] Unpload grades to an exam
- [] Download student's grades
- [] Manage student's access
- [] Store and retrieve all of your exams' information in a database in your web services server.
- [] Use a Data source in order to manage data information.

### Integration Functions
- [] Create and exam on the WS after uploading the csv file to your RMI server.
- [] Students should validate its ID bfore starting an exam. It receives, in exchange, server's connection details.
- [] Store grades on the WS.