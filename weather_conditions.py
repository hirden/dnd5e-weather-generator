from enum import Enum
from season import Season


# Seasons and their 'perfect day' counter values.
class SeasonEnum(Enum):
    SPRING = Season('Spring', 8, 3, 4)
    SUMMER = Season('Summer', 6, 0, 3)
    WINTER = Season('Winter', 11, 5, 5)
    FALL = Season('Fall', 9, 3, 4)


class Condition(Enum):
    BLIZZARD = 'Blizzard'
    MEDIUM_SNOWFALL = 'Medium Snowfall'
    LIGHT_SNOWFALL = 'Light Snowfall'
    HEAVY_RAIN_AND_LIGHTNING = 'Heavy Rain and Lightning'
    MEDIUM_RAINFALL = 'Medium Rainfall'
    LIGHT_RAINFALL = 'Light Rainfall'
    COOL_DAY = 'Cool Day'
    PERFECT_DAY = 'Perfect Day'
    WARM_DAY = 'Warm Day'
    HOT_DAY = 'Hot Day'
    VERY_HOT_DAY = 'Very hot Day'
    SCORCHING_HOT_DAY = 'Scorching hot Day'
