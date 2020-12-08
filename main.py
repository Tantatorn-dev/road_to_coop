# Road to Coop : Path to Greatness
import datetime


def read_data(filepath):
    f = open("award.txt", "r")

    awards = []

    lines = f.readlines()
    for line in lines:
        line = line.split()
        award = {}

        date = line[0].split('-')

        award['date'] = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
        award['award_name'] = line[1]
        award['rank'] = line[2]
        award['first_name'] = line[3]
        award['last_name'] = line[4]

        awards.append(award)

    return awards


def print_awards(awards):
    print("{:<8} {:<15} {:<10} {:<10} {:<10}".format('date', 'award_name', 'rank', 'first_name', 'last_name'))
    for award in awards:
        print("{:<8} {:<15} {:<10} {:<10} {:<10}".format(award['date'].strftime("%x"), award['award_name'], award['rank'], award['first_name'], award['last_name']))


def print_by_year(awards, year):

    temp = []
    for award in awards:
        if award["date"].strftime("%Y") == year:
            temp.append(award)

    print_awards(temp)


def print_from_year_to_year(awards, start_year, end_year):

    temp = []
    for award in awards:
        current_year = int(award['date'].strftime("%Y"))
        if current_year>=start_year and current_year<=end_year:
            temp.append(award)

    temp = sort_by_date(temp)
    print_awards(temp)


def sort_by_date(awards):
    awards = sorted(awards, key=lambda k: k['date'], reverse=False)
    return awards


if __name__ == '__main__':
    awards = read_data("award.txt")
    print_from_year_to_year(awards, 2015, 2018)
