#!/usr/bin/env python3

"""Routines for solving a linear system of equations."""
import numpy as np

def gaussian_eliminate(aa, bb):
    """Solves a linear system of equations (Ax = b) by Gauss-elimination

    Args:
        aa: Matrix with the coefficients. Shape: (n, n).
        bb: Right hand side of the equation. Shape: (n,)

    Returns:
        Vector xx with the solution of the linear equation or None
        if the equations are linearly dependent.
    """

    nn = aa.shape[0] #nn is the number of equations given

    bb.shape = (nn, 1) #bb transpose

    cc = np.hstack([aa, bb]) #merge the matrices

    #print(cc)



    ii = 0 #iterating index
    for ii in range(0, nn):         #great for-loop

        if cc[ii, ii] == 0: #if diagonalelement is zero switch the row with the next row that isn't zero
            if ii < nn-1:
                jj = ii+1
                while cc[jj, ii] is None:
                    if jj <= nn-1:
                        jj = jj+1
                    else:
                    #print('The LEQ is not solvable') #if there is none, the LEQ isn't solvable
                        return None
                else:
                    cc[[ii, jj], :] = cc[[jj, ii], :]
            else:
                return None
        else:
            #print(cc)
            pass

        #print(cc)

        cc[ii, :] = cc[ii, :] / cc[ii, ii] #make diagonalelement 1

        #print(cc)


        #eliminate rest of the i-column
        for jj in range(0, nn):
            if jj == ii:
                continue
            else:
                cc[jj, :] = cc[jj, :] - cc[ii, :] * cc[jj, ii]

     #print(cc)

    xx = cc[:, nn]
    #print('The solution of the LES is:')
    #print(xx)

    return xx

aa = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
bb = np.array([1.0, 2.0, 3.0])

xx = gaussian_eliminate(aa, bb)
print(xx)