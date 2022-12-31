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
        print(guests_per_day)
        
        for i in range(len(self.guests)):
            self.guests = sorted(self.guests)
            print(f"starting the loop self.guests: {self.guests}")
            amount = self.cost * self.guests[0]
            print(f"guest: {self.guests[0]}")
            print(f"starting amount: {amount}")
            amount -= amount_paid
            print(f" amount - amount paid: {amount}")
            amount = math.ceil(amount / len(self.guests))
            # amount = amount // len(self.guests)
            print(f"amount/len(guest) rounded up: {amount}")
            print(f"guest per day [0]: {guests_per_day[self.guests[0]]}")
            guest_amount[self.guests[0]] = guest_amount.get(self.guests[0], amount)
            amount = amount * guests_per_day[self.guests[0]]
            amount_paid += amount
            print(f"amount paid: {amount_paid}")
            # guest_amount[self.guests[0]] = guest_amount.get(self.guests[0], amount)
            for _ in range(guests_per_day[self.guests[0]]):
                self.guests.remove(self.guests[0])
            print(self.guests)
           

            if len(self.guests) == 0:
                break
        return guest_amount
            

def calculate_cost_per_person(cost, guests):
    rent = Rent(cost, guests)
    rent.calculate_guests_per_day

    return rent.calculate_rent_per_person()



if __name__ == "__main__":
    # cost = 50
    # guests = [12, 20, 4, 20, 10, 10, 10, 7, 7, 7]
    cost = 100
    guests = [7, 7, 7, 7, 1, 1, 2, 4, 5, 6]

    print(calculate_cost_per_person(cost, guests))

