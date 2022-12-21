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
        top_balloon = None

        for balloon in self.balloons_amount:
            if self.balloons_amount[balloon] > top_amount:
                top_amount = self.balloons_amount[balloon]
                top_balloon = balloon
            elif self.balloons_amount[balloon] == top_amount:
                top_balloon = None

        return top_balloon, top_amount

    def pop_most(self, amount):
        for _ in range(amount):
            top_balloon, top_amount = self.find_top_balloons()
            one_left = all(x == 1 for x in self.balloons_amount.values())
            if one_left:
                self.popped_ballons.append(self.balloons.pop(-1))
                continue

            if top_balloon != None:
                self.balloons_amount[top_balloon] -= 1
                for i in range(len(self.balloons) - 1, -1, -1):
                    if self.balloons[i] == top_balloon:
                        self.popped_ballons.append(self.balloons.pop(i))
                        break
            else:
                for i in range(len(self.balloons) - 1, -1, -1):
                    if self.balloons_amount[self.balloons[i]] == top_amount:
                        self.balloons_amount[self.balloons[i]] -= 1
                        self.popped_ballons.append(self.balloons.pop(i))
                        break

        return self.popped_ballons


def freq_stack(pops, balloons):
    balloons = Balloons(balloons)
    balloons.track_balloons()
    balloons.find_top_balloons()

    return balloons.pop_most(pops)


if __name__ == "__main__":
    pops = 2
    balloons = [5, 7, 5, 7, 4, 5]

    print(freq_stack(pops, balloons))
