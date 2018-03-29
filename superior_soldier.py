# Author: B122980

from soldier import *

class Superior_Soldier(Soldier):
	experience = 0		# integer (0 - 30; default 0)
	specialism = " "	# string (from list of specialist skills)
	skillset = []		# list of strings (many skills from the list of skills set)
	weapons	= {}		# dictionary of strings:fight_points (many weapons from the weapons list)
	equipment = {}		# dictionary of of strings:armour_points (many equipments from the equiments list)

	
	# set methods

	def set_experience(self, new_experience):
		self.experience = new_experience

	def set_specialsm(self, specialism):
		pass

	def set_skillset(self, skill):
		pass

	def set_weapons(self, weapon, fight_points):
		self.weapons[weapon] = fight_points

	def set_equipment(self, equipment, armour_points):
		self.equipment[equipment] = armour_points

	
	# methods used when playing 
	
	def add_experience(self, experience_points):
		self.experience = self.experience + experience_points

	# choose new skills, weapons, equipment 

	def add_skill(self, skill):
		if skill not in self.skillset:
			self.skillset.append(skill)
		else:
			print "Skill already in the skill set"

	def add_weapon(self, weapon):
		pass
	
	def add_equipment(self, equipment):
		pass

	def remove_skill(self, skill):
		if skill in self.skillset:
			skillset.remove(skill)

	def remove_weapon(self, weapon):
		if weapon in self.weapons:
			self.weapons.remove(weapon)

	def remove_equipment(self, equipment):
		if equipment in self.equipment:
			self.equipment.remove(equipment)

	
	# increase the starts by 1 point (when gaining enough experience)
	def add_move(self):
		self.move = self.move + 1

	def add_fight(self):
		self.fight = self.fight + 1

	def add_shoot(self):
		self.shoot = self.shoot + 1

	def add_armour(self):
		self.armour = self.armour + 1

	def add_morale(self):
		self.morale = self.morale + 1
	
	def add_health(self):
		self.health = self.health + 1

	# decrease the stats when getting attacked
	def decrease_move(self, move_points):
		self.move = self.move - move_points

	def decrease_fight(self, fight_points):
		self.fight = self.fight - fight_points

	def decrease_shoot(self, shoot_points):
		self.shoot = self.shoot - shoot_points

	def decrease_armour(self, armour_points):
		self.armour = self.armour - armour_points

	def decrease_morale(self, morale_points):
		self.morale = self.morale - morale_points
	
	def decrease_health(self, health_points):
		self.health = self.health - health_points 	



if __name__ == "__main__":
	s = Superior_Soldier()
	s.set_experience(10)
	print s.experience

	s.add_experience(10)
	print s.experience