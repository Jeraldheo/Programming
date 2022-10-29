def findComplement(num: int) -> int:
        digits = []
        quotient = num
        while quotient>1:
            digits.append(quotient%2)
            quotient = quotient//2
        
        digits.append(quotient)
        n = len(digits)
        for i in range(n):
            if digits[i]==1:
                digits[i] = 0
            else:
                digits[i] = 1
        
        complement = 0

        for i in range(n):
            complement  += digits[i]*2**i

        return complement

print(findComplement(5))