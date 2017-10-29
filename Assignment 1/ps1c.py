# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 21:00:41 2017

@author: Syed Bilal Hussain
"""

import sys
starting_salary=float(input("Enter the starting salary: "))
total_cost=float(1000000)
semi_annual_raise=float(0.07)
portion_down_payment=0.25*total_cost
current_savings=float(0)
monthly_salary=float(starting_salary/12)
error=10
mn=float(0)
mx=float(10000)
guess=(mx-mn)/2
r=0.04
steps=0
x=0
#if starting_salary <= 10000:
#    print('It is not possible to pay the down payment in three years.')
#    sys.exit()
while abs(current_savings-portion_down_payment)>=error and starting_salary > 10000:
    guess=(mx+mn)/2
    savingsrate=guess/10000
    current_savings=0
    presentSalary = starting_salary
    monthly_salary=float(presentSalary/12)
    for months in range(1, 37):
        returns =  (current_savings*r)/12
        current_savings += savingsrate*monthly_salary + returns
        if months %6 ==0:
            monthly_salary += monthly_salary * semi_annual_raise
    if current_savings < portion_down_payment:
        mn=guess
    else:
        mx=guess
    x=1
    steps+=1
if x:
    print('Best savings rate: %.4f' % savingsrate)
    print('Steps in bisection search: ',steps)
else:
    print('It is not possible to pay the down payment in three years.')