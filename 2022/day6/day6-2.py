for stream in open("input.txt"):

    data = []
    count = 0

    for char in stream:
        count += 1
        data.append(char)
        if len(data) > 13:
            if len(set(data)) == len(data):
                break

            data.pop(0)

    print(count)
