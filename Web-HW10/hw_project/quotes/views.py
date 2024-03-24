from django.shortcuts import render, redirect
from django.core.paginator import Paginator
# Create your views here.
from .utils import get_mongodb



def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_age = 10
    paginator = Paginator(list(quotes), per_age)
    quotes_on_page = paginator.page(page)
    return render(request, "quotes/index.html", context={"quotes": quotes_on_page})



