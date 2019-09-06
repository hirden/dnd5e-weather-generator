import advanced_weather_generator
from harptos_calendar import get_dates
import argparse

TABLE_WIDTH = 85

def pretty_print_weathers(dates, weathers):
    print('+{}+'.format('-' * TABLE_WIDTH))
    print('|   | Date                                        | Season | Weather                  |')
    print('+{}+'.format('-' * TABLE_WIDTH))
    for date, weather in zip(dates, weathers):
        condition = weather['condition'][0].value
        season = date['season'].value
        if date.get('month') is None or date.get('day') is None:
            print('|   | {} {:<38} | {:<6} | {:<24} |'.format(date['year'], date['name'], season.name, condition))
        else:
            month = date['month']
            month_string = '{} ({})'.format(month.name, month.get_month_common_name())
            print('|   | {} {:<35} {:<2} | {:<6} | {:<24} |'.format(date['year'], month_string, date['day'], season.name, condition))
    print('+{}+'.format('-' * TABLE_WIDTH))
    print('Last counter value: {}'.format(weather['counter']))

    advanced_weather_generator.print_weather_condition_info()


def main():

    parser = argparse.ArgumentParser(description='Generate a list of dates and weathers for DND 5e')
    parser.add_argument('-y', nargs='?', default='1491', help='Starting year')
    parser.add_argument('-m', nargs='?', default='1', help='Starting month')
    parser.add_argument('-d', nargs='?', default='1', help='Starting day')
    parser.add_argument('-c',
                        nargs='?',
                        help='Provide an initial counter for weather generation',
                        choices=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'],
                        default=None)
    parser.add_argument('-n', nargs='?', default=7, help='Number of days to generate for')
    parser.add_argument('--num-months', nargs='?', default=0, help='Number of months to generate for')
    parser.add_argument('--num-years', nargs='?', default=0, help='Number of years to generate for')

    args = parser.parse_args()
    y = int(args.y)
    m = int(args.m)
    d = int(args.d)
    if args.c:
        counter = int(args.c)
    else:
        counter = args.c
    days_to_generate = int(args.n)
    months_to_generate = int(args.num_months)
    years_to_generate = int(args.num_years)

    dates = get_dates(
        days_to_generate=days_to_generate,
        months_to_generate=months_to_generate,
        years_to_generate=years_to_generate,
        starting_year=y,
        starting_month=m,
        starting_day=d)
    weathers = list()
    for date in dates:
        weather = advanced_weather_generator.generate_weather(date['season'], counter)
        counter = weather['counter']
        weathers.append(weather)
    # Do stuff
    # advanced_weather_generator.pretty_print_weather_list(weathers)
    pretty_print_weathers(dates, weathers)


main()
