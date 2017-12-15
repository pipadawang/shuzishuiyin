import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import cv2
import numpy as np
import qrcode
import os


def Encode(image2):
    img = cv2.imread(image2)
    out = np.zeros(img.shape, np.uint8)
    w, h = img.shape[:2]
    for i in range(w):
        for j in range(h):
            if img[i, j, 2] % 2 == 0:
                out[i, j, 0] = 255
                out[i, j, 1] = 255
                out[i, j, 2] = 255
            else:
                out[i, j, 0] = 0
                out[i, j, 1] = 0
                out[i, j, 2] = 0
    cv2.imwrite("out.bmp", out)

def code(text1,image1):
    #生成原始二维码
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=0,
    )
    qr.add_data(text1)
    qr.make(fit=True)
    img = qr.make_image()
    img.save('123.bmp')
    #合成二维码
    im = Image.open(image1)
    cropedImage = Image.open('123.bmp')
    im.paste(cropedImage, (0, 0))
    #im.show()
    im.save('321.bmp')
    img = cv2.imread(image1)

    #备份图像
    im1=cv2.imread(image1)

    code = cv2.imread("321.bmp")
    w, h = img.shape[:2]
    # print w,h
    for i in range(w):
        for j in range(h):
            if img[i, j, 2] % 2 != 0:
                img[i, j, 2] = img[i, j, 2] + 1 if img[i, j, 2] < 2 else img[i, j, 2] - 1
                # cv2.imwrite("quanou.bmp",img)
    for i in range(w):
        for j in range(h):
            if code[i, j, 0] == 0 and code[i, j, 1] == 0 and code[i, j, 2] == 0:
                img[i, j, 2] += 1
    cv2.imwrite("final.bmp", img)

def main():
    print("1.隐藏信息")
    print("2.解密信息")
    print("3.清除临时文件并退出程序")
    #print("4.退出程序")
    choose=eval(input("请输入数字选择功能："))

    if choose==1:
        text1 = input("请输入要隐藏的信息：")
        image1 = input("请输入载体图片：")
        code(text1, image1)
        return choose
    elif choose==2:
        image2 = input("请输入要解密的图片：")
        Encode(image2)
        return choose
    elif choose==3:
        if os.path.exists('123.bmp') is True:
            os.remove('123.bmp')
            os.remove('321.bmp')
            return choose
        else:
            print("无临时文件可清理")
            return choose
    elif choose==4:
        return choose
#a=eval(1)
while main()==3:
    exit()
else:
    main()




