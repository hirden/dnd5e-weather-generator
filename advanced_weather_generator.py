from weather_conditions import SeasonEnum
from weather_conditions import Condition
import season
import secrets

_conditions = {
    11: (Condition.BLIZZARD, [SeasonEnum.WINTER]),
    10: (Condition.MEDIUM_SNOWFALL, [SeasonEnum.WINTER]),
    9: (Condition.LIGHT_SNOWFALL, [SeasonEnum.WINTER, SeasonEnum.FALL]),
    8: (Condition.HEAVY_RAIN_AND_LIGHTNING, [SeasonEnum.FALL, SeasonEnum.SPRING]),
    7: (Condition.MEDIUM_RAINFALL, [SeasonEnum.FALL, SeasonEnum.SPRING]),
    6: (Condition.LIGHT_RAINFALL, [SeasonEnum.FALL, SeasonEnum.SPRING, SeasonEnum.SUMMER]),
    5: (Condition.COOL_DAY, [SeasonEnum.WINTER, SeasonEnum.FALL, SeasonEnum.SPRING, SeasonEnum.SUMMER]),
    4: (Condition.PERFECT_DAY, [SeasonEnum.FALL, SeasonEnum.SPRING, SeasonEnum.SUMMER]),
    3: (Condition.WARM_DAY, [SeasonEnum.FALL, SeasonEnum.SPRING, SeasonEnum.SUMMER]),
    2: (Condition.HOT_DAY, [SeasonEnum.SUMMER]),
    1: (Condition.VERY_HOT_DAY, [SeasonEnum.SUMMER]),
    0: (Condition.SCORCHING_HOT_DAY, [SeasonEnum.SUMMER])
}


def _roll_d6():
    return secrets.randbelow(6) + 1


def _determine_counter(counter, season: season):
    d6_roll = _roll_d6()
    if d6_roll is 6:
        c = counter + 2
    elif d6_roll is 5:
        c = counter + 1
    elif d6_roll is 4 or d6_roll is 3:
        # Check the season perfect day value
        if counter > season.perfect_count:
            c = counter - 1
        elif counter < season.perfect_count:
            c = counter + 1
        else:
            c = counter
    elif d6_roll is 2:
        c = counter - 1
    elif d6_roll is 1:
        c = counter - 2
    else:
        c = counter

    if c < season.min_count:
        return season.min_count
    elif c > season.max_count:
        return season.max_count
    return c


def generate_weather(season: SeasonEnum, counter=None):
    _season = season.value
    if counter is None:
        counter = _season.perfect_count

    previous_counter = counter
    counter = _determine_counter(counter, _season)
    if previous_counter < counter < _season.max_count:
        while season not in _conditions[counter][1]:
            counter += 1
    elif previous_counter > counter > _season.min_count:
        while season not in _conditions[counter][1]:
            counter -= 1
    return {'counter': counter, 'condition': _conditions[counter]}


def print_weather_condition_info():
    print()
    print('Weather Complications')
    print('Bad weather can cause complications. A terrible rain storm may delay adventure’s travels, or a blizzard\n'
          'may be the perfect opportunity for a sneak attack. Here are some ideas for possible complications for each\n'
          'storm.')
    print()
    print('Blizzard:')
    print('The temperature outside is perilous. Adventures could freeze to death without correct gear. Anyone outside\n'
          'suffers from Extreme Cold (See Dungeon Masters Guide Pg:110.) Creatures have disadvantage on perception\n'
          'checks and advantage on stealth checks. The ground is covered in snow and is considered difficult terrain.\n'
          'Most roads are blocked by snow.')
    print()
    print('Medium Snowfall:')
    print('Creatures have disadvantage on perception checks and advantage on stealth checks. At night, anyone outside\n'
          'suffers from Extreme Cold (See Dungeon Masters Guide Pg:110.) If the snow fall lasts several days,\n'
          'the terrain becomes difficult.')
    print()
    print('Light Snowfall:')
    print('Creatures have disadvantage on perception checks.')
    print()
    print('Heavy Rain and Lightning:')
    print('Creatures have disadvantage on perception checks and advantage on stealth checks. When outside,\n'
          'getting hit by lightning is a deadly possibility. In combat, roll a d100 before each creature’s turn. Out\n'
          'of combat, roll randomly. On a 1 the creature is stuck by lightning. The creature is then targeted by a\n'
          'Call Lighting Spell (Spell Save 18).')
    print()
    print('Medium Rainfall:')
    print('Creatures have disadvantage on perception checks and advantage on stealth checks.')
    print()
    print('Light Rainfall: ')
    print('Creatures have disadvantage on perception checks.')
    print()
    print('Very Hot Day:')
    print('Characters outside are subject to Extreme Heat (Dungeon Masters Guide Pg:110.)')
    print()
    print('Scorching Hot Day:')
    print('Characters outside are subject to Extreme Heat (Dungeon Masters Guide Pg:110.) Characters gain no benefit '
          'from a short or long rest while in an area affected by this weather condition.')
    print()


def pretty_print_weather_list(weather_list):
    print('+--------------------------+')
    for weather in weather_list:
        #        Heavy Rain and Lightning
        print('| ' + '{:<24}'.format(weather[0].value) + ' |')
    print('+--------------------------+')
    print_weather_condition_info()
