def hotel_cost(nights):
    return 140 * nights


def plane_cost(city):
    if city == "Dubai":
        return 200
    elif city == "New Delhi":
        return 250
    elif city == "Washington DC":
        return 300


def car_rent(days):
    if days >= 7:
        return 40 * days - 50
    elif days >= 3:
        return 40 * days - 30
    else:
        return 40 * days


def trip_cost(nights, days, city, spending):
    return hotel_cost(nights) + plane_cost(city) + car_rent(days) + spending


print("Total Cost of the trip is: ", trip_cost(3, 2, "Dubai", 300))
print("Hotel Cost is ", hotel_cost(3))
print("Car rent Cost is ", car_rent(2))
print("Plane Cost is ", plane_cost("Dubai"))
print("Spending Cost is: ", 300)
