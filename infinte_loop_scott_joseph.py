class InfiniteIter:

    def __init__(self):
        self.x = 0


    def __iter__(self):
        return self


    def __next__(self):
        x = self.x
        self.x += 1
        return x


def BreakStuff():
    infinite = InfiniteIter()
    for item in infinite:
        print(item)


BreakStuff()
