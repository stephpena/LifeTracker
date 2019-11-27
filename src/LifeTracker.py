import src.depends
import src.constants

class LifeTracker(object):

    def __init__(self,format,players):
        with open(src.constants.format_file) as f:
            format_data = src.depends.json.load(f)

        self.life_start = int(format_data[format]['life_total'])
        self.deck_size = int(format_data[format]['deck_size'])
        self.deck_type = int(format_data[format]['deck_type'])
        self.sideboard = int(format_data[format]['sideboard'])
        self.max_card_copies = int(format_data[format]['max_card_copies'])
        self.life_total = self.life_start

    def get_life_total(self,reset=False):
        if reset == True:
            self.life_total = self.life_start
        else:
            x = int(input())
            self.life_total += x
        return self.life_total
