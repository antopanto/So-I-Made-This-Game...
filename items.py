class Storage():
	def __init__(self, name, slots=5, Type=''):
		self.slots = slots
		self.name = name
		self.type = Type

		self.s = {}

		self.genStorage()

	def genStorage(self):
		for i in range(1,self.slots+1): #xrange is a waste here.
			self.s[i] = None

	def addItem(self, item):
		for x,y in enumerate(self.s.values()):
			pos = x+1
			if y == None:
				self.s[pos] = item
				return True
		return False
	
	def rmvItem(self, slot):
		del self.s[slot]
		return True

	def popItem(self, slot):
		ret = self.s[slot]
		del self.s[slot]
		return ret

	def iterate(self): return self.s

	def __setitem__(self, item, value):
		self.s[item] = value
	
	def __getitem__(self, item):
		return self.s[item]

class BackPack(Storage):
	def __init__(self):
		self.id = 4
		Storage.__init__(self, 'Back Pack', 5, 'inventory')


class Food():
	def __init__(self, name, health=0, unhealth=0, poison=False, poisonChance=0):
		self.name = name
		self.type = 'food'
		self.health = health
		self.unhealth = unhealth
		self.poison = poison
		self.poisonChance = poisonChance
		self.alive = True

class Weapon():
	def __init__(self, name, damage=0, damageModifier=0, knockback=0, knockbackModifier=0, effect=None, durability=0, value=5):
		self.name = name
		self.type = 'weapon'
		self.damage = damage
		self.damageModifier = damageModifier
		self.knockback = knockback
		self.knockbackModifier = knockbackModifier
		self.effect = effect
		self.durability = durability
		self.value = value
		self.alive = True

	def genDamage(self):
		if self.damageModifier == 0: return (self.damage, self.knockback)
		else: return (self.damage*self.damageModifier, self.knockback*self.knockbackModifier)

class Apple(Food):
	def __init__(self):
		self.id = 0
		Food.__init__(self, 'Apple', 3)

class WoodSword(Weapon):
	def __init__(self):
		self.id = 1
		Weapon.__init__(self, 'Wood Sword', 3, 0, 0, 0, None, 30, 5)

class IronSword(Weapon):
	def __init__(self):
		self.id = 2
		Weapon.__init__(self, 'Iron Sword', 5, 0, 0, 0, None, 50, 15)
		
class GoldPlatedSword(Weapon):
	def __init__(self):
		self.id = 3
		Weapon.__init__(self, 'Gold Plated Sword', 10, 0, 0, 0, None, 75, 55)


itemz = {
	0:Apple,
	1:WoodSword,
	2:IronSword,
	3:GoldPlatedSword,
	4:BackPack,
}