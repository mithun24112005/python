def flames(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    for i in name1:
        if i in name2:
            name1 = name1.replace(i, "", 1)
            name2 = name2.replace(i, "", 1)
    count = len(name1) + len(name2)
    result = ["Friends", "Lovers", "Affectionate", "Marriage", "Enemies", "Siblings"]
    while len(result) > 1:
        split_index = (count % len(result) - 1)
        if split_index >= 0:
            right = result[split_index + 1:]
            left = result[:split_index]
            result = right + left
        else:
            result = result[:len(result) - 1]
    return result[0]

print(flames("", ""))