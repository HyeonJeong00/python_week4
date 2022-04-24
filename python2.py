a = {}

a["이름"] = "김현정"
a["나이"] = "23살"
a["학번"] = "2020142017"
a["학과"] = "전기전자공학부"
a["생일"] = "20000605"

print(a)
print(len(a))
print()

del a["이름"]
del a["나이"]
del a["학번"]
del a["학과"]
del a["생일"]

print(a)
print(len(a))
print(a)

a = dict(이름 = "김현정", 나이 = "23살", 학번 = "2020142017", 학과 = "전기전자공학부", 생일 = "20000605")

print(a)
print(len(a))
print()

a.clear()
print(a)
print(len(a))