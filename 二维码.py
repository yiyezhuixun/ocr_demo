# import cv2
# from pyzbar.pyzbar import decode
# from PIL import Image
# import numpy as np
# # 载入图片
# image_path = 'CHA4_400_20_frame_4.jpg'  # 替换为你的图片路径
# image = cv2.imread(image_path)
# # 解码二维码
# decoded_objects = decode(image)
# print(decoded_objects)
# # 输出解码结果
#
# for obj in decoded_objects:
#     qr_data = obj.data.decode('utf-8')
#     qr_type = obj.type
#     print(f'Data: {qr_data}, Type: {qr_type}')
#     # 可视化显示二维码的边框
#     points = obj.polygon
#     if len(points) == 4:
#         pts = [tuple(point) for point in points]
#         cv2.polylines(image, [np.array(pts, dtype=np.int32)], True, (0, 0, 255), 2)
#
# # 显示视频流
# cv2.imshow("QR Code Scanner", image)
# cv2.waitKey(0)
from qreader import QReader
import cv2
import time
import numpy as np
import os
# Create a QReader instance
qreader = QReader()

def bacth_images():
    dir_path = "0115_ori_400"
    files = os.listdir(dir_path)
    for file in files:
        img_path = os.path.join(dir_path, file)
        start = time.time()
    # Get the image that contains the QR code
        image = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB)
        cv2.imshow('image', image)
        print("检测图像： ",file)
        cv2.waitKey(1)
        fontFace = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        color =(0, 0, 255) # BGR格式，白色
        thickness = 4
        # Use the detect_and_decode function to get the decoded QR data
        decoded_text = qreader.detect_and_decode(image=image,return_detections=True)
        if len(decoded_text[1]) >2:
            a = int(int(decoded_text[1][0]['polygon_xy'][0][0] + decoded_text[1][0]['polygon_xy'][2][0]) / 6)
            b = int(int(decoded_text[1][0]['polygon_xy'][0][1] + decoded_text[1][0]['polygon_xy'][2][1]) / 2)
            # org = ((int(decoded_text[1][0]['polygon_xy'][0][0] + decoded_text[1][0]['polygon_xy'][2][0]) / 2), int((decoded_text[1][0]['polygon_xy'][0][1] + decoded_text[1][0]['polygon_xy'][2][1]) / 2))
            print(decoded_text)
            cv2.polylines(image, [np.array(decoded_text[1][0]['quad_xy'], dtype=np.int32)], True, (0, 0, 255), 2)
            cv2.putText(image,str("resut:")+str(decoded_text[0]),(a,b), fontFace, fontScale, color, thickness)
            print("分析时间：",time.time() - start)
            cv2.imshow('image',image)
            file = os.path.basename(file)
            re = 'resut:'+file
            cv2.imwrite(re,image)

def singel_image():
    start = time.time()
    image = cv2.cvtColor(cv2.imread('600w_110_95.bmp'), cv2.COLOR_BGR2RGB)

    cv2.imshow('image', image)
    cv2.waitKey(1)
    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    color = (0, 0, 255)  # BGR格式，白色
    thickness = 4
    # Use the detect_and_decode function to get the decoded QR data
    decoded_text = qreader.detect_and_decode(image=image, return_detections=True)
    try:
        if decoded_text is not None:
            a = int(int(decoded_text[1][0]['polygon_xy'][0][0] + decoded_text[1][0]['polygon_xy'][2][0]) / 6)
            b = int(int(decoded_text[1][0]['polygon_xy'][0][1] + decoded_text[1][0]['polygon_xy'][2][1]) / 2)
            # org = ((int(decoded_text[1][0]['polygon_xy'][0][0] + decoded_text[1][0]['polygon_xy'][2][0]) / 2), int((decoded_text[1][0]['polygon_xy'][0][1] + decoded_text[1][0]['polygon_xy'][2][1]) / 2))
            print(decoded_text)
            cv2.polylines(image, [np.array(decoded_text[1][0]['quad_xy'], dtype=np.int32)], True, (0, 0, 255), 2)
            cv2.putText(image, str("resut:") + str(decoded_text[0]), (a, b), fontFace, fontScale, color, thickness)
            print("分析时间：", time.time() - start)
            cv2.imshow('image', image)
            cv2.waitKey(0)
            # file = os.path.basename(file)
            # re = 'resut:' + file
            # cv2.imwrite(re, image)
    except Exception as e:
        print(e)



if __name__ == '__main__':
    singel_image()
    # bacth_images()