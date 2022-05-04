

class Seed:


    def __init__(self, name, grow_time, purchase_price, sell_price):
        self.name = name
        self.grow_time = grow_time
        self.sell_price = sell_price
        self.purchase_price = purchase_price
        # in minutes
        self.cycle = 1440
        self.hours = self.cycle / 60
        self.days = self.hours / 24
        self.harvest_count = self.cycle / self.grow_time
        self.gross = self.harvest_count * self.sell_price
        self.cost = self.harvest_count * self.purchase_price
        self.profit = self.gross - self.cost


seeds = (
         Seed("sunflower", 1, 0.0005, 0.001),
         Seed("potato", 5, 0.005, 0.007),
         Seed("pumpkin", 30, 0.01, 0.02),
         Seed("carrot", 60, 0.025, 0.04),
         Seed("cabbage", 120, 0.05, 0.075),
         Seed("beetroot", 240, 0.1, 0.14),
         Seed("cauliflower", 480, 0.15, 0.2125),
         Seed("parsnip", 720, 0.25, 0.325),
         Seed("radish", 1440, 0.35, 0.475),
         Seed("wheat", 1440, 0.25, 0.35),
        )

for seed in seeds:
    print("Per " + str(seed.cycle) + " Minutes, " + str(seed.hours)
          + " Hours, " + str(seed.days) + " Days:\n" + seed.name
          + "\n# of Harvests: " + str(seed.harvest_count) 
          + "\n Profit:" + str(seed.profit) + "\nCost:" + str(seed.cost)
          + "\n\n")
