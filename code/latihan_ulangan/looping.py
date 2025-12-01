def starsTriangle(n):
    for i in range(1, n + 1):
        print('*' * i)

def starsReverseTriangle(n):
    for i in range(n, 0, -1):
        print('*' * i)

def starsPyramid(n):
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars + spaces)

def starsReversePyramid(n):
    for i in range(n, 0, -1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars + spaces)

if __name__ == "__main__":
    n = 5
    print("Stars Triangle:")
    starsTriangle(n)
    print("\nStars Reverse Triangle:")
    starsReverseTriangle(n)
    print("\nStars Pyramid:")
    starsPyramid(n)
    print("\nStars Reverse Pyramid:")
    starsReversePyramid(n)