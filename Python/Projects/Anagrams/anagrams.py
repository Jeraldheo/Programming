def are_anagrams(s1, s2):
    hash1 = dict()
    hash2 = dict()

    for letter in s1:
        if letter not in hash1:
            hash1[letter] = 1
        else:
            hash1[letter] = hash1[letter] + 1

    for letter in s2:
        if letter not in hash2:
            hash2[letter] = 1
        else:
            hash2[letter] = hash2[letter] + 1

    if hash1 == hash2:
        return 1
    else:
        return 0


s1, s2 = input().split()


print(are_anagrams(s1, s2))