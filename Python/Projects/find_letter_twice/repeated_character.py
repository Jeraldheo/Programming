def repeatedCharacter(s: str) -> str:
        seconds = []
        n  = len(s)
        for i in range(n-1):
            second = s[i+1:n].find(s[i])
            if second!=-1:
                seconds.append(second + i +1)

        return s[min(seconds)]

print(repeatedCharacter('abccbaacz'))