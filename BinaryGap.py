def solution(N):
    # code in Python 3.6
    bitstring = '{0:08b}'.format(N)
    max_gap = 0
    try:
        for i,j in enumerate(bitstring):
            if int(j) == 1:
                bitstring = bitstring[i:]
                bitstring = bitstring[::-1] #reverse
                for k,l in enumerate(bitstring):
                    if int(l) == 1:
                        bitstring = bitstring[k:]
                        lits = bitstring.split('1')
                        if len(lits)>2:
                            #print(lits)
                            max_gap = max([len(n) for n in lits])
                            break
            else:
                # Continue if the inner loop wasn't broken.
                continue
            # Inner loop was broken, break the outer.
            break
            
    except ValueError:
        print("error")
        max_gap = 0
    return max_gap