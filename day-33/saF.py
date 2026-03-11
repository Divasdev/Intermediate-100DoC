def all_common(strings):
    # start with characters from the first string
    common_chars = set(strings[0])

    # intersect with characters from the remaining strings
    for s in strings[1:]:
        common_chars = common_chars.intersection(set(s))

    # return characters in ascending order as a string
    return "".join(sorted(common_chars))




all_common([
    "abcde",
    "bcdef",
    "cdefg",
])

