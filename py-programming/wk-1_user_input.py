#!/usr/bin/env python
"""
A company decided to give bonus of 5% to employee
if his/her year of service is more than 5 years.
Ask the user for their salary and year of service
and print the net bonus amount.

Write a python code to implement this scenario.
"""


print(f"Hello {input('[name]: ')}. Check if u r due for a bonus.")
salary = input("What is your salary: ")
service_yrs = input("For how long have u worked with us? ")

if int(service_yrs) >= 5:
    print(f"Your bonus is: {int(salary) * 5/100}")
else:
    print("You are not yet due for a bonus", end=" ")
    print(f"Just {5 - int(service_yrs)} years shy.")
