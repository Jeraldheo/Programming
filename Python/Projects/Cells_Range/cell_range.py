def cellsInRange(s):
        alpha = ['A', 'B', 'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        col_start = alpha.index(s[0])
        col_end = alpha.index(s[3])
        row_start = int(s[1])
        row_end = int(s[4])
        result = []
        
        for i in range(col_start, col_end + 1):
            for j in range(row_start, row_end + 1):
                result.append(alpha[i]+str(j))
        
        print(result)


s = input()
cellsInRange(s)