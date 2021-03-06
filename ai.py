import time
from modules import astar

class AI():
	def __init__(self, name, player, attack=1, health=5, Map=0, char='+', speed=.5, attackSpeed=1,color=(255,255,255)): 
		global game
		import game
		self.name = name
		self.player = player
		self.attack = attack
		self.health = [health, health]
		self.map = Map
		self.char = char
		self.color = color
		self.speed = speed
		self.attackSpeed = attackSpeed
		self.goal = 'player' #player/entity
		self.pathFindy = astar.AStar()

		self.type = 'bot'
		self.alive = False
		self.pos = [10, 10]

		self.combatmode = 0
		self.lastmove = time.time()
		self.lastattack = time.time()
	
	def spawn(self, pos=[11,11]):
		self.alive = True
		self.pos = pos
		return self

	def attackPlayer(self): 
		print 'attacked'
		self.combatmode = 1
		self.player.attackMode(self)
		self.pos = [2,2]
		self.map = 0

	def attackEntity(self): pass

	def collide(self, ent):
		if ent.type == 'projectile':
			self.unheal(ent.damage)
			return True

	def move(self):
		if time.time() - self.lastmove >= self.speed and self.alive is True:
			self.lastmove = time.time() #@NOTE Make sure this stays put. Will wreck shit otherwise (the returns cancel it out)
			if self.goal == 'player':
				self.pathFindy.findPath(tuple(self.player.pos), tuple(self.pos), self.player.levels[str(self.map)].hitMap) 
				f = self.pathFindy.path
				if len(f) > 2: 
					self.pos = list(f[1])
					return True
				else: #@NOTE We dont actually move anywhere here, so why re-render?
					if time.time() - self.lastattack >= self.attackSpeed:
						if self.player.mode is 1:
							self.attackPlayer()
						elif self.player.mode is 0:
							self.player.attacked(self.attack)
						self.lastattack = time.time()
						return True	
	
	def die(self):
		if self.combatmode == 1 and self.player.mode == 0:
			self.player.wonBattle()
		self.health[0] = 0
		self.alive = False

	def unheal(self, amount):
		if self.health[0]-amount < 0: self.die()
		else: self.health[0]-=amount

class Pos():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.pos = lambda: [x,y]

def attackModel(botPos, goalPos): pass