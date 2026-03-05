class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self, amount: int = 1) -> None:
        self.height += amount
        print(f"{self.name} grew {amount}cm")

    def __str__(self) -> str:
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> str:
        return "(blooming)"

    def __str__(self) -> str:
        return (f"- {self.name}: {self.height}cm, "
                f"{self.color} flowers {self.bloom()}")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int,
                 age: int, color: str, prize_points: int):
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

    def __str__(self) -> str:
        return (f"- {self.name}: {self.height}cm, {self.color} "
                f"flowers {self.bloom()}, Prize points: {self.prize_points}")


class Garden:
    def __init__(self, name: str):
        self.name = name
        self.plants = []
        self.initial_heights = 0


class GardenManager:
    _gardens = []

    def create_garden_network(cls, gardens: list) -> None:
        cls._gardens += gardens
        print(f"Total gardens managed: {len(cls._gardens)}")
    create_garden_network = classmethod(create_garden_network)

    def add_plant(garden: Garden, plant: Plant) -> None:
        garden.plants += [plant]
        garden.initial_heights += plant.height
        print(f"Added {plant.name} to {garden.name}'s garden")
    add_plant = staticmethod(add_plant)

    def grow_all(garden: Garden) -> None:
        print(f"\n{garden.name} is helping all plants grow...")
        for plant in garden.plants:
            plant.grow()
    grow_all = staticmethod(grow_all)

    def validate_height(height: int) -> bool:
        return height > 0
    validate_height = staticmethod(validate_height)

    class GardenStats:
        def generate_report(garden: Garden) -> None:
            regular = 0
            flowering = 0
            prize = 0
            total_points = 0
            current_height = 0
            start_height = garden.initial_heights
            for plant in garden.plants:
                current_height += plant.height

                name = plant.__class__.__name__
                if name == "Plant":
                    regular += 1
                elif name == "FloweringPlant":
                    flowering += 1
                elif name == "PrizeFlower":
                    prize += 1
                    total_points += plant.prize_points

            total_growth = current_height - start_height

            print(
                f"Plants added: {len(garden.plants)}, "
                f"Total growth: {total_growth}cm")
            print(
                f"Plant types: {regular} regular, {flowering} "
                f"flowering, {prize} prize flowers")
        generate_report = staticmethod(generate_report)

        def calculate_score(garden: Garden) -> int:
            score = 0
            for plant in garden.plants:
                score += plant.height
                name = plant.__class__.__name__
                if name == "Plant" or name == "FloweringPlant":
                    score += 10
                elif name == "PrizeFlower":
                    score += 10 + plant.prize_points
            return score
        calculate_score = staticmethod(calculate_score)


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    alice_garden = Garden("Alice")
    bob_garden = Garden("Bob")

    oak = Plant("Oak Tree", 100, 20)
    rose = FloweringPlant("Rose", 25, 5, "red")
    sunflower = PrizeFlower("Sunflower", 50, 5, "yellow", 10)

    GardenManager.add_plant(alice_garden, oak)
    GardenManager.add_plant(alice_garden, rose)
    GardenManager.add_plant(alice_garden, sunflower)

    GardenManager.grow_all(alice_garden)

    print(f"\n=== {alice_garden.name}'s Garden Report ===")
    print("Plants in garden:")
    for plant in alice_garden.plants:
        print(plant)
    print("")

    narcissus = PrizeFlower("Narcissus", 60, 20, "White", 22)
    bob_garden.plants += [narcissus]

    GardenManager.GardenStats.generate_report(alice_garden)
    print(f"\nHeight validation test: {GardenManager.validate_height(100)}")

    alice_score = GardenManager.GardenStats.calculate_score(alice_garden)
    bob_score = GardenManager.GardenStats.calculate_score(bob_garden)
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")

    GardenManager.create_garden_network([alice_garden, bob_garden])
