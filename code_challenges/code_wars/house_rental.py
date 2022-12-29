import math


class Rent:
    def __init__(self, cost, guests):
        self.cost = cost
        self.guests = guests

    def calculate_guests_per_day(self):
        guests_per_day = {}
        for guest in self.guests:
            guests_per_day[guest] = guests_per_day.get(guest, 0) + 1

        return guests_per_day

    def calculate_rent_per_person(self):
        guests_per_day = self.calculate_guests_per_day()
        guest_amount = {}
        amount_paid = 0
    
        
        for guest in sorted(self.guests):
            guest_to_remove = guest
            amount = self.cost * guest
            print(f"guest: {guest}")
            print(f"starting amount: {amount}")
            amount -= amount_paid
            print(f" amount - amount paid: {amount}")
            amount = math.ceil(amount / len(self.guests))
            print(f"amount/len(guest) rounded up: {amount}")
            amount_paid += amount
            print(f"amount paid: {amount_paid}")
            guest_amount[guest] = guest_amount.get(guest, amount)
            self.guests = [guest for guest in self.guests if guest != guest]
                # list_of_num = [num for num in list_of_num if num != 54 and num !=55 ]
           

            if len(self.guests) == 0:
                break
            print(guest_amount)
            

        # return 




rent = Rent(100, [7, 7, 7, 7, 1, 1, 2, 4, 5, 6])
rent.calculate_guests_per_day()
print(rent.calculate_rent_per_person())



# def calculate_cost_per_person(cost):
#     pass



# if __name__ == "__main__":
#     cost = 100
#     guests = [7, 7, 7, 7, 1, 1, 2, 4, 5, 6]
#     print(calculate_cost_per_person(cost, [7, 7, 7, 7, 1, 1, 2, 4, 5, 6]))
