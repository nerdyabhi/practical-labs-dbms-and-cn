def calc_redundant_bits(m):
    # Use the formula 2^r >= m + r + 1 to find the number of redundant bits
    for i in range(m):
        if (2**i >= m + i + 1):
            return i

def position_redundant_bits(data, r):
    # Insert redundant bits at positions that are powers of 2
    j = 0
    k = 1
    m = len(data)
    res = ''
    for i in range(1, m + r + 1):
        if (i == 2**j):
            res = res + '0'
            j += 1
        else:
            res = res + data[-k]
            k += 1
    return res[::-1]

def calculate_parity_bits(arr, r):
    n = len(arr)
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if j & (2**i) == (2**i):
                val = val ^ int(arr[-j])
        arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:]
    return arr

def detect_error(arr, nr):
    n = len(arr)
    res = 0
    for i in range(nr):
        val = 0
        for j in range(1, n + 1):
            if j & (2**i) == (2**i):
                val = val ^ int(arr[-j])
        res = res + val*(10**i)
    return int(str(res), 2)

data = input("Enter the data to be transmitted: ")
m = len(data)
r = calc_redundant_bits(m)

arr = position_redundant_bits(data, r)
arr = calculate_parity_bits(arr, r)

print("Data transferred with redundant bits: ", arr)

# Create error in data for testing
test_arr = arr[:len(arr)-1] + str(1 - int(arr[-1]))
print("Data with error for testing: ", test_arr)

error_position = detect_error(test_arr, r)
print("Error is found at position (starting from 1): ", error_position)