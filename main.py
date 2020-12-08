# Road to Coop : Path to Greatness
import datetime


def read_data(filepath):
    f = open("award.txt", "r")

    awards = []

    lines = f.readlines()
    for line in lines:

        if line == "":
            break

        line = line.split()
        award = {}

        date = line[0].split('-')

        award['date'] = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
        award['award_name'] = line[1]
        award['rank'] = line[2]
        award['first_name'] = line[3]
        award['last_name'] = line[4]

        awards.append(award)

    f.close()

    return awards


def write_data(filepath, awards):
    f = open(filepath, "w")

    newtext = ""

    for award in awards:
        date = award["date"].strftime("%Y-%m-%d")
        award_name = award["award_name"]
        rank = award["rank"]
        first_name = award["first_name"]
        last_name = award["last_name"]
        line = "{} {} {} {} {}".format(date, award_name, rank, first_name, last_name)

        newtext =  newtext + line + "\n"

    f.write(newtext)

    f.close()


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


def add_award(awards, date, award_name, rank, first_name, last_name):

    award = {}
    award["date"] = datetime.datetime.strptime(date, "%Y-%m-%d")
    award["award_name"] = award_name
    award["rank"] = rank
    award["first_name"] = first_name
    award["last_name"] = last_name

    awards.append(award)


if __name__ == '__main__':
    awards = read_data("award.txt")
    add_award(awards, "2017-12-08", "MOTO", "1", "Moto", "Rola")
    write_data("award.txt", awards)
