class car:

    def __init__(self, body, engine, tyre):
        self.body = body;
        self.engine  = engine;
        self.tyre = tyre;

    def mileage(self):
        print("Mileage of the car")

class tata(car):
    pass


t = tata("Steel", "dual", 4)
print(t.mileage())
