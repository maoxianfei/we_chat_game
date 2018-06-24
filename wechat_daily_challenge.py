import os
from PIL import Image
import cv2
from PIL import ImageChops
import matplotlib.pyplot as plt
import numpy as np

def pull_screenshot():
    #os.system('adb shell screencap -p /sdcard/findTheDiff.png')
    #os.system('adb pull /sdcard/findTheDiff.png .')
    img=cv2.imread('findTheDiff.png')
    #crop_img1=img[168:991,214:1039]#这里需要将对比的部分以img的格式提取出来
    #crop_img2=img[1027:1850,214:1039]
    crop_img1=img[165:999,210:1040]#截取范围高度（上：下） 宽度（左：右）
    crop_img2=img[1025:1850,210:1045]
    cv2.imwrite('img1.png',crop_img1)
    cv2.imwrite('img2.png',crop_img2)
    img1=Image.open('img1.png')
    img2=Image.open('img2.png')
    out=ImageChops.difference(img1,img2)
    out.save('img3.png')
    return out

def on_click(event):
    click_count = 0
    ix,iy=event.xdata,event.ydata
    coords=[(int(ix)+214,int(iy)+168)]#从小方块坐标转换到屏幕坐标
    print('now=',coords)
    click_count+=1
    if click_count>0:
        click_count=0
        press(coords)

def press(coords):
    ix = coords[0][0]
    iy = coords[0][1]
    cmd = 'adb shell input swipe {x1} {y1} {x2} {y2} {duration}'.format(x1=ix-10,y1=iy-10,x2=ix+10,y2=iy+10,duration=100)
    os.system(cmd)
    

def main():
    while True:
        inp=input('是否更新图片(默认更新,输入n或N不更新)')
        if inp=='n' or inp=='N':
            break
        fig = plt.figure()
        img = np.array(pull_screenshot())
        im = plt.imshow(img, animated=True)
        fig.canvas.mpl_connect('button_press_event',on_click)
        plt.show()
if __name__=="__main__":
    main()
        
    





    


