from django.shortcuts import render


def main_view(request):
    return render(request, 'tours/index.html')


def departure_view(request, city):
    return render(request, 'tours/depature.html')


def tour_view(request, tour):
    return render(request, 'tours/tour.html')
