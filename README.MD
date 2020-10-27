## Setting up
* Set up and activate virtual environment:
```
    python -m venv .env && source .env/bin/activate
```

* Install dependencies:
```
    pip install -r requirements.txt
```

* If starting from zero (not this case), do this:
```
    python manage.py makemigrations
    python manage.py makemigrations backend
    python manage.py makemigrations frontend
    python manage.py migrate
    python manage.py loaddata backend/fixtures/leadstatus_fixture.json 
```

* Since I left the DB in the repo, the process above is not necessary

* Run server
```
    python manage.py runserver
```

* Access it at `http://127.0.0.1:8000`

## Functionality
From the root page you can easily access the login and registration pages. Once logged in, you have access to a table with your leads and a button to create new ones. From the table you can click on the buttons to change the lead status

I already made a user as an example, username 'teste' and password 'teste'.

You can also access the api endpoints at `/api/leads` and `/api/users` (for registration)