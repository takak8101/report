#!/usr/bin/python3

import re
                
def calc(A,B):
        ai=str(A)
        bi=str(B)
        #p = re.compile('\d+(\.\d+)?')
        p = re.compile('\d+')
        #if p.match(ai) or p.match(bi):
        if p.fullmatch(ai) and p.fullmatch(bi):
                a=float(ai)
                b=float(bi)
                if 0<a and 0<b and a<1000 and b<1000:
                        valid=True
                else:
                        valid=False
        else:
                valid=False
                
        if valid:
                ans=a*b
                return ans
        else:
                return -1
        
                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()
