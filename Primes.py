import time
import math


def SieveOfAtkin(limit):
    # 2 and 3 are known
    # to be prime

    # Initialise the sieve
    # array with False values
    sieve = [False] * (limit + 1)

    '''Mark sieve[n] is True if
    one of the following is True:
    a) n = (4*x*x)+(y*y) has odd
    number of solutions, i.e.,
    there exist odd number of
    distinct pairs (x, y) that
    satisfy the equation and
    n % 12 = 1 or n % 12 = 5.
    b) n = (3*x*x)+(y*y) has
    odd number of solutions
    and n % 12 = 7
    c) n = (3*x*x)-(y*y) has
    odd number of solutions,
    x > y and n % 12 = 11 '''
    x = 1
    while x * x <= limit:
        y = 1
        while y * y <= limit:

            # Main part of
            # Sieve of Atkin
            n = (4 * x * x) + (y * y)
            if (n <= limit and (n % 12 == 1 or
                                n % 12 == 5)):
                sieve[n] ^= True

            n = (3 * x * x) + (y * y)
            if n <= limit and n % 12 == 7:
                sieve[n] ^= True

            n = (3 * x * x) - (y * y)
            if (x > y and n <= limit and
                    n % 12 == 11):
                sieve[n] ^= True
            y += 1
        x += 1

    # Mark all multiples of
    # squares as non-prime
    r = 5
    while r * r <= limit:
        if sieve[r]:
            for i in range(r * r, limit + 1, r * r):
                sieve[i] = False

        r += 1

        # Print primes
    # using sieve[]
    return [2, 3] + list(map(lambda x: x[0] + 5, filter(lambda x: x[1], enumerate(sieve[5:]))))


def primes_up_to_n(n):
    if n < 3:
        return n + 1
    elif n == 3:
        return 5
    elif n == 4:
        return 7
    elif n == 5:
        return 11
    # List of primes excluding 2 and 5 (to check for factors)
    # - Every number is divisible by 1
    # - We only check odd numbers, so no need to check if divisible by 2
    # - Don't need to check if divisible by 5
    primes = [0] * (n - 2)
    primes[:4] = [3, 7, 11, 13]
    i = 17
    index = 4
    while True:
        for _ in range(4):
            p_limit = math.sqrt(i)
            for p in primes:
                # Don't need to check if number is divisible by anything more than i^1/2
                # - We know anything i^1/2 or less isn't a factor of i
                if p > p_limit:
                    primes[index] = i
                    index += 1
                    break
                if (i / p).is_integer():
                    break
            i += 2
            if i >= n:
                return [2,3,5] + primes[1:index]
        # When about to check a number ending in 5, add 2 (skip it)
        i += 2


def nth_prime_quick(n):
    if n < 3:
        return n + 1
    elif n == 3:
        return 5
    elif n == 4:
        return 7
    elif n == 5:
        return 11
    # List of primes excluding 2 and 5 (to check for factors)
    # - Every number is divisible by 1
    # - We only check odd numbers, so no need to check if divisible by 2
    # - Don't need to check if divisible by 5
    primes = [0] * (n - 2)
    primes[:4] = [3, 7, 11, 13]
    i = 17
    index = 4
    k = n - 2
    while True:
        for _ in range(4):
            p_limit = math.sqrt(i)
            for p in primes:
                # Don't need to check if number is divisible by anything more than i^1/2
                # - We know anything i^1/2 or less isn't a factor of i
                if p > p_limit:
                    primes[index] = i
                    index += 1
                    if index == k:
                        return i
                    break
                if (i / p).is_integer():
                    break
            i += 2
        # When about to check a number ending in 5, add 2 (skip it)
        i += 2


class LinkedList:
    class Node:
        def __init__(self, value, next = None):
            self.value = value
            self.next: LinkedList.Node = next

    def __init__(self, list):
        self.head = LinkedList.Node(list[0])
        prev = self.head
        for e in list[1:]:
            new_node = LinkedList.Node(e)
            prev.next = new_node
            prev = new_node
        self.tail = prev
        self.length = len(list)
        self.current: LinkedList.Node = self.head

    def append(self, value):
        self.tail.next = LinkedList.Node(value)
        self.tail = self.tail.next
        self.length += 1

    def __len__(self):
        return self.length

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            self.current = self.head
            raise StopIteration
        else:
            node = self.current
            self.current = self.current.next
            return node


def nth_prime_linked_list(n):
    if n < 3:
        return n + 1
    elif n == 3:
        return 5
    elif n == 4:
        return 7
    elif n == 5:
        return 11
    # List of primes excluding 1 and 2 (to check for factors)
    # - Every number is divisible by 1
    # - We only check odd numbers, so no need to check if divisible by 2

    primes = LinkedList([3, 7, 11, 13])
    i = 17

    def check(x):
        p_limit = math.sqrt(i)
        for n in primes:  # (n/6)!
            # Don't need to check if number is divisible by anything more than i^1/2
            # - We know anything i^1/2 or less isn't a factor of i
            if n.value > p_limit:
                primes.append(i)
                break
            if (i / n.value).is_integer():
                break
    counter = 0
    while len(primes) < n - 2: # n
        # Check next number ending in 7
        check(i)
        if counter == 3:
            i += 4
            counter = 0
        else:
            i += 2
            counter += 1
    return primes.tail.value


def main():
    while True:
        n = int(input("Enter a number (nth prime): "))
        start = time.time()
        prime = nth_prime_quick(n)
        seconds = time.time() - start

        print(f'The {n}th prime is: {prime} (in {seconds} seconds)')

        n = int(input("Enter a number (primes up to n): "))
        start = time.time()
        prime = primes_up_to_n(n)
        seconds = time.time() - start
        print(f'The primes up to {n}: {prime}\n (in {seconds} seconds) (Homemade)')
        start = time.time()
        prime = SieveOfAtkin(n)
        seconds = time.time() - start

        print(f'The primes up to {n}: {prime}\n (in {seconds} seconds) (Sieve)')


if __name__ == "__main__":
    main()

