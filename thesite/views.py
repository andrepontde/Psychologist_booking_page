from django.shortcuts import render

def homepage(request):
    return render(request, "index.html")

def bookings(request):
    return render(request, "bookings.html")
def about(request):
    return render(request, "about.html")