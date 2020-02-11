import os


def func_a():
    a = None
    try:
        a = os.environ["aaaaa"]
    except KeyError as e:
        raise


if __name__ == '__main__':
    try:
        func_a()
    except Exception:
        print("yeaa")
