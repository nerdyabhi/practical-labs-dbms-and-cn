def calcrBits(data):
    # 2 ^ r >= m + r  +1;
    for i in range(1,m):
        if(2**i >= m+i+1):
            return i

def generateParity(data , r):
    j =0
    k =1
    m = len(data)
    res =''
    for i in range(1 , m +r + 1):
        if(i== 2**j):
            res += '0'
            j= j+1
        else:
            res += data[-k]
            k= k+1
    return res[::-1]

def mainParity(arr , r):
    n = len(arr)

    for i in range(r):
        val =0
        for j in range(1 , n+1):
            if j & (2**i) == (2**i):
                val = val ^ int(arr[-j])
        pos = (2**i)
        arr = arr[:n-pos] + str(val) + arr[n-pos +1:]
    return arr



def detectError(arr , r):
    n = len(arr)
    res =0

    for i in range(r):
        val =0
        for j in range(1 , n+1):
            if j & (2**i) == (2**i):
                val = val ^ int(arr[-j])
        res = res + val * (10 ** i) # YAAD RAKHNAAA
    return int(str(res), 2)



data = input("Enter data : ");
m = len(data)
r = calcrBits(m);
arr = generateParity(data , r)
ans = mainParity(arr , r)

print("After all that , data transferred  is : " , ans)
n = len(ans)

test = ans[:n-1] + str(1 - int(ans[-1]))
print("Data with error : " , test)
post  = detectError(test , r)
print(" Error at pos " , post)

