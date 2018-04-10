import numpy as np

aa = np.array([[2.0, 4.0, 4.0], [5.0, 4.0, 2.0], [1.0, 2.0, -1.0]])
bb = np.array([1.0, 4.0, 2.0])

nn = aa.shape[0] #nn is the number of equations given

bb.shape=(nn,1) #bb transpose

cc = np.hstack([aa, bb]) #merge the matrices

print(cc)



ii=0 #iterating index
for ii in range (0,nn):         #great for-loop

    if cc[ii,ii]==0: #if diagonalelement is zero switch the row with the next row that isn't zero
            jj = ii+1
            while cc[jj,ii] is None:
                if jj<=nn-1:
                    jj=jj+1
                else:
                    print('The LES is not solvable') #if there is none, the LEQ isn't solvable
            else:
                 cc[[ii,jj],:]=cc[[jj,ii],:]


    print(cc)

    cc[ii,:]=cc[ii,:]/cc[ii,ii] #make diagonalelement 1

    print(cc)

    #eliminate rest of the i-column
    for jj in range (0,nn):
        if jj==ii:
            continue
        else:
            cc[jj,:]=cc[jj,:]-cc[ii,:]*cc[jj,ii]

print(cc)

xx=cc[:,nn]
print('The solution of the LES is:')
print(xx)