def process(message):

    # codesignal => cadosegnil

    # convert input into string
    messages = list(message)

    vowels = ["a", "e", "i", "o", "u"]

    prevIdx, lastVowel = None, ""

    # start from the back
    for i in range(len(messages) - 1, -1, -1):

        c = messages[i]

        # if a vowel
        if messages[i] in vowels:

            # if first vowel we encounter
            # we need to remember for the first vowel
            if not prevIdx:
                lastVowel = c
            else:
                messages[prevIdx] = c

            prevIdx = i

    # now we iterate over string and then find first vowel
    for i in range(len(messages)):
        if messages[i] in vowels:
            messages[i] = lastVowel
            break

    return "".join(messages)


print(process("codesignal"))
print(process("message"))
