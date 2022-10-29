from turtle import position


def time_arrival(position, speed, target):
    return (target-position)/speed
    

def car_fleet(target, positions, speeds):
    cars = zip(positions, speeds)
    cars = sorted(cars, key=lambda car:car[0])
    num_fleet = 1
    num_cars = len(cars)
    curr_car = len(cars)-1
    for i in range(num_cars-2, -1   , -1):
        t1 = time_arrival(cars[curr_car][0], cars[curr_car][1], target)
        t2 = time_arrival(cars[i][0], cars[i][1], target)
        if t1>=t2:
            continue
        num_fleet = num_fleet + 1 
        curr_car = i
    return num_fleet

print(car_fleet(10, [3], [3]))