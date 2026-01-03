import math

def entropy(total, c1, c2, c3):
    ent = 0
    for c in [c1, c2, c3]:
        if c != 0:  # avoid log(0)
            p = c / total
            ent -= p * math.log2(p)
    return round(ent, 2)

# def gain()


print(entropy(14,4,8,2))

# print(1-((2/2)*1)-((3/8)*0.92))
# print(0.92-(2/3))