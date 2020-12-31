from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views import View
from .models import Item
from .forms import AddItemForm
from .tasks import crawl


class TrackerView(View):
    def get(self, request):
        items = Item.objects.order_by("-id")
        form = AddItemForm()

        context = {
            "items": items,
            "form": form,
        }

        return render(request, "tracker.html", context)

    def post(self, request):
        form = AddItemForm(request.POST)

        if form.is_valid():
            url = form.cleaned_data.get("url")
            requested_price = form.cleaned_data.get("requested_price")

            data = crawl(url)

            title = data["title"]
            current_price = data["current_price"]

            Item.objects.create(
                url=url,
                title=title,
                requested_price=requested_price,
                current_price=current_price,
            )

        items = Item.objects.order_by("-id")

        context = {
            "items": items,
            "form": form,
        }

        return render(request, "tracker.html", context)
