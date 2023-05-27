def checkio(words_set):
    longest = ""
    for word in words_set:
        if len(word) > len(longest):
            longest = word
    words_set.remove(longest)
    # print(words_set)

    for letterW in words_set:
        # print('lW>> ', letterW)
        # print('len>> ', len(letterW))
        # print(longest[len(longest)-len(letterW):])
        if letterW == longest[len(longest) - len(letterW) :]:
            return True
        # for letterL in longest:
        # if letterW == letterL:
        # condition = True
        # else:
        # condition = False
    # return condition
    return False


# These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     assert checkio({"hello", "lo", "he"}) == True, "helLO"
#     assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
#     assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
#     assert checkio({"one"}) == False, "Only One"
#     assert checkio({"helicopter", "li", "he"}) == False, "Only end"

print(checkio({"aa", "a"}))
