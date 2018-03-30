# Author: B122980

from superior_soldier import *
from game_data import *

class Captain(Superior_Soldier):

	# set specialism tree available for Captain
	def set_specialsm(self, specialism):
		available_specialisms = CAPTAIN_SPECIALISM.keys()

		if specialism in available_specialisms:
			self.specialism = specialism
		else:
			print "The specialism selected does nor exist"

	# set skillset from the available skills of Captain
	def set_skillset(self, skill):
		available_skills = CAPTAIN_SPECIALISM.get(self.specialism)

		if skill in available_skills:
			self.skillset.append(skill)
		else:
			print "This skill is not available"

	# add items (weapon and equipment)

	def add_weapon(self, weapon):
		if len(self.weapons) <= CAPTAIN_WEAPONS:
			self.weapons.append(weapon)
		else:
			print "The Captain has the right to 2 weapons"
	
	def add_equipment(self, equipment):
		if len(self.weapons) + len(self.equipment) <= CAPTAIN_ITEMS:
			self.equipment.append(equipment)
		else:
			print "The Captain has the right to 6 items"