#!/usr/bin/env python
"""
Exercise:
Write a program for a hospital

Check in a patient named John Smith
He is 20 years old
He is a new Patient
Declare variables to store this values
"""


pat_name = "John Smith"
pat_age = 20
pat_info = "He is a new Patient"

patient = (f"- Check in a patient named {pat_name}\n"
           f"- He is {pat_age} years old\n- {pat_info}.")

print(patient)
