with open("text", "r") as data, open("answer", "w") as answer:
    info = []
    for line in data:
        info.append(line.rstrip())
    info.reverse()
    for line in info:
        answer.write(line + "\n")
    data.close()
    answer.close()
