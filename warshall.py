while True:
    n, m = list(map(int,input().split()))
    if n == 0 and m == 0:
        break
    # グラフ
    cost =  [[10000000 for i in range(m+1)] for j in range(m+1)]
    time =  [[10000000 for i in range(m+1)] for j in range(m+1)]
    for i in range(n):
        a, b, c, t = list(map(int, input().split()))
        cost[a][b] = cost[b][a] = c
        time[a][b] = time[b][a] = t

    # ワーシャルフロイド
    for k in range(m+1):
        for i in range(m+1):
            for j in range(m+1):
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
                time[i][j] = min(time[i][j], time[i][k] + time[k][j])

    # 問合わせ
    k = int(input())
    p = []
    for i in range(k):
        p = list(map(int, input().split()))
        if p[2] == 0: print(cost[p[0]][p[1]])
        else: print(time[p[0]][p[1]])
