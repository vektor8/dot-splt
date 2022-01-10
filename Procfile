websocket: daphne server.asgi:application --port 8000 --bind 0.0.0.0 -v2
web: gunicorn server.wsgi
release: python3 manage.py makemigrations --noinput
release: python3 manage.py collectstatic --noinput
release: python3 manage.py migrate --noinput
