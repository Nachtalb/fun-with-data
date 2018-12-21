import os
import sys

from github3 import login

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(os.path.abspath(__file__))))
DATA_PATH = os.path.join(BASE_PATH, 'data')

GITHUB_DATA_PATH = os.path.join(DATA_PATH, 'github_data.json')


class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream

    def write(self, data):
        self.stream.write(data)
        self.stream.flush()

    def writelines(self, datas):
        self.stream.writelines(datas)
        self.stream.flush()

    def __getattr__(self, attr):
        return getattr(self.stream, attr)


# https://stackoverflow.com/a/107717/5699307
sys.stdout = Unbuffered(sys.stdout)

github = login(token=os.getenv('GITHUB_TOKEN', None))
ftw = github.organization('4teamwork')
ftw_repos = ftw.repositories()
