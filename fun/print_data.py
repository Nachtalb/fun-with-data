import argparse
from datetime import datetime

from fun.parse_data import open_pr_per_person


def print_open_prs_per_person():
    today = datetime.now()
    for user, pulls in open_pr_per_person():
        print(f'\n{user}')
        print(f'{"":-<{len(user)}}')

        infos = []
        max_repo = 0
        max_delta = 0
        max_number = 0

        for pull in pulls:
            created = datetime.fromisoformat(pull['created_at'][:-1])
            created_string = created.strftime('%Y-%m-%d %H:%M')
            delta = today - created

            repo_name = pull['head']['repo']['name']
            number = pull['number']

            max_repo = max([max_repo, len(repo_name)])
            max_delta = max([max_delta, len(str(delta.days))])
            max_number = max([max_number, len(str(number))])

            infos.append(dict(
                repo_name=repo_name,
                delta_days=delta.days,
                created=created_string,
                number=number,
                url=pull['html_url'],
            ))

        for info in infos:
            print('PR: {repo_name: <{max_repo}} - Since {delta_days: <{max_delta}} days ({created}) - '
                  '#{number: <{max_number}} {url}'.format(
                max_delta=max_delta,
                max_repo=max_repo,
                max_number=max_number,
                **info
            ))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p1', action='store_true', help='Print open PRs by person')
    args = parser.parse_args()

    if args.p1 is not None:
        print_open_prs_per_person()
