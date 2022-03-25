def build_reverse(sequence):
    graph_r = []
    n = len(sequence)
    for i in range(n):
        graph_r.append([sequence[i]])

    for i in range(n-1, -1, -1):
        for j in range(i-1, -1, -1):
            if graph_r[i][0] > graph_r[j][0]:
                graph_r[i].append(j)
    return graph_r


def max_neighbor(G, i):
    if len(G[i])>3:
        max = G[G[i][1]][len(G[G[i][1]])-1]
        j = G[i][1]
        k = 2
        while k<len(G[i])-2:
            if max<G[G[i][k]][len(G[G[i][k]])-1]:
                max = G[G[i][k]][len(G[G[i][k]])-1]
                j = G[i][k]
            k+=1
        G[i][len(G[i])-2] = j
        return max
    else:
        return 0


def compute_LIS(G):
    
    for i in range(len(G)):
        G[i].append(-1)
        G[i].append(1)

    for i in range(len(G)):
        G[i][len(G[i])-1]+= max_neighbor(G,i)

    max = G[0][len(G[0])-1]
    start = 0
    for i in range(1, len(G)):
        if max < G[i][len(G[i])-1]:
            max = G[i][len(G[i])-1]
            start = i

    print(G[start][0])
    next = G[start][len(G[start])-2]
    while next!=-1:
       print(G[next][0])
       next = G[next][len(G[next])-2]



if __name__ == '__main__':
    seq = [int(element) for element in input().split()]
    
    compute_LIS((build_reverse(seq)))

