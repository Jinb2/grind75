# we have two pointers
# basically get every possible subarray contigous
# first pointer is where we start
# and second pointer is iterating through the array and checking if we can add his element to our subarray
# if asc then next iteration has to be descending
# vice versa


def countSawSubarrays(arr):

    count = 0

    for i in range(len(arr) - 1):

        asc = None

        for j in range(i + 1, len(arr)):

            if arr[j - 1] == arr[j]:
                break

            elif arr[j - 1] < arr[j]:
                if asc == None or not asc:
                    asc = True
                else:
                    break
            else:

                if asc == None or asc:
                    asc = False
                else:
                    break
            count += 1

    return count


print(countSawSubarrays([1, 2, 1, 2, 1]))
