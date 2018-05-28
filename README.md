# cryptocoin-ticker-tutorial

This is the codebase to accompany the cryptocoin ticker tutorial on Medium.com.

# Trying it out

* Run `pipenv install --skip-lock`
* Run `cd ccticker/`, `./manage.py migrate`, `./manage.py createsuperuser`, `./manage.py runserver`
* Go to `http://localhost:8000/admin/django_celery_beat/periodictask/add/` and schedule `ccapp.tasks.update_cc_prices` to run every ten seconds
* Run `cd ccticker/`, `celery -A ccticker worker -l info`
* and `cd ccticker/`, `celery -A ccticker beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler`
* Go to `http://localhost:8000/tickers`