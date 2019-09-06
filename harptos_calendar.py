from enum import Enum

from weather_conditions import SeasonEnum

DAYS_IN_MONTH = 30
MONTHS_IN_YEAR = 12
DAYS_IN_YEAR = DAYS_IN_MONTH * MONTHS_IN_YEAR + 5


class Month(Enum):
    Hammer = 1
    Alturiak = 2
    Ches = 3
    Tarsakh = 4
    Mirtul = 5
    Kythorn = 6
    Flamerule = 7
    Eleasis = 8
    Eleint = 9
    Marpenoth = 10
    Uktar = 11
    Nightal = 12

    def get_month_common_name(self):
        if self is Month.Hammer:
            return 'Deepwinter'
        if self is Month.Alturiak:
            return 'The Claw of Winter'
        if self is Month.Ches:
            return 'The Claw of the Sunsets'
        if self is Month.Tarsakh:
            return 'The Claw of the Storms'
        if self is Month.Mirtul:
            return 'The Melting'
        if self is Month.Kythorn:
            return 'The Time of Flowers'
        if self is Month.Flamerule:
            return 'Summertide'
        if self is Month.Eleasis:
            return 'Highsun'
        if self is Month.Eleint:
            return 'The Fading'
        if self is Month.Marpenoth:
            return 'Leaffall'
        if self is Month.Uktar:
            return 'The Rotting'
        if self is Month.Nightal:
            return 'The Drawing Down'


def get_season(month, day):
    month = Month(month)
    if (month is Month.Nightal and day >= 15) or (month is Month.Hammer) or (month is Month.Alturiak) or (
            month is Month.Ches and day <= 14):
        return SeasonEnum.WINTER
    if (month is Month.Ches and day >= 15) or month is Month.Tarsakh or month is Month.Mirtul or (
            month is Month.Kythorn and day <= 14):
        return SeasonEnum.SPRING
    if (month is Month.Kythorn and day >= 15) or month is Month.Flamerule or month is Month.Eleasis or (
            month is Month.Eleint and day <= 14):
        return SeasonEnum.SUMMER
    if (month is Month.Eleint and day >= 15) or month is Month.Marpenoth or month is Month.Uktar or (
            month is Month.Nightal and day <= 14):
        return SeasonEnum.FALL


def _calculate_number_of_days(days_to_generate, years_to_generate, months_to_generate):
    return days_to_generate + (DAYS_IN_MONTH * months_to_generate) + (DAYS_IN_YEAR * years_to_generate)


def _is_next_day_holiday(month, day):
    month = Month(month)
    if day is DAYS_IN_MONTH:
        if month is Month.Hammer:
            return True, 'Midwinter'
        if month is Month.Tarsakh:
            return True, 'Greengrass'
        if month is Month.Flamerule:
            return True, 'Midsummer'
        if month is Month.Eleint:
            return True, 'Highharvestide'
        if month is Month.Uktar:
            return True, 'The Feast of the Moon'
    return False


def get_date(year, month, day):
    return {'year': year, 'month': Month(month), 'day': day, 'season': get_season(month, day)}


def get_dates(
        days_to_generate=1,
        years_to_generate=0,
        months_to_generate=0,
        starting_year=1491,
        starting_month=1,
        starting_day=1):
    total_days_to_generate = _calculate_number_of_days(days_to_generate, years_to_generate, months_to_generate)
    date_list = list()
    y = starting_year
    m = starting_month
    d = starting_day
    date_list.append(get_date(y, m, d))
    was_holiday = False
    for day in range(total_days_to_generate - 1):
        is_holiday = False
        if not was_holiday:
            is_holiday = _is_next_day_holiday(m, d)
        if is_holiday:
            date_list.append({'year': y, 'name': is_holiday[1], 'season': get_season(m, d)})
            was_holiday = True
        else:
            if d is DAYS_IN_MONTH:
                d = 1
                if m is MONTHS_IN_YEAR:
                    m = 1
                    y += 1
                else:
                    m += 1
            else:
                d += 1

            date_list.append(get_date(y, m, d))
            was_holiday = False
    return date_list
