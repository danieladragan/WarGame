# Author: B122980

from captain import *
from hierophant import *
from soldier import *

class Squad:
	members = []		# list of objects (Soldier, Captain, Hierophant)
	credit = 500  		# integer
	name = " "			# string
	visibility = True	# boolean - true for public, false for private
	stash =[]	    	# list of weapons/equipment (strings)

	def __init__(self):
		captain = Captain()
		hierophant = Hierophant()
		self.members = [captain, hierophant]

	# only when creating the squad
	def set_name(self, new_name):
		self.name = new_name

	def add_credit(self, amount):
		self.credit = self.credit + amount

	def get_credit(self):
		return self.credit
	
	# modify the credit; the credit < 0 is not possible
	def add_member(self, new_member):
		if isinstance(new_member, Soldier):
			if len(self.members) <= 10:
				self.members.append(new_member)
				self.credit = self.credit - new_member.cost
			else:
				print "The squad has a limit of 10 members"
		else:
			print "Only soldiers can be added in a squad!"

	def delete_member(self, member):
		if isinstance(member, Soldier):
			self.members.remove(member)
			self.credit = self.credit + member.cost
		else:
			print "The Captain and Hierophant can not be deleted!"

	def get_members(self):
		return self.members

	def set_visibility(self, new_visibility):
		self.visibility = new_visibility

	def get_visibility(self):
		return self.visibility

	def display_credit(self):
		print "For the "+ self.name + " squad the credit is "\
				 + str(self.credit)

	def add_stash(self, new_item):
		self.stash.append(new_item)

	def remove_stash(self, item):
		self.stash.remove(item)

	def __str__(self):
		if self.visibility is True:
			return "This squad has " + str(len(self.members)) + " members"
		else:
			return "You are not allowed to see the members of this squad!"


if __name__ == "__main__":
	s = Squad()
	s.set_name("Miraculous squad")
	s.display_credit()
	s.add_credit(10)
	s.display_credit()
	print s

	soldier = Soldier()

	soldier.set_move(10)
	soldier.set_cost(40)
	soldier.set_health(30)
	soldier.set_armour(50)
	soldier.set_morale(40)
	soldier.set_shoot(5)
	soldier.set_fight(20)

	squad = Squad()
	squad.set_name("Test Squad")
	squad.set_visibility(True)
	squad.add_member(soldier)

	print len(squad.get_members())