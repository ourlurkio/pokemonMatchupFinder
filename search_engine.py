import requests
# Class SearchEngine is used to query all pokemon, identify if that pokemon is strong vs TargetPokemon, and if so
#return True and pass json to MatchedPokemon class for initialisation

endpoint = 'https://pokeapi.co/api/v2/pokemon/'
test_list = ['grass', 'fire', 'water']

class SearchEngine():
    def __init__(self):
        self.pokemon_id = 1

    def get_other_mon_data(self):
        """Function queries API based on input pokemon id, and returns data as json"""
        query = self.pokemon_id
        try:
            response = requests.get(f'{endpoint}{query}')
            response.raise_for_status()
            data = response.json()
            self.pokemon_id += 1
            return data
        except requests.exceptions.HTTPError as e:
            return "Error: " + str(e)
            self.pokemon_id = 1

    def check_if_mon_strong(self, weakness_types, json):
        """Takes pokemon data as json, and checks if type is listed in weakness_type. If in list, return True and json
        to be passed to MatchedPokemon for initialisation"""
        if type(json) == str:
            #retuns false as str means all pokemon queried, and get_all_mon_data has returned an error message
            return False
            #if a json returned, checks the types against weakness_types list, and if present returns True.
            # matchup_finder.py then initialises a matchup_pokemon object for that pokemon
        else:
            if json['types'][0]['type']['name'] in weakness_types:
                return 'strong'
            try:
                if json['types'][1]['type']['name'] in weakness_types:
                    return 'strong'
                else:
                    return 'not strong'
            except IndexError:
                if type(json) == str:
                    # retuns false as str means all pokemon queried, and get_all_mon_data has returned an error message
                    return False
                else:
                    return 'not strong'

