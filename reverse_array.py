#hhh
def reverse_array(ar):
    l = len(ar)
    for i in xrange(l//2):
        k = l-1-i
        ar[i], ar[k] = ar[k], ar[i]

    print ar

ar = [1,2,3,4,5,6,7,8]
reverse_array(ar)