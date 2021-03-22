prime_table = [False, False, True]
prime_count = [0, 0, 1]


def sillyGame(n):
    def fill_prime_table(n):
        global prime_table

    global prime_count
    start = len(prime_table)
    prime_table += [True] * (n + 1 - start)
    for i in range(2, int(n ** 0.5) + 1):
        prime_table[i * 2:n + 1:i] = [False] * ((n - i) // i)
    for j in range(len(prime_count), len(prime_table)):
        prime_count += (prime_count[-1] + 1) if prime_table[j] else prime_count[-1],


    PLAYERS = ['Bob', 'Alice']
    fill_prime_table(n)
    return PLAYERS[prime_count[n] % 2]

if __name__ == '__main__':
    l = [1, 2, 5]
    # l = [5]
    for x in l:
        print(sillyGame(x))
