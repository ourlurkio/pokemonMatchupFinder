# Class MatchupPokemon used to initialise object with key attributes that can be appended to list in matchup_finder.py
# This can be then used to determine most efficient pokemon(s) to battle opponent

class MatchupPokemon():
    def __init__(self):
        self.mon_name = ''
        self.mon_type_1 = ''
        self.mon_type_2 = ''
        self.attack = 0
        self.sp_attack = 0
        self.type_attack_modifier = 1
        self.sprite = ''

    def update_mon_stats(self, json):
        """Takes json as argument(from matchup_data) then updates all attributes from query data"""
        self.mon_name = json['forms'][0]['name']
        self.mon_type_1 = json['types'][0]['type']['name']
        if len(json['types']) == 2:
            self.mon_type_2 = json['types'][1]['type']['name']
        self.attack = json['stats'][1]['base_stat']
        self.sp_attack = json['stats'][3]['base_stat']
        self.sprite = json['sprites']['front_default']

    def set_attack_type_modifier(self, weakness_types):
        if self.mon_type_1 in weakness_types and self.mon_type_2 in weakness_types:
            self.type_attack_modifier = 2



