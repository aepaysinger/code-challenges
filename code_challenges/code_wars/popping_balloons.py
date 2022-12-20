class Balloons:
    def __init__(self, balloons):
        self.balloons = balloons
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

    def pop_most(self, amount):
        print(self.balloons)
        for _ in range(amount):
            top_balloon, top_amount, second_balloon, second_amount = self.find_top_balloons()
            one_left = all(x == 1 for x in self.balloons_amount.values())
            if one_left:
                self.popped_ballons.append(self.balloons.pop(-1))
                continue
            
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
                        print(self.balloons[i])
                        the_biggest = self.balloons[i]
                        print(f"biggest = {the_biggest}")
                        self.balloons_amount[the_biggest] -= 1
                        break

                for i in range(len(self.balloons) -1, -1, -1):
                    if self.balloons[i] == the_biggest:
                        self.popped_ballons.append(self.balloons[i])
                        self.balloons.pop(i)    
                        break

 
        return self.popped_ballons
def freq_stack(pops, balloons):
    balloons = Balloons(balloons)
    print(balloons.track_balloons())
    balloons.find_top_balloons()

    
    return balloons.pop_most(pops)
    


if __name__ == "__main__":
       pops = 2
       balloons = [10, 32, 13, 28, 2, 10, 14, 21, 12, 22, 7, 7, 37, 6, 19, 1, 24, 7, 17, 33, 27, 19, 36, 1, 21, 6, 28, 22, 19, 21, 36, 24, 10, 29, 23, 26, 18, 10, 28, 20, 37, 38, 31, 1, 2, 24, 36, 23, 24, 9, 14, 30, 34, 4, 24, 34, 35, 21, 31, 5, 38, 1, 32, 21, 19, 32, 22, 5, 9, 36, 16, 30, 14, 29, 38, 12, 17, 33, 33, 14, 10, 37, 26, 15, 35, 12, 32, 22, 28, 22, 20, 8, 29, 29, 10, 6, 33, 2, 7, 15, 22, 31, 27, 32, 14, 9, 36, 7, 23, 32, 23, 24, 37, 32, 26, 11]
       
       print(freq_stack(pops, balloons))
       
