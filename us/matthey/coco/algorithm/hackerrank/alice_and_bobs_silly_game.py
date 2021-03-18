prime_table = [False, False, True]


def sillyGame(n):
    def fill_prime_table(n):
        global prime_table
        start = len(prime_table)
        prime_table += [True] * (n + 1 - start)
        i_prime = 2
        while i_prime <= n:
            i = max((start // i_prime + 1) * i_prime, 2 * i_prime)
            while i <= n:
                prime_table[i] = False
                i += i_prime
            i_prime += 1
            while i_prime <= n and not prime_table[i_prime]:
                i_prime += 1

    PLAYERS = ['Bob', 'Alice']
    fill_prime_table(n)
    # print('prime_table', prime_table)
    # print('prime_table short', prime_table[:n + 1])
    return PLAYERS[prime_table[:n + 1].count(True) % 2]


if __name__ == '__main__':
    l = [1, 2, 5]
    # l = [5]
    for x in l:
        print(sillyGame(x))
