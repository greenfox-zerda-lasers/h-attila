# this is a design data file for elevator view app

building_roof = "\n      LEVEL \033[93m{}\x1b[0m, Pers. \033[93m{}\x1b[0m/\033[93m{}\x1b[0m       \n___________________________________\n`._______________________________.'"
building_body_with_elevator = "   || || {} || ||       || ||"
building_body_without_elevator = "   || ||       || ||       || ||"
building_ground_with_lift = "  _||_||_{}_||_||_______||_||_\n.'_______________________________`.\n"
building_ground_without_lift = "  _||_||_______||_||_______||_||_\n.'_______________________________`.\n"


elevator_empty = '[   ]'
elevator_1 = '[ \033[93mX\x1b[0m ]'
elevator_2 = '[\033[93mX X\x1b[0m]'
elevator_3 = '[\033[93mXXX\x1b[0m]'
elevator_full = '[\033[93mFUL\x1b[0m]'
elevator_more = '[\033[93m {} \x1b[0m]'


main_menu = '\n    What would you like to do?\n==================================\n\n  -> Move elevator up or down\n  -> Add people\n  -> Remove people\n\n  -> Exit program\n'
user_input = 'What is your choice?\n[\033[93m move \x1b[0m] [\033[93m add \x1b[0m] [\033[93m remove \x1b[0m] [\033[93m exit \x1b[0m]: '
new_level_input = 'What level want to go? [\033[93m number \x1b[0m] '
add_people_input = 'How many people want to add? [\033[93m number \x1b[0m] '
remove_people_input = 'How many people want to remove? [\033[93m number \x1b[0m] '