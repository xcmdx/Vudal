import argparse
def fib(n):
    if n == 1 or n == 2:
        num = 1
        return num
    if n > 2:
        num = fib(n - 1) + fib(n - 2)
        return num
parser = argparse.ArgumentParser()
parser.add_argument('n', type=int)
args = parser.parse_args()
print(fib(args.n))