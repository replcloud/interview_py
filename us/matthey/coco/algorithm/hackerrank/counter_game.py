def counterGame(n):
    PLAYER = ['Louise', 'Richard']
    winner = 1
    if n == 1: return 'Louise'
    while n != 1:
        o = n
        c = 0
        while o != 1:
            o >>= 1
            c += 1
        o <<= c
        if n == o:
            n >>= 1
        else:
            n -= o
        winner = (winner + 1) % 2
    return PLAYER[winner]

if __name__ == '__main__':
    print(counterGame(6))