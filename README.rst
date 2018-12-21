Fun with data
=============

Fun with data is a small project, in which I collect data and make graphs and so on. Nothing special, really.


1. Install the requirements ``pip install -r requirements.txt``
2. Create a GitHub Token and add it to your env variables as ``GITHUB_TOKEN``.
3. Then run the ``fun/get_data.py`` script to get a JSON file with all repos and it's pull requests of the 4teamwork organization. This will take some time.
4. Now you can use ``fun/graph_data.py`` to create some graphs.
