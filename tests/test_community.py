import pytest
import os

import tests
from WaniKaniTools.community import Discourse


@pytest.mark.skipif('TRAVIS' in os.environ, reason='no credential specified')
def test_community():
    board = Discourse()

    id = 10
    flag = ("all", "yearly", "quarterly", "monthly", "weekly", "daily")
    username = 'polv'
    end_point = (
        'categories',  # Get a list of categories
        'c/{}'.format(id),  # Get a list of topics in the specified category
        't/{}'.format(id),  # Get a single topic
        'latest',  # Get the latest topics
        'top',  # Get the top topics
        'top/{}'.format(flag[0]),  # Get the top topics filtered by specified flag
        'post/{}'.format(id),  # Get a single post
        'users/{}'.format(username),  # Get a single user by username
        'directory_items',  # get a public list of users. Requires params: period, order
        'admin/users/list/{}'.format(flag),  # returns a list of users
        'user_actions',
        # and so on
    )

    print(board.GET('users/polv'))


if __name__ == '__main__':
    test_community()
