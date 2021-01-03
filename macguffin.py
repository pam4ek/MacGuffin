def split_data(data):  # 64 bit to 4 x 16 bit
    mask0 = "1"*16+"0"*48
    num0 = data & int(mask0, 2)
    num0 = num0 >> 48
    mask1 = "0"*16 + "1"*16 + "0"*32
    num1 = data & int(mask1, 2)
    num1 = num1 >> 32
    mask2 = "0"*32 + "1"*16 + "0"*16
    num2 = data & int(mask2, 2)
    num2 = num2 >> 16
    mask3 = "0"*48 + "1"*16
    num3 = data & int(mask3, 2)
    return num0, num1, num2, num3
    
    
def permutation(num1, num2, num3):
    #tempArray6bit = split_3_to_8(num1, num2, num3)
    tempArray6bit = get_perm_ind(num1, num2, num3)
    tempArray2bit = change_6_to_2_bit(tempArray6bit)
    result = union(tempArray2bit)
    return result
    
    
def get_perm_ind(num1, num2, num3):
    n1 = "{0:b}".format(num1)
    n1 = to16bit(n1)
    n1 = n1[::-1]
    n2 = "{0:b}".format(num2)
    n2 = to16bit(n2)
    n2 = n2[::-1]
    n3 = "{0:b}".format(num3)
    n3 = to16bit(n3)
    n3 = n3[::-1]
    sbox = []
    sbox.append(int(n3[13] + n3[11] + n2[9] + n2[6] + n1[5] + n1[2], 2))
    sbox.append(int(n3[14] + n3[8] + n2[10] + n2[7] + n1[4] + n1[1],2))
    sbox.append(int(n3[15] + n3[0] + n2[13] + n2[8] + n1[6] + n1[3],2))
    sbox.append(int(n3[10] + n3[4] + n2[2] + n2[1] + n1[14] + n1[12],2))
    sbox.append(int(n3[12] + n3[6] + n2[14] + n2[3] + n1[10] + n1[0],2))
    sbox.append(int(n3[5] + n3[1] + n2[15] + n2[12] + n1[8] + n1[7],2))
    sbox.append(int(n3[7] + n3[2] + n2[11] + n2[5] + n1[15] + n1[9],2))
    sbox.append(int(n3[9] + n3[3] + n2[4] + n2[0] + n1[13] + n1[11],2))
    return sbox

def to16bit(snum):
    while len(snum)!=16:
        snum = "0"+snum
    return snum
    
    
def change_6_to_2_bit(array):
    tempArray = []
    for i in range(8):
        tempArray.append(s(i,array[i]))
    return tempArray

def s(i, n): ### s(i, n)
    table = [
        [2, 0, 0, 3, 3, 1, 1, 0, 0, 2, 3, 0, 3, 3, 2, 1, 1, 2, 2, 0, 0, 2, 2, 3, 1, 3, 3, 1, 0, 1, 1, 2,
0, 3, 1, 2, 2, 2, 2, 0, 3, 0, 0, 3, 0, 1, 3, 1, 3, 1, 2, 3, 3, 1, 1, 2, 1, 2, 2, 0, 1, 0, 0, 3],
    [3, 1, 1, 3, 2, 0, 2, 1, 0, 3, 3, 0, 1, 2, 0, 2, 3, 2, 1, 0, 0, 1, 3, 2, 2, 0, 0, 3, 1, 3, 2, 1,
0, 3, 2, 2, 1, 2, 3, 1, 2, 1, 0, 3, 3, 0, 1, 0, 1, 3, 2, 0, 2, 1, 0, 2, 3, 0, 1, 1, 0, 2, 3, 3],
    [2, 3, 0, 1, 3, 0, 2, 3, 0, 1, 1, 0, 3, 0, 1, 2, 1, 0, 3, 2, 2, 1, 1, 2, 3, 2, 0, 3, 0, 3, 2, 1,
3, 1, 0, 2, 0, 3, 3, 0, 2, 0, 3, 3, 1, 2, 0, 1, 3, 0, 1, 3, 0, 2, 2, 1, 1, 3, 2, 1, 2, 0, 1, 2],
    [1, 3, 3, 2, 2, 3, 1, 1, 0, 0, 0, 3, 3, 0, 2, 1, 1, 0, 0, 1, 2, 0, 1, 2, 3, 1, 2, 2, 0, 2, 3, 3,
2, 1, 0, 3, 3, 0, 0, 0, 2, 2, 3, 1, 1, 3, 3, 2, 3, 3, 1, 0, 1, 1, 2, 3, 1, 2, 0, 1, 2, 0, 0, 2],
    [0, 2, 2, 3, 0, 0, 1, 2, 1, 0, 2, 1, 3, 3, 0, 1, 2, 1, 1, 0, 1, 3, 3, 2, 3, 1, 0, 3, 2, 2, 3, 0,
0, 3, 0, 2, 1, 2, 3, 1, 2, 1, 3, 2, 1, 0, 2, 3, 3, 0, 3, 3, 2, 0, 1, 3, 0, 2, 1, 0, 0, 1, 2, 1],
    [2, 2, 1, 3, 2, 0, 3, 0, 3, 1, 0, 2, 0, 3, 2, 1, 0, 0, 3, 1, 1, 3, 0, 2, 2, 0, 1, 3, 1, 1, 3, 2,
3, 0, 2, 1, 3, 0, 1, 2, 0, 3, 2, 1, 2, 3, 1, 2, 1, 3, 0, 2, 0, 1, 2, 1, 1, 0, 3, 0, 3, 2, 0, 3],
    [0, 3, 3, 0, 0, 3, 2, 1, 3, 0, 0, 3, 2, 1, 3, 2, 1, 2, 2, 1, 3, 1, 1, 2, 1, 0, 2, 3, 0, 2, 1, 0,
1, 0, 0, 3, 3, 3, 3, 2, 2, 1, 1, 0, 1, 2, 2, 1, 2, 3, 3, 1, 0, 0, 2, 3, 0, 2, 1, 0, 3, 1, 0, 2],
    [3, 1, 0, 3, 2, 3, 0, 2, 0, 2, 3, 1, 3, 1, 1, 0, 2, 2, 3, 1, 1, 0, 2, 3, 1, 0, 0, 2, 2, 3, 1, 0,
1, 0, 3, 1, 0, 2, 1, 1, 3, 0, 2, 2, 2, 2, 0, 3, 0, 3, 0, 2, 2, 3, 3, 0, 3, 1, 1, 1, 1, 0, 2, 3]]
    return table[i][n]


