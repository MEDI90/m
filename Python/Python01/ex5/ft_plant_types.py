class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def Bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"{self.name} provides {self.trunk_diameter} "
              "square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int,
                 age: int, harvest_season: str,  nutritional_value: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self. nutritional_value = nutritional_value


if __name__ == "__main__":
    rose = Flower("Rose", 25, 30, "red")
    sunflower = Flower("Sunflower", 150, 45, "yellow")
    oak = Tree("Oak", 500, 1825, 50, 78)
    pine = Tree("Pine", 800, 3650, 40, 50)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 20, 60, "autumn", "vitamin A")
    print("=== Garden Plant Types ===")
    print()
    print(f"{rose.name} (Flower): {rose.height}cm, "
          f"{rose.age} days, {rose.color} color")
    rose.bloom()
    print()
    print(f"{oak.name} (Tree): {oak.height}cm, "
          f"{oak.age} days, {oak.trunk_diameter}cm diameter")
    oak.produce_shade()
    print()
    print(f"{tomato.name} (Vegetable): {tomato.height}cm, "
          f"{tomato.age} days, {tomato.harvest_season} harvest")
    print(f"{tomato.name} is rich in {tomato.nutritional_value}")
    print()
    print(f"{sunflower.name} (Flower): {sunflower.height}cm, "
          f"{sunflower.age} days, {sunflower.color} color")
    sunflower.bloom()
    print()
    print(f"{pine.name} (Tree): {pine.height}cm, "
          f"{pine.age} days, {pine.trunk_diameter}cm diameter")
    pine.produce_shade()
    print()
    print(f"{carrot.name} (Vegetable): {carrot.height}cm, "
          f"{carrot.age} days, {carrot.harvest_season} harvest")
    print(f"{carrot.name} is rich in {carrot.nutritional_value}")
