import json
from datetime import datetime
from datetime import timedelta

from fun import GITHUB_DATA_PATH

big_ass_data = None
with open(GITHUB_DATA_PATH) as json_file:
    big_ass_data = json.load(json_file)


def pull_iterator():
    for repo in big_ass_data.values():
        for pull in repo['pull_requests']:
            yield pull


def dates_pull_request_was_not_merged(pull_request):
    merged = datetime.fromisoformat(pull_request['merged_at'][:-1])
    created = datetime.fromisoformat(pull_request['created_at'][:-1])

    delta = merged - created
    dates = []
    for index in range(delta.days):
        date_time = created + timedelta(days=index)
        dates.append(date_time.date())
    return dates


def merge_duration_over_time():
    over_time = {}

    for pull in pull_iterator():
        if not pull['merged_at']:
            continue

        for day in dates_pull_request_was_not_merged(pull):
            over_time.setdefault(day, [])
            over_time[day].append(pull)

    return sorted(over_time.items(), key=lambda item: item[0])


def open_pr_per_person():
    people = {}
    for pull in pull_iterator():
        if not pull['state'] == 'open':
            continue
        user = pull['user']['login']
        people.setdefault(user, [])
        people[user].append(pull)

    return sorted(people.items(), key=lambda item: item[0])
