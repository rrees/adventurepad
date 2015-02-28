from hero import hero
from models import Combatant
from dice import d6

def resolve_fight(player, monster):
	results = []
	while(player.health > 0 and monster.health > 0):
	
		player_attack_score = player.attack_score()
		monster_attack_score = monster.attack_score()
	
		if(player_attack_score > monster_attack_score):
			monster.health = monster.health - (d6() + player.brawn - monster.armour) 
	
		if(player_attack_score < monster_attack_score):
			player.health = player.health - (d6() + monster.brawn - player.armour)
		
		results.append({'player' : {'health' : player.health}, 'monster' : {'health' : monster.health}})
		
	return results
