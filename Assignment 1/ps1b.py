# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 19:25:42 2017

@author: Syed Bilal Hussain
"""

annual_salary=float(input("Enter your annual salary: "))
portion_saved=float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost=float(input("Enter the cost of your dream home: "))
semi_annual_raise=float(input("Enter the semi-annual raise, as a decimal: "))
portion_down_payment=0.25*total_cost
current_savings=float(0)
monthly_salary=float(annual_salary/12)
r=0.04
m=0
while current_savings < portion_down_payment:
    returns = (current_savings * r / 12)
    current_savings += ( returns + monthly_salary*portion_saved )
    m+=1
    if m%6==0:
        monthly_salary += monthly_salary * semi_annual_raise
print(m)