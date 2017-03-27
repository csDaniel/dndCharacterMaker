#!/usr/bin/python

from add_race import add_race
import sys, os








# language input
# language parser
#	dndChar make, build, play, help


class dnd(object):

	def error(self, msg):
		print("Error:\t {}".format(msg))

	def system(self):
		if len(sys.argv) != 2:
			self.error("expected usage <python dndChar.py [make, build, play, help]>")

		command = str(sys.argv[1]).lower()
		if command == 'make':
			self.make()
		elif command == "build":
			self.build()
		elif command == "play":
			self.play()
		elif command == "help":
			self.help()
		else:
			self.error("unknown command: {}".format(command))

	def make(self):
		print("make dnd char")

	def build(self):
		print("building DB...")

		race_db = add_race()


		print("Adding races...")
		with open('races') as fd:
			race_list = fd.read().split(', ')
		fd.close()
		for n in race_list:
			race_db.add_new_race(n)

		print("Setting sizes...")
		with open('medium races') as fd:
			race_list = fd.read().split(', ')
		fd.close()
		for n in race_list[1:]:
			race_db.add_new_size(n, 'medium')

		with open('small races') as fd:
			race_list = fd.read().split(', ')
		fd.close()
		for n in race_list[1:]:
			race_db.add_new_size(n, 'small')

		print("Setting speeds...")
		with open('speed 25') as fd:
			race_list = fd.read().split(', ')
		fd.close()
		for n in race_list[1:]:
			race_db.add_new_speed(n, 25)

		with open('speed 30') as fd:
			race_list = fd.read().split(', ')
		fd.close()
		for n in race_list[1:]:
			race_db.add_new_speed(n, 30)

		print("Setting stats...")
		with open('char stats') as fd:
			char_stats = fd.read().split(', ')
		fd.close()


		fixed_stats = []
		for i in char_stats:
			fixed_stats.append(i.strip())

		#print ("{}".format(fixed_stats))

		for n in range(0,len(fixed_stats),3):
			print repr("race: {}, \t{}: {}".format(fixed_stats[n],fixed_stats[n+1],fixed_stats[n+2]))
			race_db.add_new_stat(fixed_stats[n], fixed_stats[n+1], fixed_stats[n+2])


		# finish and output updated contents as raw
		#print race_db.load_races()


	def play(self):
		print("play dnd")

	def help(self):
		print("help commands")



def launcher():
	game = dnd()
	game.system()

launcher()