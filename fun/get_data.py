import json

from fun import GITHUB_DATA_PATH
from fun import ftw_repos
from fun.utils import one_line_print


def get_pr_data():
    big_ass_dict = {}

    for index, repo in enumerate(ftw_repos):
        pulls = repo.pull_requests('all')

        big_ass_dict[repo.name] = repo.as_dict()
        big_ass_dict[repo.name].setdefault('pull_requests', [])

        one_line_print(f'{index + 1} - {repo.name}')
        for jindex, pull in enumerate(pulls):
            one_line_print(f'{index} - {repo.name}: {jindex + 1} #{pull.number} - {pull.title}')
            big_ass_dict[repo.name]['pull_requests'].append(pull.as_dict())

    return big_ass_dict


def save_as_json(data):
    with open(GITHUB_DATA_PATH, 'w') as json_file:
        json.dump(big_data, json_file, sort_keys=True, indent=4)
    return GITHUB_DATA_PATH


big_data = get_pr_data()
path = save_as_json(big_data)

print(f'Saved to {path}')
