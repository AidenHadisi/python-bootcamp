from typing import Iterator

"""
Generators create an iterator.
We can make generators using the yield keyword!

We can make iterators as an object that implements __next__ and __iter__ or we can make them using generators.
Or we can use generator comprehension.
"""


class first_n:
    """An iterator that returns the first n numbers."""

    def __init__(self, n: int) -> None:
        self.n = n
        self.cur = -1

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        self.cur += 1
        if self.cur >= self.n:
            raise StopIteration
        return self.cur


def first_n_generator(n: int) -> Iterator[int]:
    """A generator that returns the first n numbers using yield."""
    for i in range(n):
        yield i


def first_n_generator_comprehension(n: int) -> Iterator[int]:
    """A generator that returns the first n numbers using generator comprehension."""
    return (num for num in range(n))


if __name__ == "__main__":
    # Can use any func that expects an iterable
    print(sum(first_n(10)))
    print(sum(first_n_generator(10)))
    print(sum(first_n_generator_comprehension(10)))

    # can use loops
    my_gen = first_n_generator_comprehension(10)
    for i in my_gen:
        print(i)

    # can use next
    my_gen = first_n_generator_comprehension(10)
    print(next(my_gen))
    print(next(my_gen))

    # make a string an iterable
    my_string = "hello"
    my_iter = iter(my_string)
    print(tuple(my_iter))
