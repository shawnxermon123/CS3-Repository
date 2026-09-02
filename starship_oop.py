
def calculate_fuel(cargo_weight):
    final_fuel = 0
    base_ship_weigth = 50000
    total_weight = cargo_weight + base_ship_weigth
    final_fuel = total_weight * 3

    return final_fuel

class starship:
    def __init__(self, cargo_weight, base_weight, final_fuel):
            self.cargo_weight = cargo_weight
            self.base_weight = base_weight
            self.final_fuel = final_fuel
            
    def calculate_fuel(self):
        print("Final Fuel Needed: ", self.final_fuel)
         
starship = starship(50000, 0, 0)
starship.load_cargo()
starship.load_cargo()
starship.load_cargo()

starship.calculate_fuel()