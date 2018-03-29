# Author: B122980

import unittest
from soldier import *
from squad import *


class TestSoldier(unittest.TestCase):

	# test set/get methods

	# for move_points
	def test_set_move_upper_limit(self):
		soldier = Soldier()
		soldier.set_move(60)

		self.assertEqual(soldier.get_move(), 0, "The move points take values between 0 and 50")

	def test_set_move_low_limit(self):
		soldier = Soldier()
		soldier.set_move(-60)

		self.assertEqual(soldier.get_move(), 0, "The move points take values between 0 and 50")

	def test_set_get_move(self):
		soldier = Soldier()
		soldier.set_move(10)
		
		self.assertEqual(soldier.get_move(), 10, "The set_move method does not initialise the right values")

	# for fight points
	def test_set_fight_upper_limit(self):
		soldier = Soldier()
		soldier.set_fight(60)

		self.assertEqual(soldier.get_fight(), 0, "The fight points take values between 0 and 50")

	def test_set_fight_low_limit(self):
		soldier = Soldier()
		soldier.set_fight(-60)

		self.assertEqual(soldier.get_fight(), 0, "The fight points take values between 0 and 50")

	def test_set_get_fight(self):
		soldier = Soldier()
		soldier.set_fight(10)
		
		self.assertEqual(soldier.get_fight(), 10, "The set_fight method does not initialise the right values")

	# for shoot points
	def test_set_shoot_upper_limit(self):
		soldier = Soldier()
		soldier.set_shoot(60)

		self.assertEqual(soldier.get_shoot(), 0, "The shoot points take values between 0 and 50")

	def test_set_shoot_low_limit(self):
		soldier = Soldier()
		soldier.set_shoot(-60)

		self.assertEqual(soldier.get_shoot(), 0, "The shoot points take values between 0 and 50")

	def test_set_get_shoot(self):
		soldier = Soldier()
		soldier.set_shoot(10)
		
		self.assertEqual(soldier.get_shoot(), 10, "The set_shoot method does not initialise the right values")

	# for armour
	def test_set_armour_upper_limit(self):
		soldier = Soldier()
		soldier.set_armour(60)

		self.assertEqual(soldier.get_armour(), 0, "The armour points take values between 0 and 50")

	def test_set_armour_low_limit(self):
		soldier = Soldier()
		soldier.set_armour(-60)

		self.assertEqual(soldier.get_armour(), 0, "The armour points take values between 0 and 50")

	def test_set_get_armour(self):
		soldier = Soldier()
		soldier.set_armour(10)
		
		self.assertEqual(soldier.get_armour(), 10, "The set_armour method does not initialise the right values")

	# for morale
	def test_set_morale_upper_limit(self):
		soldier = Soldier()
		soldier.set_morale(60)

		self.assertEqual(soldier.get_morale(), 0, "The morale points take values between 0 and 50")

	def test_set_morale_low_limit(self):
		soldier = Soldier()
		soldier.set_morale(-60)

		self.assertEqual(soldier.get_morale(), 0, "The morale points take values between 0 and 50")

	def test_set_get_morale(self):
		soldier = Soldier()
		soldier.set_morale(10)
		
		self.assertEqual(soldier.get_morale(), 10, "The set_morale method does not initialise the right values")

	# for health
	def test_set_health_upper_limit(self):
		soldier = Soldier()
		soldier.set_health(60)

		self.assertEqual(soldier.get_health(), 0, "The health points take values between 0 and 50")

	def test_set_health_low_limit(self):
		soldier = Soldier()
		soldier.set_health(-60)

		self.assertEqual(soldier.get_health(), 0, "The health points take values between 0 and 50")

	def test_set_get_health(self):
		soldier = Soldier()
		soldier.set_health(10)
		
		self.assertEqual(soldier.get_health(), 10, "The set_health method does not initialise the right values")

	# for cost
	def test_set_cost_upper_limit(self):
		soldier = Soldier()
		soldier.set_cost(60)

		self.assertEqual(soldier.get_cost(), 0, "The cost points take values between 0 and 50")

	def test_set_cost_low_limit(self):
		soldier = Soldier()
		soldier.set_cost(-60)

		self.assertEqual(soldier.get_cost(), 0, "The cost points take values between 0 and 50")

	def test_set_get_cost(self):
		soldier = Soldier()
		soldier.set_cost(10)
		
		self.assertEqual(soldier.get_cost(), 10, "The set_cost method does not initialise the right values")


	# for notes
	def test_set_get_note(self):
		soldier = Soldier()
		soldier.set_note("This soldier is carring a shild")
		
		self.assertNotEqual(soldier.get_note(), " ", "The set_note method does not set the description of the soldier")



class TestSquad(unittest.TestCase):

	# credit is decreasing
	def test_decreasing_of_credit(self):
		soldier = Soldier()
		cost = 40
		soldier.set_cost(cost)

		squad = Squad()
		squad.set_name("Test Squad")
		squad.set_visibility(True)
		squad.add_member(soldier)

		self.assertEqual(squad.get_credit(), 500 - cost, "When buying soldiers credit is not decreasing")

	# credit is growing
	def test_growing_of_credit(self):
		soldier = Soldier()
		cost = 40
		soldier.set_cost(cost)

		squad = Squad()
		squad.set_name("Test Squad")
		squad.set_visibility(True)
		squad.add_member(soldier)
		squad.add_member(soldier)
		squad.add_member(soldier)

		squad.delete_member(soldier)

		self.assertEqual(squad.get_credit(), 500 - (cost * 3) + cost, "When buying soldiers credit is not decreasing")


	# adding soldiers in the squad
	def test_create_squad_3_members(self):
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

		self.assertEqual(len(squad.get_members()), 3, "Adding members does not work")


if __name__ == '__main__':
    unittest.main()
