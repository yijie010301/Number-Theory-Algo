import math


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

    # Store the value.
    for i in range(0, strLen - 2):
        list.append(c)
        c = c * c % n
    count = 0;

    # Calculate the value.
    for i in range(strLen - 1, 1, -1):
        if int(strBin[i]) == 1:
            result = result * list[count] % n
        count = count + 1;
    return result % n

def miller(p):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    copyp = p
    p = p - 1
    count = 0
    while (p % 2 == 0):
        p = p / 2
        count += 1
    print(count)
    for prime in primes:
        for i in range(0, count):
            print("witness is: ", prime)
            print("power is: ",  int((2**i)*p))
            print("result is: ", fast_power(prime, int((2**i)*p), copyp));


# Main for some test.
if __name__ == '__main__':
    miller(118901509)
    print(fast_power(2, 59450754, 118901509))