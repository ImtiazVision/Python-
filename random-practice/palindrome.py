def palindrome (item):
    character_in_reverse = []
    for element in reversed(range(len(item))):
        character_in_reverse.append(item[element])
    return item == "".join(character_in_reverse)
palindrome("wor")