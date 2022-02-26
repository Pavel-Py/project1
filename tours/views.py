from django.shortcuts import render
from tours import data
from random import randrange


def main_view(request):
    rand_tours = list()    # Создаем список в который будем добавлять поочереди ID тура, затем словарь с атрибутами
    while len(rand_tours) < 12:    # Цикл на 6 повторов по 2 значения за повтор
        tour_id = randrange(1, len(data.tours) + 1)      # Выбор случайного id
        if tour_id not in rand_tours:   # Если id нету в нашем списке
            rand_tours.append(tour_id)  # Добавляем id (нулевой или четный индекс)
            rand_tours.append(data.tours[tour_id])  # Добавляем словарь с атрибутами (нечетный индекс)
    return render(request, 'tours/index.html', context={'rand_tours': rand_tours})


def departure_view(request, city):
    dep_city = data.departures.get(city)
    tours, prices, nights = list(), list(), list()
    for tour_id, tour_args in data.tours.items():
        if tour_args['departure'] == city:
            tours.append(tour_id)
            tours.append(tour_args)
            prices.append(tour_args['price'])
            nights.append(tour_args['nights'])
    return render(request, 'tours/departure.html', {'tours': tours, 'dep_city': dep_city, 'prices': prices,
                                                    'nights': nights})


def tour_view(request, tour_id):
    tour = data.tours.get(tour_id)  # Выбираем тур
    departure = data.departures.get(tour.get('departure'))  # Вытаскиваем из словаря город отправления
    return render(request, 'tours/tour.html', context={'tour': tour, 'departure': departure})


def custom_handler404(request, exception):
    return render(request, 'tours/404.html')


def custom_handler500(request):
    return render(request, 'tours/500.html')
