def merge(*iterables):
    generator = (iter(current) for current in iterables)
    iters = list(generator)
    while iters:
        for i in iters:
            try:
                yield i.__next__()
            except StopIteration:
                iters.remove(i)


s1 = [0, 1, 2, 3]
s2 = [4, 5, 6]
s3 = [7, 8, 9, 10]

print([*(i for i in merge(s1, s2, s3))])
