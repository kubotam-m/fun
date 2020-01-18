import random
v = random.random()
per = {"大吉":10, "中吉":20, "小吉":30, "吉":5, "末吉":20, "凶":50}
#per = {"大吉":10, "中吉":20, "小吉":20, "凶":50}
val = list(per.values())
key = list(per.keys())
sum = 0
for i in val:
    sum = sum + i
val = [i/sum for i in val]
sum = 0
for i in range(len(val)):
    val[i] = val[i] + sum
    sum = val[i]
print(val)
for i in range(len(val)):
    if v < val[i]:
        print(key[i])
        break

