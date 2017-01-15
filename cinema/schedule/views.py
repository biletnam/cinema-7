from datetime import datetime
from django.shortcuts import render
from ..schedule.models import Seance, Hall
from ..catalog.models import Movie


def get_time(movie):
    time = str(movie['time'])
    time = time[:19]
    time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
    return time


def show_schedule(request, day=0, month=0):
    all_seances = Seance.objects.order_by('-start_time')
    date = set()  # set of date
    format_seances = {}  # result dict
    print("TEEST " + all_seances.values())
    for movie in all_seances.values():  # forming set of date
        date.add(get_time(movie).strftime('%d-%m'))
    for val in date:  # finding seances for every date
        day_seanses = {}  # all seances for that date
        hall = {}
        for movie in all_seances.values():  # iterate all films
            if get_time(movie).strftime('%d-%m') == val:
                cur_seanses = []
                cur_hall = Hall.objects.get(id=movie['hall_id'])
                cur_movie = Movie.objects.get(id=movie['film_id'])
                hall[cur_hall] = get_time(movie).strftime('%H:%M')
                if cur_movie in day_seanses.keys():  # if film already exist in day_seances
                    for value in day_seanses[cur_movie]:  # copy exist hall+time
                        cur_seanses.append(value)
                    for obj in cur_seanses:  # if current hall for that film exist in day_seances
                        for hallname in obj:
                            if cur_hall == hallname:
                                print(hall[cur_hall])
                                print(1)  # implement adding time here
                            else:
                                print(2)
                cur_seanses.append(hall)
                day_seanses[cur_movie] = cur_seanses
                hall = {}
        format_seances[val] = day_seanses
        print(day_seanses)
    if day == 0 and month == 0:  # schedule for today
        now = datetime.now()
        today = now.strftime("%d-%m")
    else:  # schedule for future or past
        today = day + '-' + month
    context = {'seanses': format_seances, 'today': today}
    return render(request, 'schedule/schedule.html', context)
