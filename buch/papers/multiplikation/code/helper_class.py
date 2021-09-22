#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 09:02:48 2021

@author: nunigan
"""

from datetime import datetime
import numpy as np

class Helper():
    def __init__(self):
        pass

    def write_c_matrix(self, n_array):
  
        with open('c_matrix.h', 'w') as file:
            file.writelines('/* Seminar Matrizen, autogenerated File, Michael Schmid, {} */ \n \n'.format(datetime.now().strftime("%d/%m/%Y, %H:%M:%S")))

            file.writelines('#include <stdint.h> \n')



            for k, n in enumerate(n_array):
                A = np.random.randint(-100,100,(n,n))
                B = np.random.randint(-100,100,(n,n))
                file.writelines('const int A{}[][{}] = \n'.format(k, n))
                file.writelines('  {\n')
                for i in range(n):
                    file.writelines('    {')
                    for j in range(n):
                        if j == n-1:
                            file.writelines('{}'.format(A[i,j]))
                        else:
                            file.writelines('{},'.format(A[i,j]))
                    if i == n-1:
                        file.writelines('}\n')
                    else:
                        file.writelines('},\n')
    
                file.writelines('  };\n')
    
                file.writelines('const int B{}[][{}] = \n'.format(k,n))
                file.writelines('  {\n')
                for i in range(n):
                    file.writelines('    {')
                    for j in range(n):
                        if j == n-1:
                            file.writelines('{}'.format(B[i,j]))
                        else:
                            file.writelines('{},'.format(B[i,j]))
                    if i == n-1:
                        file.writelines('}\n')
                    else:
                        file.writelines('},\n')
    
                file.writelines('  };\n')
    
                file.writelines('const double dB{}[][{}] = \n'.format(k,n))
                file.writelines('  {\n')
                for i in range(n):
                    file.writelines('    {')
                    for j in range(n):
                        if j == n-1:
                            file.writelines('{}'.format(B[i,j]))
                        else:
                            file.writelines('{},'.format(B[i,j]))
                    if i == n-1:
                        file.writelines('}\n')
                    else:
                        file.writelines('},\n')
    
                file.writelines('  };\n')
    
                file.writelines('const double dA{}[][{}] = \n'.format(k,n))
                file.writelines('  {\n')
                for i in range(n):
                    file.writelines('    {')
                    for j in range(n):
                        if j == n-1:
                            file.writelines('{}'.format(A[i,j]))
                        else:
                            file.writelines('{},'.format(A[i,j]))
                    if i == n-1:
                        file.writelines('}\n')
                    else:
                        file.writelines('},\n')
    
                file.writelines('  };\n')

            file.writelines('const int *Ap[{}] = {{{}}}; \n'.format(len(n_array),",".join(['(int*) A'+str(element) for element in np.arange(len(n_array))])))
            file.writelines('const int *Bp[{}] = {{{}}}; \n'.format(len(n_array),",".join(['(int*) B'+str(element) for element in np.arange(len(n_array))])))
            file.writelines('const double *dAp[{}] = {{{}}}; \n'.format(len(n_array),",".join(['(double*) dA'+str(element) for element in np.arange(len(n_array))])))
            file.writelines('const double *dBp[{}] = {{{}}}; \n'.format(len(n_array),",".join(['(double*) dB'+str(element) for element in np.arange(len(n_array))])))
            file.writelines('int n[{}] = {{{}}}; \n'.format(len(n_array),",".join([str(element) for element in n_array])))
            file.writelines('int n_arrays = {};\n'.format(len(n_array)))

# test%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
if __name__ == '__main__':

    helper = Helper()
    # n = np.arange(2,10)
    n = np.logspace(1,11,11,base=2,dtype=(np.int))
    # n=[8192]
    # C = helper.write_c_matrix(n)
