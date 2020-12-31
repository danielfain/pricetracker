from celery import shared_task


@shared_task
def update_prices():
    prices = {}

    # do scraping work here

    return prices