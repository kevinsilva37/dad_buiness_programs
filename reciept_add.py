#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import libaries needed for this project

import numpy as np

while True:
    # Declaring of variables
        x2='n'
        i=0
        sum=0
        # Start of program
        while True:
            x=input('How many reciepts are you adding up today?\n')
            print('You are adding up',x,'reciepts? y/n\n')
            x2=input()
            if(x2=='y'):
                from numpy import zeros
                reciept_vals= zeros([int(x)])
                break
        # Collect the reciept values and add them up
        print('Input the total values from the reciept below')

        for val in range(int(x)):
            x1=input('Total= ')
            reciept_vals[val]=float(x1)
            sum=sum+reciept_vals[val]

        print('Final sum=',sum) 
        
        repeat_ans=input('Would you like to use the application again? y/n\n')
        if(repeat_ans=='n'):
            break
    

