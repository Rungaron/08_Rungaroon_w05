import math

pi = math.pi

def cal_circle_area(radius):
    '''คำนวณ พท. วงกลม'''
    return pi * radius ** 2

def cal_rect_area(width,lengh):
    '''คำนวณ พท. 4 เหลี่ยม'''
    return width * lengh

radius = 10
width = 2
lengh = 4

result = cal_circle_area(width,lengh)
print(result)




# () ** * / + -
# L ===> R