# -*- coding: utf-8 -*-
"""HW1-BMI.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PmEcFBgrzXGV10H1CjljXbkfBT3utq0X
"""

h = float(input("請輸入您的身高(公尺):"))
w = float(input("請輸入您的體重(公斤):"))
bmi = w/(h**2)
print(f"您的BMI是:{bmi:.2f}")