# Road to Coop : Path to Greatness
import  datetime

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


def print_all_awards(awards):
    print("{:<8} {:<15} {:<10} {:<10} {:<10}".format('date', 'award_name', 'rank', 'first_name', 'last_name'))
    for award in awards:
        print("{:<8} {:<15} {:<10} {:<10} {:<10}".format(award['date'].strftime("%x"), award['award_name'], award['rank'], award['first_name'], award['last_name']))

def print_by_year(awards, year):
    pass

if __name__ == '__main__':
    awards = read_data("award.txt")
    print_all_awards(awards)