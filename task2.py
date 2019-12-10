class Airplane():
    def __init__(self, make, model, year, max_speed):
        self.make=make
        self.model=model
        self.year=year
        self.max_speed=max_speed
        self.odometer=0
        self.on_letel = 0
        self.is_flying = 0

    def odometer_reading(self):
        print(f"Pokozanie odometra: {self.odometer}")

    def leti(self, dist):
        self.dist = dist
        self.is_flying += self.dist
        self.odometer += self.dist
        self.on_letel += 1
        # self.ostonovis(0)

    def ostonovis(self, stop_):
        self.stop = stop_
        self.is_flying = self.stop

    def get_descriptive_name(self):
        if self.is_flying == False and self.on_letel == False:
            print(f'This {self.make} has v angare')
        elif self.is_flying:
            print(f'This {self.make} has v letit')
        elif self.on_letel:
            print(f'This {self.make} has v prizemlilsya')
        else:
            pass




my_new_airplane=Airplane('Boing', 777, 2018, 5000)
my_new_airplane.odometer_reading()
my_new_airplane.get_descriptive_name()
my_new_airplane.leti(50000)
my_new_airplane.get_descriptive_name()
my_new_airplane.ostonovis(0)
my_new_airplane.get_descriptive_name()
my_new_airplane.odometer_reading()






