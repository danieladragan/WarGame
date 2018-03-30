# Author: B122980

class Soldier:
	move = 0		# integer (0-50)
	fight = 0		# integer (0-50)
	shoot = 0		# integer (0-50)
	armour = 0 		# integer (0-50)
	morale = 0 		# integer (0-50)
	health = 0 		# integer (0-50)
	cost = 0 		# integer (0-50)
	note = " " 		# string (listing special characteristics and equipment)
		
	def set_move(self, new_move):
		if new_move > 50 or new_move < 0:
			print "The move ability is a number between 0 and 50"
		else:
			self.move = new_move

	def set_fight(self, new_fight):
		if new_fight > 50 or new_fight < 0:
			print "The fight ability is a number between 0 and 50"
		else:
			self.fight = new_fight

	def set_shoot(self, new_shoot):
		if new_shoot > 50 or new_shoot < 0:
			print "The shoot ability is a number between 0 and 50"
		else:
			self.shoot = new_shoot

	def set_armour(self, new_armour):
		if new_armour > 50 or new_armour < 0:
			print "The armour ability is a number between 0 and 50"
		else:
			self.armour = new_armour

	def set_morale(self, new_morale):
		if new_morale > 50 or new_morale < 0:
			print "The morale ability is a number between 0 and 50"
		else:
			self.morale = new_morale

	def set_health(self, new_health):
		if new_health > 50 or new_health < 0:
			print "The health ability is a number between 0 and 50"
		else:
			self.health = new_health

	def set_cost(self, new_cost):
		if new_cost > 50 or new_cost < 0:
			print "The cost is a number between 0 and 50"
		else:
			self.cost = new_cost

	def set_note(self, new_note):
		self.note = new_note

	def get_move(self):
		return self.move

	def get_fight(self):
		return self.fight

	def get_shoot(self):
		return self.shoot

	def get_armour(self):
		return self.armour

	def get_morale(self):
		return self.morale

	def get_health(self):
		return self.health

	def get_cost (self):
		return self.cost 

	def get_note(self):
		return self.note