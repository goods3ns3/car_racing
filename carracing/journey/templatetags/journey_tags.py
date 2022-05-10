from django import template

register = template.Library()


@register.simple_tag()
def get_cars_and_distance(journey_list):
    car_distance = {}
    for j in journey_list:
        if j.car in car_distance:
            car_distance[j.car] += j.distance
        else:
            car_distance[j.car] = j.distance
    return car_distance
