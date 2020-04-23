# cryptocoin-ticker-tutorial [![pipeline status](https://gitlab.com/jameshiew/cryptocoin-ticker-tutorial/badges/master/pipeline.svg)](https://gitlab.com/jameshiew/cryptocoin-ticker-tutorial/commits/master)

This is the codebase to accompany the cryptocoin ticker tutorial [on Medium.com](https://medium.com/@auxyz/creating-a-cryptocoin-price-ticker-with-django-2-0-part-one-2b628deb85d9).

# Trying it out

* Run `pipenv install --skip-lock` to set up an environment with required dependencies
* Run `pipenv shell` to activate the environment in your shell
* Run `cd ccticker/`, `./manage.py migrate`, `./manage.py createsuperuser`, `./manage.py runserver`
* Go to `http://localhost:8000/admin/django_celery_beat/periodictask/add/` and schedule `ccapp.tasks.update_cc_prices` to run every ten seconds
* Run `cd ccticker/`, `celery -A ccticker worker -l info`
* and `cd ccticker/`, `celery -A ccticker beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler`
* Go to `http://localhost:8000/tickers`
