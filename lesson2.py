names = ['АнТон','АврААм','МариЯ','МакСим']
names_A = []
names_M = []


for name in names:
    if name.lower().startswith('а'):
        names_A.append(name)
    elif name.lower().startswith('м'):
        names_M.append(name)

print(names_A)
print(names_M)