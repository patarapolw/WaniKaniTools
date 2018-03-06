import os
import inspect

ROOT = os.path.dirname(os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename))
DATABASE = os.path.join(ROOT, 'database')

if __name__ == '__main__':
    print(ROOT)
    print(DATABASE)
