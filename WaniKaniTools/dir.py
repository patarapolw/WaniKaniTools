import os
import inspect

ROOT = os.path.dirname(os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename))


def database_path(database):
    return os.path.join(ROOT, 'database', database)
