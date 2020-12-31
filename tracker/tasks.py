from celery import shared_task
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from .models import Item


@shared_task
def update_prices():
    items = Item.objects.all()

    for item in items:
        data = crawl(item.url)
        current_price = data["current_price"]

        item_obj = Item.objects.get(id=item.id)

        if current_price < item.requested_price:
            # send email notifying eventually
            pass

        item_obj.current_price = current_price

        item_obj.save()


def crawl(url):
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    html = urlopen(req).read()
    bs = BeautifulSoup(html, "html.parser")

    title = bs.find("h1", id="itemTitle").get_text().replace("Details about", "")
    price = bs.find("span", id="prcIsum").get_text()
    clean_price = float(price.strip().replace("US", "").replace("$", ""))

    return {"title": title, "current_price": clean_price}