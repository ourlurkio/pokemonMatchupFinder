import requests
# Class TargetPokemon used to take user input (i.e. mon they are battling), query API, and save attributes to class.
# Object initialised and used within match-up engine for further processing

endpoint = 'https://pokeapi.co/api/v2/pokemon/'

class TargetPokemon():
    def __init__(self):
        self.mon_name = ''
        self.mon_type_1 = ''
        self.mon_type_2 = ''
        self.defense = 0
        self.sp_defense = 0
        self.sprite = ''

    def get_target_mon_data(self, user_input):
        """Function takes input target pokemon, queries API and returns json. If error passed from query, return
        error message"""
        query = user_input.lower()
        try:
            response = requests.get(f'{endpoint}{query}')
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.HTTPError as e:
            return "Error: " + str(e)

    def update_mon_stats(self, json):
        """Takes json as argument(from get_target_mon_data), and checks if format is a json or string. If string,
        prints error message as no such pokemon, as string is generated from error message of get_target_mon_data.
        If json is passed, then updates all attributes from query data"""
        if type(json) == str:
            print('No such Pokemon!')
        else:
            self.mon_name = json['forms'][0]['name']
            self.mon_type_1 = json['types'][0]['type']['name']
            if len(json['types']) == 2:
                self.mon_type_2 = json['types'][1]['type']['name']
            self.defense = json['stats'][2]['base_stat']
            self.sp_defense = json['stats'][4]['base_stat']
            self.sprite = json['sprites']['front_default']

