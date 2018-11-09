import os


THIS_DIR = os.path.realpath(os.path.dirname(__file__))


def bar():
    top = os.path.realpath(os.path.join(THIS_DIR))
    return os.path.normpath(os.path.join(top))
