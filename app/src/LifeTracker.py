import src.depends as depends
import src.constants as constants

class LifeTracker(object):

    def __init__(self,format,players=2):
        with open(constants.format_file) as f:
            format_data = depends.json.load(f)

        self.life_start = int(format_data[format]['life_total'])
        self.deck_size = int(format_data[format]['deck_size'])
        self.deck_type = int(format_data[format]['deck_type'])
        self.sideboard = int(format_data[format]['sideboard'])
        self.max_card_copies = int(format_data[format]['max_card_copies'])
        self.life_total = self.life_start
        self.players = players

    def get_life_total(self,life_adjust=0,reset=False):
        if reset == True:
            self.life_total = self.life_start
        else:
            self.life_total += life_adjust

        if self.life_total <= 0:
            self.life_total = 0
        return self.life_total
