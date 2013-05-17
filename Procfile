web: make collectstatic; gunicorn_django --workers=4 --bind=0.0.0.0:$PORT douhack_basic/settings/production.py 
scheduler: python manage.py celery worker -B -E --maxtasksperchild=1000
