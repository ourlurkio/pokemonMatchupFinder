import target_pokemon
import matchup_pokemon
import search_engine
import json

print('Welcome to the pokemon match-up calculator! This will take you inputted pokemon \n'
      'opponent and output the recommended best pokemon you could use! Have fun!')

endpoint = 'https://pokeapi.co/api/v2/pokemon/'
user_input = input('\nWho is your opponent?!\n')

# Initialise target pokemon object, and update all stats

opponent = target_pokemon.TargetPokemon()
opponent.update_mon_stats(opponent.get_target_mon_data(user_input))

# Iterate through matchup_chart.json to find types opponent is weak against, and add types to weakness_types list

weakness_types = []
with open('matchup_chart.json') as f:
    matchup_data = json.load(f)
    f.close()

for attack_type in matchup_data:
    for defense_type in matchup_data[attack_type]:
        if opponent.mon_type_1 == defense_type and matchup_data[attack_type][defense_type] == 2:
              weakness_types.append(attack_type)

#use search_engine to search through all pokemon, and initialise matchup_pokemon objects for pokemon with strong type
#vs opponent

search_engine = search_engine.SearchEngine()
strong_mon_object_list = []
check_pokemon = True

while check_pokemon:
    print(search_engine.pokemon_id)
    matchup_data = search_engine.get_other_mon_data()
    strong = search_engine.check_if_mon_strong(weakness_types, matchup_data)
    # print(matchup_data['forms'][0]['name'])
    if strong == 'strong':
        matchup_mon = matchup_pokemon.MatchupPokemon()
        matchup_mon.update_mon_stats(matchup_data)
        matchup_mon.set_attack_type_modifier(weakness_types)
        strong_mon_object_list.append(matchup_mon)
    elif not strong:
        check_pokemon = False

#generate list of names to present to the user
name_list_strong_mons = []
for mon in strong_mon_object_list:
    name_list_strong_mons.append(mon.mon_name)

#loop through list of strong mons, and extract all mons with best offensive stat vs opponent lowest defensive stat
best_mon = strong_mon_object_list[0]

#check if opponent defense > sp_defense, and if so a pokemon with high sp_attack is preferred
if opponent.defense > opponent.sp_defense:
    for mon in strong_mon_object_list:
        if mon.sp_attack >= best_mon.sp_attack:
            best_mon = mon
else:
    for mon in strong_mon_object_list:
        if mon.attack >= best_mon.attack:
            best_mon = mon

print(f'The Pokemons best suited to fight {opponent.mon_name} are:\n{name_list_strong_mons}')
print(f'The best Pokemon against your opponent,{opponent.mon_name}, is {best_mon.mon_name}')




