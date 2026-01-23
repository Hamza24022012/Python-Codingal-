def hotel_cost(days):
    return 140*days

def plane_ride(city):
    if "New York"==city:
        return 183
    elif "Paris"==city:
        return 183
    elif "Los Angeles"==city:
        return 183
    elif "London"==city:
        return 183
def rental_car(days):
    if days >= 7:
        return 40 * days - 50
    elif days >= 3:
        return 40 * days - 20
    else:
        return 40*days
def trip_cost(city,days,spending_money):
    return rental_car(days)+hotel_cost(days)+plane_ride(city)+spending_money
print(trip_cost("Paris",6,400))
