from constants import *

name = 'Длинноволосая брюнетка'

hp = 120
element = NONE
damage_range =  ( 16, 18 )

coins = 25

loot = [ 'laser_gun' ]

def enter(user, reply):
	reply('Ан, нет. Это чубака')

	if user.has_aura(AURA_BUDDHA):
		reply('Чубака уважает буддистов, правда не знает, кто это, но уважает.')
		user.leave(reply)