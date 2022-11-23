def calc_nth():
    n = int(input("Enter N: "))
    #nth_square = n + sum(2*i for i in range(0, n))
    nth_square = n + n*(n-1)
    #for i in range(0, n):
        #nth_square += 2 * i
    print(f'The {n}th square number is: {nth_square}')

def main():
    while(True):
        calc_nth()


if __name__ == "__main__":
    main()

