#!/usr/bin/python

import os, sys
import json
import pprint


class add_race(object):
	def __init__(self):
		self.languages = [
			'common',
			'elvish',
			'halfling',
			'giant',
			'orc',
			'goblin',
			'auran',
			'draconic',
			'kor silent speech',
			'merfolk',
			'arakocra',
			'drwarf',
			'drow hand signs',
			'abyssal',
			'infernal',
			'primordial',
			'vampire'
			]
		self.stats = [
			'strength',
			'dexterity',
			'constitution',
			'intelligence',
			'wisdom',
			'charisma'
			]
		self.size = [
			'small',
			'medium'
			]

	def error_message(self, msg):
		print("error:\t {}".format(msg))

	def clear_dnd_file(self):
		fd = open('dnd_races', 'w')
		fd.write('')
		fd.close()

	def load_races(self):
		contents = self._get_dnd_race_file()
		pprint.pprint(contents)

	def _get_dnd_race_file(self):
		try:
			with open('dnd_races') as fd:
				# http://stackoverflow.com/questions/2507808/python-how-to-check-file-empty-or-not
				# ensure contents weren't deleted
				fd.seek(0)
				first_char = fd.read(1)
				if not first_char:
					contents = {}
				else:
					fd.seek(0)
					contents = json.load(fd)
			fd.close()
		except IOError:
			contents = {}

		return contents

	def _update_dnd_race_file(self, contents):
		filedesc = open('dnd_races', 'w')
		filedesc.write(json.dumps(contents))
		filedesc.write('\n')
		filedesc.close()

	def add_new_race(self, race):
		# open and place json file as dict. Else, make new dict
		contents = self._get_dnd_race_file()

		# add the new race
		new_race = {}
		new_race[race] = {}
		profile = new_race[race]
		profile['stats'] = {}
		profile['languages'] = []
		profile['extra'] = []
		profile['speed'] = None
		profile['size'] = None

		if race not in contents:
			contents[race] = profile
		else:
			self.error_message("Race already exists")
		
		self._update_dnd_race_file(contents)

	def add_new_speed(self, race, speed):
		contents = self._get_dnd_race_file()

		if race not in contents:
			self.error_message("Race not found! Creating new race \"{}\"...".format(race))
			self.add_new_race(race)

		contents[race]['speed'] = speed

		self._update_dnd_race_file(contents)

	def add_new_stat(self, race, stat, value):
		#print("adding new stat")

		contents = self._get_dnd_race_file()
		stat_found = False

		if race not in contents:
			self.error_message("Race not found! Creating new race {}...".format(race))
			self.add_new_race(race)

		if stat not in self.stats:
			self.error_message("Stat name {} not found in stat list".format(stat))
		else:
			stat_found = True

		if stat_found:
			if contents[race]['stats'][stat]:
				contents[race]['stats'][stat] += value
			else:
				contents[race]['stats'][stat] = value

		self._update_dnd_race_file(contents)

	def add_new_language(self, race, language):
		#print("adding new language")

		contents = self._get_dnd_race_file()
		language_found = False

		if race not in contents:
			self.error_message("Race not found! Creating new race...")
			self.add_new_race(race)

		if language not in self.languages:
			self.error_message("Langauage name: {} not found in language list".format(language))			
		else:
			language_found = True

		if language_found and language not in contents[race]['languages']:
			contents[race]['languages'].append(language)
		else:
			self.error_message("{} already has language: {}".format(race, language))

		self._update_dnd_race_file(contents)

	def add_new_size(self, race, size):
		contents = self._get_dnd_race_file()
		size_found = False

		if race not in contents:
			self.error_message("Race not found! Creating new race...")
			self.add_new_race(race)

		if size not in self.size:
			self.error_message("Size: {} not found in size list".format(size))
		elif contents[race]['size'] is not None:
			self.error_message("{} size already set".format(race))
		else:
			size_found = True

		#print("Attempting to add new size: {}, found: {}".format(size, size_found))
		if size_found and contents[race]['size'] is None:
			contents[race]['size'] = size

		self._update_dnd_race_file(contents)


	def add_new_extra(self, race, extra):
		#print("adding new extra")

		contents = self._get_dnd_race_file()

		if race not in contents:
			self.error_message("Race not found! Creating new race...")
			self.add_new_race(race)

		if extra not in contents[race]['extra']:
			contents[race]['extra'].append(extra)
		else:
			self.error_message("{} already has extra {}".format(race, extra))

		self._update_dnd_race_file(contents)



