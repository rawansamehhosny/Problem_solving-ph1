def rev_n(x):
    return int(str(x)[::-1])

num= list(map(int, input().split))
rev_num = [rev_n(n) for n in num]

print(sum(rev_num))
