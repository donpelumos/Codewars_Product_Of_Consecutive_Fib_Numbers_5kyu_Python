__author__ = 'Don Pelumos'
'''URL FOR THE KATA - https://www.codewars.com/kata/5541f58a944b85ce6d00006a/train/python'''
def main(prod):
    st = 0
    st2 = 1
    output = []
    for i in range(1,prod,1):
        new =st+st2
        st = st2
        st2 = new
        #print("%d--%d"%(st,st2))
        if (st*st2 == prod):
            #print("equal at %d and %d"%(st,st2))
            output.append(st)
            output.append(st2)
            output.append(True)
            break
        elif(st*st2 > prod):
            #print("greater at %d and %d"%(st,st2))
            output.append(st)
            output.append(st2)
            output.append(False)
            break
    return output
print(main(5895))
