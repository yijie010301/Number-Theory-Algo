import math
from sympy import mod_inverse


# Fast power algo from last HW.
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
    count = 0

    # Calculate the value.
    for i in range(strLen - 1, 1, -1):
        if int(strBin[i]) == 1:
            result = result * list[count] % n
        count = count + 1;
    return result % n


# factor a number and store the prime factorization into dictionary.
def factor(p):
    factors = []
    for i in range(1, p + 1):
        if p % i == 0:
            factors.append(i)
    return factors


# Find the order of g in prime p by Lagrange's theorem
# Order of g should be factor of p - 1
def findorder(g, p):
    factors = factor(p - 1)
    for i in range(len(factors)):
        if fast_power(g, factors[i], p) == 1:
            return factors[i]


# Baby list for shank's algorithm
# n is the steps, p is the prime, h = g^x.
def babyStep(n, g, p):
    babyList = []
    temp = 1
    for i in range(1, n + 1):
        babyList.append(temp)
        temp = temp * g % p
    return babyList


# Giant list for shank's algorithm
# n is the steps, p is the prime, c is the mod inverse of g, h = g^x.
def giantStep(n, p, c, h):
    giantList = []
    temp = h
    # find g^(-n) = g^((-1)*n) = c^n (mod p).
    unit = fast_power(c, n, p)
    for i in range(1, n + 1):
        giantList.append(temp)
        temp = temp * unit % p
    return giantList


# Pohlig-Hellman Algorithm.
def match(g, p, h):
    c = mod_inverse(g, p)
    order = findorder(g, p)
    n = int(math.sqrt(order)) + 1
    print("need steps: ", n)
    list1 = babyStep(n, g, p)
    print("Baby List: ", list1)
    list2 = giantStep(n, p, c, h)
    print("Giant List: ", list2)

    # find the match and calculate x.
    for i in range(len(list1)):
        for j in range(len(list2)):
            if (list1[i] == list2[j]):
                return i + j * n
    return -1

# Main for some tests
if __name__ == '__main__':
    print("Problem1 (a): x = ", match(11, 71, 21))
    print("\n")
    print("Problem1 (b): x = ", match(156, 593, 116))
    print("\n")
    print("Problem1 (c): x = ", match(650, 3571, 2213))
    print("\n")
    print("\n")
    print("Problem3 (b): order N = order(g = 10) = ", findorder(10, 746497))
    print("Problem3 (b): g1 = ", fast_power(10, 729, 746497))
    print("Problem3 (b): h1 = ", fast_power(243278, 729, 746497))
    # arguments come from g1 and h1.
    print("Problem3 (b): y1 = ", match(4168, 746497, 38277))
    print("\n")
    print("Problem3 (b): g2 = ", fast_power(10, 1024, 746497))
    print("Problem3 (b): h2 = ", fast_power(243278, 1024, 746497))
    # arguments come from g2 and h2.
    print("Problem3 (b): y2 = ", match(674719, 746497, 322735))
    print("1024y' = 158 mod 729: y' = ", mod_inverse(1024, 729) * 158 % 729)
    print("Problem3 (b) x = ", 218 * 1024 + 523)
    print("\n")
    print("\n")
    print("Problem3 (c): order N = order(g = 2) = ", findorder(2, 41022299))
    # Compute g1 h1 y1 manually since it is trivial.
    print("Problem3 (c): g2 = ", fast_power(2, 20511149, 41022299))
    print("Problem3 (c): h2 = ", fast_power(39183497, 20511149, 41022299))
    # arguments come from g2 and h2.
    print("Problem3 (c): y1 = ", match(4, 41022299, 11844727))
    print("Problem3 (c) x = ", 13192165 + math.pow(29, 5))

