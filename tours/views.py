from django.shortcuts import render


def main_view(request):
    return render(request, 'index.html')


def departure_view(request, city):
    return render(request, 'depature.html')


def tour_view(request, tour):
    return render(request, 'tour.html')
