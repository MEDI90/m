#!/usr/bin/python3
class plant:
	def __init__(self, name: str, height: int, age: int):
		self.name = name
		self.height = height
		self.age = age	

	def desplay_info(self) -> None:
		print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
	roze = plant("Roze", 25, 30)
	sunflower = plant("Sunflower", 80, 45)
	cactus = plant("Cactun", 15, 120)
	print("=== Welcome to My Garden ===")
	roze.desplay_info()
	sunflower.desplay_info()
	cactus.desplay_info()
