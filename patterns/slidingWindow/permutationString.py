def find_permutation(s, pattern):

    left, matched = 0, 0

    freq = {}

    for c in pattern:
        freq[c] = 1 + freq.get(c, 0)

    for right in range(len(s)):

        c = s[right]

        if c in freq:
            freq[c] -= 1

            if freq[c] == 0:
                matched += 1

        if matched == len(pattern):
            return True

        if right > len(pattern) - 1:

            c = s[left]
            left += 1

            if c in freq:

                if freq[c] == 0:
                    matched -= 1

                freq[c] += 1

    return False


def main():
    print("Permutation exist: " + str(find_permutation("oidbcaf", "abc")))
    print("Permutation exist: " + str(find_permutation("odicf", "dc")))
    print("Permutation exist: " + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
    print("Permutation exist: " + str(find_permutation("aaacb", "abc")))


main()
