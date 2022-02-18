from django.shortcuts import render


def main_view(request):
    return render(request, 'tours/index.html')


def departure_view(request, city):
    return render(request, 'tours/depature.html')


def tour_view(request, tour_id):
    return render(request, 'tours/tour.html')


def custom_handler404(request, exception):
    return render(request, 'tours/404.html')


def custom_handler500(request):
    return render(request, 'tours/500.html')
