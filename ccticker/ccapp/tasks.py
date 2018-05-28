from celery import shared_task
from cryptocompy import price
from django.core.cache import cache


@shared_task
def example_task():
    import logging
    logging.info("This is a test message!")


@shared_task
def update_cc_prices():
    cryptocoins = ['ETH', 'BTC']
    currencies = ['EUR', 'USD']
    response = price.get_current_price(cryptocoins, currencies)
    for cryptocoin in cryptocoins:
        for currency in currencies:
            ticker_code = cryptocoin + currency
            cache.set(ticker_code, response[cryptocoin][currency])
