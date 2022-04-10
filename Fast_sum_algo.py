from sympy import mod_inverse

# b is the b times point p
# c is coefficient A in the y^2 = x^3 + Ax + 1
# (x, y) is the point.
# p is the prime.
def fast_sum(x, y, p, b, c):
    listx = []
    listy = []
    binNum = bin(b);
    strBin = binNum + ""
    strLen = len(binNum + "")
    tempx = x
    tempy = y
    for i in range(0, strLen - 2):
        listx.append(tempx)
        listy.append(tempy)
        lamd = ((tempx*tempx*3 + c) * mod_inverse(2*tempy, p)) % p
        prev_x = tempx
        tempx = (lamd * lamd - tempx - tempx) % p
        tempy = (lamd * (prev_x - tempx) - tempy) % p
    count = 0
    prevx = 0
    prevy = 0
    currx = 0
    curry = 0
    flag = True;
    for i in range(strLen - 1, 1 , -1):
        if (int(strBin[i]) == 1):
            if (flag == True):
                flag = False
                prevx = listx[count]
                prevy = listy[count]
                count += 1
                continue
            currx = listx[count]
            curry = listy[count]
            l2 = ((curry - prevy) * mod_inverse((currx - prevx), p)) % p
            x3 = (l2 * l2 - prevx - currx) % p
            y3 = (l2 * (prevx - x3) - prevy) % p
            prevx = x3
            prevy = y3
        count += 1
    return prevx, prevy
    
    


if __name__ == '__main__':
    print(fast_sum(1980, 431, 2671, 1943, 171))

    print(fast_sum(2110, 543, 2671, 1943, 171))

    for i in range(1, 3000):
        x, y = fast_sum(1980, 431, 2671, i, 171)
        if (x == 2110 and y == 543):
            print(i)
            break

    print(fast_sum(1980, 431, 2671, 875, 171))

    print(fast_sum(2, 2575, 2671, 875, 171))

    print(fast_sum(2,12,26167, 1,4))

    print(fast_sum(2,12,26167, 2,4))


    print(fast_sum(2,12,26167,6,4))

    print(fast_sum(2,12,26167,24,4))

    try:
        print(fast_sum(2,12,26167,120,4))
    except Exception as e:
        print(e)


# In[12]:


    temp = 1
    for i in range (1,100):
        temp = temp * i
        try:
            fast_sum(7,4,28102844557, temp, 18)
        except Exception as e:
            print(e)
            print(i)
            break



