def generate_evens():
    evens = []
    for x in range(1,50):
        if x % 2 == 0:
            evens.append(x)
    print(evens)

generate_evens()