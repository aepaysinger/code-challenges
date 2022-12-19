class Balloons:
    def __init__(self, amount, balloons):
        self.balloons = balloons
        self.amount = amount
        self.balloons_amount = {}
        self.popped_ballons = []

    
    def track_balloons(self):
        for balloon in self.balloons:
            self.balloons_amount[balloon] = self.balloons_amount.get(balloon, 0) + 1
        return self.balloons_amount

    def find_top_balloons(self):
        top_amount = 0
        second_amount = 0
        top_balloon = None
        second_balloon = None
        
        for balloon in self.balloons_amount:
            if self.balloons_amount[balloon] > top_amount:
                second_amount = top_amount
                second_balloon = top_balloon
                top_amount = self.balloons_amount[balloon]
                top_balloon = balloon
            elif self.balloons_amount[balloon] > second_amount and self.balloons_amount[balloon] <= top_amount:
                second_amount = self.balloons_amount[balloon]
                second_balloon = balloon
        return top_balloon, top_amount, second_balloon, second_amount

    def pop_most(self):
        top_balloon, top_amount, second_balloon, second_amount = self.find_top_balloons()
        one_left = all(x == 1 for x in self.balloons_amount.values())
        if one_left:
            while len(self.popped_ballons) < self.amount:
                self.popped_ballons.append(self.balloons[-1])
                self.balloons.pop(-1)
                return self.popped_ballons
        
        if top_amount > second_amount:
                self.balloons_amount[top_balloon] -= 1
                for i in range(len(self.balloons) -1, -1, -1):
                    if self.balloons[i] == top_balloon:
                        self.popped_ballons.append(self.balloons[i])
                        self.balloons.pop(i)
                        break
        elif top_amount == second_amount:
            the_biggest = None
            for i in range(len(self.balloons) -1, -1, -1):
                if self.balloons[i] == top_balloon or self.balloons[i] == second_balloon:
                    the_biggest = self.balloons[i]
                    self.balloons_amount[the_biggest] -= 1
                    break

            for i in range(len(self.balloons) -1, -1, -1):
                if self.balloons[i] == the_biggest:
                    self.popped_ballons.append(self.balloons[i])
                    self.balloons.pop(i)    
                    break

 
        return self.balloons, self.popped_ballons

    def pop_most_amount(self):
        for i in range(self.amount):
            self.pop_most()
        return self.popped_ballons

def freq_stack(pops, balloons):
    balloons = Balloons(pops, balloons)
    balloons.track_balloons()
    balloons.find_top_balloons()
    
    return balloons.pop_most_amount()




if __name__ == "__main__":
       pops = 10
       balloons = [1, 2, 3, 4, 5, 5, 7, 8, 9, 10]
       print(freq_stack(pops, balloons))

# 7, [12, 9, 8, 8, 12, 12, 6, 1, 8]
# [8, 12, 12, 8, 1, 6, 8]


# balloons = Balloons([5, 7, 5, 7, 4, 5], 4)
# balloons.track_balloons()
# balloons.find_top_balloons()
# print(balloons.pop_most_amount())

# print(balloons.pop_most())
# print(balloons.pop_most())
# print(balloons.pop_most())
# print(balloons.pop_most())
# print(balloons.pop_most())
# print(balloons.popped_ballons)
