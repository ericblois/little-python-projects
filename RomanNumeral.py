def roman_num(n: int):
    roman = ''
    n_p = n
    symbols = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    for symbol in symbols.keys():
        count = int((n_p - (n_p % symbols[symbol])) / symbols[symbol])
        roman += count*symbol
        n_p -= count * symbols[symbol]
    return roman


def main():
    while True:
        n = int(input("Enter a number (up to 3999): "))
        if n > 3999:
            print(f'Number is too high!')
            continue
        print(f'The Roman numeral for {n} is: {roman_num(n)}')


if __name__ == "__main__":
    main()

