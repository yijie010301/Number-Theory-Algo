import math


def gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


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

def pollard(p):
    i = 2
    while True:
        temp = fast_power(2, math.factorial(i), p) - 1
        c = gcd(temp, p)
        if c == 1:
            i += 1
            continue
        else:
            print("temp: ", temp)
            print("current factorial: ", i)
            print("common factor: ", c)
            break
    return


# For small primes.
def isPrime(n):
    for i in range (2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    print("2(a):")
    pollard(1739)
    print("\n")
    print("2(b):")
    pollard(220459)
    #print(isPrime(449))
    #print(isPrime(491))
    print("\n")
    print("2(c):")
    pollard(48356747)
    #print(isPrime(6917))
    print(isPrime(233))
    print(isPrime(229))

