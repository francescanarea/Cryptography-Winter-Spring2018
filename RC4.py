
#output is an array of length x w/ binary representation of y
def SubRoutineA(x,y):
    bin=[None] * x
    #backwards loop, goes from x-1 --> 0: range(start,end+1,increment)
    for i in range(x-1, -1,-1): 
        r = y%2
        y = int(y/2)
        bin[i] = r
        
    return bin

#output decimal representation of arr
def SubRoutineB(bin):
    #if given an array with any non-zero length
    if len(bin) > 0:
        dec = 0 #if non-zero, lowest will be 0 since interpreting unsigned
        #backwards loop, goes from len(bin)-1 --> 0: range(start,end+1,increment)
        for i in range(len(bin)-1,-1,-1):
            #dec += array value * 2^(len-1-i) b/c power is opposite of array index
            dec += bin[i]*(2**(len(bin)-1-i)) 
        return dec
    #if given a zero length array, will return -1
    return -1

#takes in a key, n and l
#returns array of RC4 keystream
def RC4(n,l, key):
    #initialization of arrays to their respective sizes
    ks = [None]*(2**n)
    s=[None]*(2**n)
    j = 0

    #expanding the key
    #getting the KS values based on the n-bit encoding
    ksI = 0
    for i in range(0,len(key), n):
        ks[ksI] = (SubRoutineB(key[i:i+n]))
        ksI += 1
    #telling the KS to wrap around if the pt length > generated key values
    if len(key)/n < len(ks):
        wrapStart = ksI
        for i in range(ksI, len(ks)):
            ks[i] = ks[i-wrapStart]

   #fills s 0-2^n-1
    for i in range(2**n):
        s[i] = i

    for i in range(2**(n)):
        j = (j+s[i]+ks[i])%(2**n)
        #swap s[i] and s[j]
        a = s[i]
        s[i] = s[j]
        s[j] = a
    i=0
    j=0

    #generating the keystream
    stream = [None]*l
    for r in range(l):
        i = (r+1)%(2**n) 
        j = (j + s[i])%(2**n)
        #swap s[i] and s[j]
        a = s[i]
        s[i] = s[j]
        s[j] = a
        t = (s[i]+s[j])%(2**n)        
        stream[r] = s[t]
    #turn stream into binary, + convert 2d array --> 1d
    streamBin = [None]*len(stream)*n
    binI = 0
    for i in range(len(stream)):
        stream[i] = SubRoutineA(n,stream[i])
        for j in range(len(stream[i])):
            streamBin[binI] = stream[i][j]
            binI += 1
    
    return streamBin

#returns pt
def runRC4(n,l,key,ct):
    
    ks = RC4(n,l,key)
    #print(len(ks))
    
    pt = [None]*len(ct)
    #print(len(pt))
    for i in range(len(ct)):
        pt[i] = (ct[i]+ks[i])%2
    print(''.join(map(str, pt))) 

    #convert given PT in EScrypto
    
#TEST1
runRC4(3, 11,[1,1,0,1,1,1,0,0,0,0,1,1,0,0,1,0,1,1], [1,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1,0])

#TEST2
test2key=[1, 0, 1, 1, 1, 0, 0, 1 , 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1]
test2ct = [1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0]
runRC4(8, 28, test2key, test2ct)

