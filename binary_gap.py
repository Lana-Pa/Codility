#binary gap exs

def solution(N):
    b_num = bin(N)[2:]
    print b_num
    gap = False
    maxgap = 0
    
    for i in range(len(b_num)-1):
        # start of the gap if current element is 0 and prev element is 1
        if b_num[i]=='1' and b_num[i+1]=='0':
            gap = True
            count = 0
        # stop of the gap, if current element is 1 and prev element is 0
        elif b_num[i]=='0' and b_num[i+1]=='1':
            gap = False
        
        # in the gap, count current element(i+1), if it's zero
        if b_num[i+1]=='0' and i+1<>len(b_num)-1:
            count+=1
            # find max
            if count>maxgap:
                maxgap=count

    print "maxpgap:", maxgap

solution(20)