def union(array):
    num0 = ""
    for i in range(8):
        tmp = "{0:b}".format(array[i])
        if len(tmp) < 2:
            tmp = "0"+tmp
        tmp = tmp[::-1]
        num0 = tmp+num0
    return int(num0, 2)
    
    
def lap(data, key):
    num0, num1, num2, num3 = split_data(data)
    #print('left = ', num0)
    #print('a = ', num1)
    #print('b = ', num2)
    #print('c = ', num3)
    tmp1 = num1 ^ key[0]
    tmp2 = num2 ^ key[1]
    tmp3 = num3 ^ key[2]
    #print('a ^ key[0]', tmp1)
    #print('b ^ key[1]', tmp2)
    #print('c ^ key[2]', tmp3)
    tmp = permutation(tmp1, tmp2, tmp3)
    #print("tmp = ", tmp)
    num0 = num0 ^ tmp
    #print("left ^ tmp = ", num0)
    #print('swap to a, b, c, left')
    result = (num1 << 48) + (num2 << 32) + (num3 << 16) + num0
    return result



def back_lap(data, key):
    num0, num1, num2, num3 = split_data(data)
    #print('start with :')
    #print('left = ', num0)
    #print('a = ', num1)
    #print('b = ', num2)
    #print('c = ', num3)
    tmp1 = num1 ^ key[0]
    tmp2 = num2 ^ key[1]
    tmp3 = num3 ^ key[2]
    #print('a ^ key[0]', tmp1)
    #print('b ^ key[1]', tmp2)
    #print('c ^ key[2]', tmp3)
    tmp = permutation(tmp1, tmp2, tmp3)
    #print("tmp = ", tmp)
    num0 = num0 ^ tmp
    #print("left ^ tmp = ", num0)
    #result = (num3 << 48) + (num0 << 32) + (num1 << 16) + num2
    result = (num3 << 48) + (num0 << 32) + (num1 << 16) + num2
    return result

def encrypt(data, key):
    for i in range(32):
        #print(key[i])
        data = lap(data, key[i])
    return data

def decrypt(data, key):
    tempData = recombination(data)
    for i in range(31, -1, -1):
        #print(key[i])
        tempData = back_lap(tempData, key[i])
    tempData = recombination(tempData)
    tempData = recombination(tempData)
    tempData = recombination(tempData)

    return tempData


def recombination(data):
    #print('change left, a, b, c to a, b, c, left')
    num0, num1, num2, num3 = split_data(data)
    #print('left = ', num0)
    #print('a = ', num1)
    #print('b = ', num2)
    #print('c = ', num3)
    tmp = (num3 << 48)
    tmp += (num0 << 32)
    tmp += (num1 << 16)
    tmp += num2
    return tmp


def make_key(unic_key): #
    key = [[0]*3]*32
    part1 = unic_key >> 64
    part2 = unic_key - (part1 << 64)
    for i in range(32):
        part1 = encrypt(part1, key)
        left = part1 >> 48
        tmp = part1 - (left << 48)
        a = tmp >> 32
        tmp = tmp - (a << 32)
        b = tmp >> 16
        key[i] = [left, a, b]
    
    for i in range(32):
        part2 = encrypt(part2, key)
        left = part2 >> 48
        tmp = part2- (left << 48)
        a = tmp >> 32
        tmp = tmp - (a << 32)
        b = tmp >> 16
        left = key[i][0] ^ left
        a = key[i][1] ^ a
        b = key[i][2] ^ b
        key[i] = [left, a, b]
    
    return key
        
