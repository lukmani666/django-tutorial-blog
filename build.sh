pip install -r requirements.txt
python manage.py showmigrations
python manage.py migrate
python manage.py showmigrations
python manage.py collectstatic --noinput

