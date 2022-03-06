import math


def plus_N_sqrt(n):
    i = 1
    while True:
        temp = n + i * i
        #print(temp)
        if int(math.sqrt(temp)) * int(math.sqrt(temp)) == temp:
            print("Current i: ", i)
            print("square root: ", math.sqrt(temp))
            break
        i += 1
    return
def agm_plus_N_sqrt(k, n, init):
    i = init
    while True:
        temp = k * n + i * i
        # print(temp)
        if int(math.sqrt(temp)) * int(math.sqrt(temp)) == temp:
            print("Current i: ", i)
            print("square root: ", math.sqrt(temp))
            break
        i += 1
    return

def gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a

if __name__ == '__main__':
    print("3(a)")
    plus_N_sqrt(53357)
    print("\n3(b)")
    plus_N_sqrt(34571)
    print("\n3(c)")
    plus_N_sqrt(25777)
    print("\n3(d)")
    plus_N_sqrt(64213)

    print("\n------------------------------------")
    print("4(a):")
    agm_plus_N_sqrt(247, 143041, 1)
    print(gcd(143041, 5947))
    print(gcd(143041, 5941))
    print("\n4(b):")
    agm_plus_N_sqrt(3, 1226987, 36)
    print("\n4(c):")
    agm_plus_N_sqrt(21, 2510839, 90)
    print(gcd(2510839, 7167))
    print(gcd(2510839, 7357))
    print("\n------------------------------------")
    print("5(c):")
    print(gcd(1189*2378-54000, 198103))
    print(gcd(1189 * 1605 * 2815 - 44100, 198103))
    print("\n5(d):")
    print(gcd(1591 * 4773 - 16170, 2525891))
    print(gcd(1591 * 3182 - 10780, 2525891))
    print(gcd(4773 * 3182 - 32340, 2525891))
    print(gcd(1591 * 5275 * 5401 - 17463600, 2525891))







