import os

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

from fun import DATA_PATH
from fun.parse_data import merge_duration_over_time
from fun.parse_data import open_pr_per_person
from fun.utils import rgba

ftw_colour = rgba(19, 179, 236)


def graph_open_prs_per_day():
    plt.figure(num=None, figsize=(10, 6), dpi=221, facecolor='w', edgecolor='k')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %y'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=6))

    merge_duration = merge_duration_over_time()
    good_data = zip(*[(date, len(items)) for date, items in merge_duration])

    plt.plot(*good_data, color=ftw_colour)
    plt.gcf().autofmt_xdate()

    plt.xlabel('Dates')
    plt.ylabel('Open PRs')
    plt.title("Open PRs per day")
    plt.savefig(os.path.join(DATA_PATH, 'graph_open_prs_per_day.png'), bbox_inches='tight')
    plt.show()


def graph_open_pr_per_person():
    plt.figure(num=None, figsize=(10, 6), dpi=221, facecolor='w', edgecolor='k')

    people_open_prs = open_pr_per_person()
    usernames, open_prs = list(zip(*people_open_prs))

    plt.bar(usernames, open_prs, color=ftw_colour)

    plt.xticks(rotation=70)

    plt.xlabel('People')
    plt.ylabel('Open PRs')
    plt.title("Open PRs per person")
    plt.savefig(os.path.join(DATA_PATH, 'open_pr_per_person.png'), bbox_inches='tight')
    plt.show()


graph_open_prs_per_day()
graph_open_pr_per_person()
