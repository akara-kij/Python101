# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 20:41:10 2021

@author: AkaraI7G10
"""

"""
Python Spyder เป็น Open-source IDE ของภาษา Python ออกแบบมาเพื่อ Scientist, Engineer และ Data Scient โดยเฉพาะ
มี Library ที่จำเป็นต่อการวิเคราะห์ข้อมูลติดตั้งมาตั้งแต่แรก
"""

'''
เริ่มเขียนโปรแกรมเป็นครั้งแรก Hello world

คำสั่ง print สามารถใช้แสดงผลข้อความที่ต้องการ
```print( Input String)``` ( หมายเหตุ ` สามาถพิมพ์ด้วยการกด Alt + 96 ส่วนเครื่องหมาย ~ ใช้ Alt + 126)
**ตัวอย่างเช่น** :  print("Hello World")
'''

print("Hello World")

#%%

"""

Section Divider in Spyder

- สามารถแบ่ง Code ใน Spyder เป็น Section ต่างๆ เพื่อ Run แยกจากกัน
- การสร้าง Section ทำได้โดยการใช้เครื่งหมาย #%%
- การ Run แต่ละ Section ทำได้โดยกด Ctrl + Enter

"""

print("Hello World of the 2nd Section")

#%%
## การใช้ Comment Line
#
#* Comment line เป็นการบอกให้ Python ทราบว่าบรรทัดที่ระบุนี้มิใช่ Code หากแต่เป็นข้อความที่โปรแกรมเมอร์ใส่ไว้เพื่อให้อธิบายรายละเอียดของ Code
#* ใช้เครื่องหมาย # เพื่อเปลี่ยนข้อความเป็น Comment Line

# ข้อความต่อไปนี้คือ Comment Line ดังนันภาษา Python จะข้าม Comment Line อันนี้ไป
print("Hello Comment Line")

#%%

## การใช้ Comment Block
#
# สามารถใส่คำอธิบายที่ยาวหลายบรรทัดได้ โดยนำข้อความเหล่านั้นให้อยู่ภายใต้เครื่องหายต่อไปนี้
# * Single Quote จำนวน 3 อัน ตัวอย่างเช่น ''' ข้อความ '''
# * Double Quote จำนวน 3 อัน ตัวอย่างเช่น """  ข้อความ """

"""
ตัวอย่าง Comment Block ภายใต้เครื่องหมาย Double Quote
1. บรรทัดที่ 1
2. บรรทัดที่ 2
3. บรรทัดที่ 3
"""
print("ตัวอย่างการสร้าง Comment Block ด้วย Double Quote")

'''
ตัวอย่าง Comment Block ภายใต้เครื่องหมาย Single Quote
1. บรรทัดที่ 1
2. บรรทัดที่ 2
3. บรรทัดที่ 3
'''
print("ตัวอย่างการสร้าง Comment Block ด้วย Single Quote")