def romanToInt(s: str) -> int:
        roman_decimal = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        n = len(s)
        num = 0
        i = 0
        while i<n:
            if (i!=n-1) and (s[i:i+2] in roman_decimal):
                print(str(i)  + "   " + str(roman_decimal[s[i:i+2]]))
                num+= roman_decimal[s[i:i+2]]
                i+=2
            else:
                print(str(i)  + '   ' + str(roman_decimal[s[i]]))
                num+= roman_decimal[s[i]]
                i+=1
        return num

print(romanToInt("MCMXCIV"))