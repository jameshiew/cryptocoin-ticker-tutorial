from celery import shared_task


@shared_task
def example_task():
    import logging
    logging.info("This is a test message!")
