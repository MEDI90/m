#!/usr/bin/python3
class plant:
	def __init__(self, name: str, height: int, age: int):
		self.name = name
		self.height = height
		self.age = age
	
	def desplay_info(self) -> None:
		print(f"{self.name}: {self.height}cm, {self.age} days old")

	def grow(self, ammount: int = 1) -> None:
		self.height = self.height + ammount
	
	def aging(self, ammount: int = 1) -> None:
		self.age = self.age + ammount

if __name__ == "__main__":
    rose = plant("Rose", 25, 30)
    start_height = rose.height
    print("=== Day 1 ===")
    rose.desplay_info()
    for _ in range(6):
        rose.grow(1)
        rose.aging(1)
    print("=== Day 7 ===")
    rose.desplay_info()
    growth_this_week = rose.height - start_height
    print(f"Growth this week: +{growth_this_week}cm")