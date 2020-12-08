class PrimitiveType:
    def countBits(self, x):
        numBits = 0
        while x != 0:
            numBits += x & 1
            x >>= 1
        return numBits


if __name__ == '__main__':
    print(PrimitiveType().countBits(4))