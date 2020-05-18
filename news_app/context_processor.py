from django.shortcuts import render
from news_app.models import Category


def categories(request):
    category_list = Category.objects.all()
    return {"categories": category_list}