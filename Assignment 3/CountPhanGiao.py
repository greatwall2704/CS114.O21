m, n = map(int, input().split())
online_users = list(map(int, input().split()))
friends = list(map(int, input().split()))
c = 0
i = 0
j = 0
friends = sorted(friends)
while i < len(friends) and j < len(online_users):
    if friends[i] > online_users[len(online_users)-1]:
        break
    else:
        if online_users[j] == friends[i]:
            c += 1
            i += 1
        elif online_users[j] > friends[i]:
            i += 1
        else:
            j += 1
print(c)