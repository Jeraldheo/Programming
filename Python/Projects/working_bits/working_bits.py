def reverseBits(n: int) -> int:
        num = list(str(n))
        size = len(num)
        decimal = 0
        for i in range(size):
            decimal+= int(num[size-1-i])*2**i
        
        return decimal

print(reverseBits(111001011110000010100101000000))