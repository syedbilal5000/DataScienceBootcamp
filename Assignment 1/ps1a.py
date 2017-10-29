# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 22:24:49 2017

@author: Syed Bilal Hussain
"""

annual_salary=float(input("Enter your annual salary: "))
portion_saved=float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost=float(input("Enter the cost of your dream home: "))
portion_down_payment=0.25*total_cost
current_savings=float(0)
monthly_salary=float(annual_salary/12)
r=0.04
rate=0.04/12
monthly_savings=monthly_salary*0.1
m=0
while current_savings < portion_down_payment:
    returns = (current_savings * r / 12)
    current_savings += ( returns + monthly_salary*portion_saved )
    m+=1
print(m)