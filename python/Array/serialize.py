

def serialize(A):
    d = ""
    for i in A:
        m = len(i)
        d += i + str(m) + "~"
    return d


print(serialize([ "ajjuqilyyj", "yuqbodnqqk", "xeskbielhz"]))