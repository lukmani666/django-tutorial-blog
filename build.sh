pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
python -m gunicorn blogconfiguration.wsgi:application
