from random import randrange

from django.shortcuts import render

from tours import data


def main_view(request):
    rand_tours = list()    # Создаем список в который будем добавлять поочереди ID тура, затем словарь с атрибутами
    while len(rand_tours) < 12:    # Цикл на 6 повторов по 2 значения за повтор
        tour_id = randrange(1, len(data.tours) + 1)      # Выбор случайного id
        if tour_id not in rand_tours:   # Если id нету в списке случайных туров
            rand_tours.append(tour_id)  # Добавляем id (нулевой или четный индекс)
            rand_tours.append(data.tours[tour_id])  # Добавляем словарь с атрибутами (нечетный индекс)
    return render(request, 'tours/index.html', context={'rand_tours': rand_tours})


def departure_view(request, city):
    dep_city = data.departures.get(city)    # Добавляем строку с названием города
    tours, prices, nights = list(), list(), list()  # Список для ID и туров, список цен, список кол-ва ночей
    for tour_id, tour_args in data.tours.items():   # Пробегаем по изначальному словарю
        if tour_args['departure'] == city:  # Если тур соответствует городу отправдения
            tours.append(tour_id)   # В tour список добавляем его ID
            tours.append(tour_args) # И его атрибуты
            prices.append(tour_args['price'])   # Добавляем цену в price спикок
            nights.append(tour_args['nights'])  # Добавляем кол-во ночей в список nights
    return render(request, 'tours/departure.html', {'tours': tours, 'dep_city': dep_city, 'prices': prices,
                                                    'nights': nights})


def tour_view(request, tour_id):
    tour = data.tours.get(tour_id)  # Переменная со словарем атрибутов тура
    departure = data.departures.get(tour.get('departure'))  # Переменная с городом отправления
    return render(request, 'tours/tour.html', context={'tour': tour, 'departure': departure})


def custom_handler404(request, exception):
    return render(request, 'tours/404.html')


def custom_handler500(request):
    return render(request, 'tours/500.html')
