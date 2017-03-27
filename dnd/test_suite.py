#!/usr/bin/python

from add_race import add_race
import pprint


def test_get_race():

	char = add_race()

	#old = char._get_dnd_race_file()
	#pprint.pprint(old)
	char.load_races()


def test_add_race(race):
	char = add_race()
	char.add_new_race(race)

def test_add_race_stat(race, stat, value):
	char = add_race()
	char.add_new_stat(race, stat, value)

def test_add_race_extra(race, value):
	char = add_race()
	char.add_new_extra(race, value)

def test_add_race_size(race, value):
	char = add_race()
	char.add_new_size(race, value)

def test_clear_dnd_file():
	char = add_race()
	char.clear_dnd_file()

def run_test():
	'''
	n = ['merfolk', 'human', 'half-elf', 'orc']
	for name in n:
		test_add_race(name)

	test_add_race_stat('human', 'charisma', 2)	
	test_add_race_stat('orc', 'strength', 2)

	test_add_race_extra('orc', 'Super angry all the time')
	test_add_race_extra('orc', 'nightvision')
	test_add_race_extra('merfolk', 'nightvision')

	test_get_race()
	'''
	#test_clear_dnd_file()
	test_get_race()

run_test()