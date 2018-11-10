/* 
    Go through each possible way to shift it until find sensible english.
    
    Could have also initially found most common, then used this as E, but did an easy brute force since there are not that many ways to shift.
*/

ct = 'Z CVRIEVU KYV WFCCFNZEX AFBV KYV CRJK KZDV Z NFIBVU R IVRC AFS. NYRK UZU KYV WZJY JRP NYVE YV YZK YZJ YVRU? URD'

for i in range(26):
    pt= ''
    for ch in ct:
        if ord(ch) > 90 or ord(ch) < 65:
            pt += ch
        else:
            if ord(ch) + i > 90:
                pt += chr(ord(ch) + i - 26)
            else:
                pt += chr(ord(ch) + i)
    print(i)
    print(pt)
