print("my Bard")

class dnd(object):
	def __init__(self):
		self.name = None
		self.profession = None
		self.race = None
		self.stats = {}
		self.abilities = ""
		self.notes = "lore!"
		# skills, abilities, spells 

	def get_stats(self):
		print("Name: {}".format(self.name))
		print("Race: {}".format(self.race))
		print("Profession: {}".format(self.profession))
		for (k, v) in self.stats.items():
			print("{}: {}".format(k,v))


		print("Abilities: {}".format(self.abilities))


	def set_name(self):
		print("name")

	def add_profession(self):
		print("profession")

	def add_race(self):
		print("race")

	def init_stats(self):
		self.stats["strength"] = 10
		self.stats["dexterity"] = 14
		self.stats["constitution"] = 13
		self.stats["intelligence"] = 12
		self.stats["wisdom"] = 8
		self.stats["charisma"] = 15
	#init_stats()
		# 15, 14, 13, 12, 10, 8
		# strength, dexterity, constitution, intelligence, wisdom, charisma

	def set_race(self):
		n = raw_input("Select a race: ")

		if n == "half-elf":
			self.race = "Half-Elf"
			self.stats["charisma"] += 2

			#update 2 more skills
			m = raw_input("Select two skills to add +1 to: ")
			two_skills = m.split(',')
			for skill in two_skills:
				if skill in self.stats:
					self.stats[skill] += 1
			if self.abilities == "":
				self.abilities = "darkvision, fey ancestry, skill versatility"
			else:
				self.abilities.append(", darkvision, fey ancestry, skill versality")
		else:
			print("Sorry, I only know half-elf")

	def set_profession(self):
		n = raw_input("Select a profession: ")
		if n == "bard":
			self.profession = "Bard"


def build_char():
	char = dnd()
	char.init_stats()
	char.set_race()
	char.set_profession()
	char.set_name()

	char.get_stats()

build_char()

