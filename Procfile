# web: gunicorn douhack_basic.wsgi
# web: python manage.py run_gunicorn -b 0.0.0.0:\$PORT -w 9 -k gevent --max-requests 250 --preload
web: make collectstatic; gunicorn_django --workers=4 --bind=0.0.0.0:$PORT douhack_basic/settings/production.py 

