from django.shortcuts import render

# Create your views here.

def display_homepage(request):
    return render(request, "landing_page.html")

def check_out_books(request):
    return render(request, "books.html")