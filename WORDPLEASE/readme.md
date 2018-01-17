# Development setup

1. Install Python 3.5+
2. Install requirements using: `pip install -r requirements.txt`
*NOTE: Every time we install a new dependency, we must update the field "requirements.txt")*
3. Enter the `src`folder with `cd src`
3. Create database & apply migrations: `python manage.py migrate`
4. Run development server with `python manage.py runserver`
