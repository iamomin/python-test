print('Hello World')

class Test(object):
    """
    docstring
    """
    def __init__(self):
        print('Init')
    def __del__(self):
        print('Destruct')


if __name__ == '__main__':
    Test()