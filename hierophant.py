# Author: B122980

from superior_soldier import *
from game_data import *

class Hierophant(Superior_Soldier):

	def set_specialsm(self, specialism):
		available_specialisms = HIEROPHANT_SPECIALISM.keys()

		if specialism in available_specialisms:
			self.specialism = specialism
		else:
			print "The specialism selected does nor exist"

	def set_skillset(self, skill):
		available_skills = HIEROPHANT_SPECIALISM.get(self.specialism)

		if skill in available_skills:
			self.skillset.append(skill)
		else:
			print "This skill is not available"

	def add_weapon(self, weapon):
		if len(self.weapons) <= HIEROPHANT_WEAPONS:
			self.weapons.append(weapon)
		else:
			print "The Hierophant has the right to 1 weapon"
	
	def add_equipment(self, equipment):
		if len(self.weapons) + len(self.equipment) <= HIEROPHANT_ITEMS:
			self.equipment.append(equipment)
		else:
			print "The Hierophant has the right to 4 items"