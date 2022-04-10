import math
from sympy import mod_inverse

# Find the a^(b) mod n.
def fast_power(a, b, n):
    # list for the number mod n with a^(2^p)
    list = []
    result = 1

    # Covert to binary.
    binNum = bin(b);
    strBin = binNum + ""
    strLen = len(binNum + "")

    c = math.pow(a, math.pow(2, 0)) % n
    #print(c)
    # Store the value.
    for i in range(0, strLen - 2):
        list.append(c)
        c = c * c % n
    count = 0;
    #print(list)

    # Calculate the value.
    for i in range(strLen - 1, 1, -1):
        if int(strBin[i]) == 1:
            result = result * list[count] % n
            #print(list[count])
        count = count + 1;
    return result % n


# Main for some test.
if __name__ == '__main__':
    ##print("Part a: ")
    #print(fast_power(892383, 103, 2038667))
    #print('\n')
    #print("Part c: ")
    #print(fast_power(317730, 810367, 2038667))
    #print(fast_power(2, 29725377, 118901509))
    #print(fast_power(2, 120, 1739))
    print(fast_power(17, 3030, 19079))
    print(fast_power(17, 6892, 19079))
    print(fast_power(17, 18312, 19079))
    print(mod_inverse(17, 19079))
    print(fast_power(11223, 12400, 19079))
    
