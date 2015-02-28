from dice import d6

class Combatant:
	def __init__(self, name, health, speed = 0, brawn = 0, armour = 0):
		self.name = name
		self.speed = speed
		self.brawn = brawn
		self.health = health
		self.armour = armour
		
	def attack_score(self):
		return self.speed + d6() + d6()
