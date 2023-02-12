# distance = 1000 km
# max amount of days = 3
# cost per charge = 5
import math
def find_distance(vehicle_names, vehicle_ranges, vehcile_rental_prices):
    vehicles = {}
    distance = 1000
    amount_of_days = 3
    for i, vehicle in enumerate(vehicle_names):
        vehicles[vehicle] = [vehcile_rental_prices[i] * amount_of_days, math.ceil(distance/vehicle_ranges[i]) * 5]

    least_cost_vehicle = None
    least_cost_amount = math.inf
    for vehicle in vehicles:
        if sum(vehicles[vehicle]) < least_cost_amount:
            least_cost_amount = sum(vehicles[vehicle])
            least_cost_vehicle = vehicle

    return f"The least expensive vehicle is the {least_cost_vehicle} which will cost ${least_cost_amount:.2f} to take on the trip."



if __name__ == "__main__":
    vehicle_names = ["Toyota Prius", "Leaf", "ID4"]
    vehicle_ranges = [100, 200, 75]
    vehicle_rental_prices = [50.00, 75.00, 100.00]
    print(find_distance(vehicle_names, vehicle_ranges, vehicle_rental_prices))