web: gunicorn server.wsgi
web : daphne server.asgi:application --port $PORT --bind 0.0.0.0 -v2 
release: python3 manage.py makemigrations --noinput
release: python3 manage.py collectstatic --noinput
release: python3 manage.py migrate --noinput