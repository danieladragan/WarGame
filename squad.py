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

	def set_name(self, new_name):
		self.name = new_name

	def add_credit(self, amount):
		self.credit = self.credit + amount

	def get_credit(self):
		return self.credit

	def get_members(self):
		return self.members

	def set_visibility(self, new_visibility):
		self.visibility = new_visibility

	def get_visibility(self):
		return self.visibility
	
	# function for adding a soldier in the team
	def add_member(self, new_member):
		if isinstance(new_member, Soldier):
			if len(self.members) <= 10:
				self.members.append(new_member)
				self.credit = self.credit - new_member.cost
			else:
				print "The squad has a limit of 10 members"
		else:
			print "Only soldiers can be added in a squad!"

	# function for deleting a soldier from a team
	def delete_member(self, member):
		if isinstance(member, Soldier):
			self.members.remove(member)
			self.credit = self.credit + member.cost
		else:
			print "The Captain and Hierophant can not be deleted!"

	# display the users' credit
	def display_credit(self):
		print "For the "+ self.name + " squad the credit is "\
				 + str(self.credit)

	# adding and removing items in/from stash
	def add_stash(self, new_item):
		self.stash.append(new_item)

	def remove_stash(self, item):
		self.stash.remove(item)

	def __str__(self):
		if self.visibility is True:
			return "This squad has " + str(len(self.members)) + " members"
		else:
			return "You are not allowed to see the members of this squad!"