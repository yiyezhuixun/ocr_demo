# # from paddleocr import PaddleOCR, draw_ocr
# #
# # # Paddleocr supports Chinese, English, French, German, Korean and Japanese
# # # You can set the parameter `lang` as `ch`, `en`, `french`, `german`, `korean`, `japan`
# # # to switch the language model in order
# # ocr = PaddleOCR(use_angle_cls=True, lang='en') # need to run only once to download and load model into memory
# # img_path = 'ocr.png'
# # result = ocr.ocr(img_path, cls=True)
# # for idx in range(len(result)):
# #     res = result[idx]
# #     for line in res:
# #         print(line)
# #
# # # draw result
# # from PIL import Image
# # result = result[0]
# # image = Image.open(img_path).convert('RGB')
# # boxes = [line[0] for line in result]
# # txts = [line[1][0] for line in result]
# # scores = [line[1][1] for line in result]
# # im_show = draw_ocr(image, boxes, txts, scores, font_path='/path/to/PaddleOCR/doc/fonts/simfang.ttf')
# # im_show = Image.fromarray(im_show)
# # im_show.save('result.jpg')
#
# from paddlex import create_pipeline
# import time
#
# s = time.time()
# pipeline = create_pipeline(pipeline='OCR')
# result = pipeline.predict(['ocr.png'])
# for res in result:
#     a= res.print()
#     print("aaa:",a)
#     res.save_to_img("./output/")
#     res.save_to_json("./output/")
# print(time.time() - s)
from paddleocr import PaddleOCR, draw_ocr
# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
import time
s = time.time()
ocr = PaddleOCR(use_angle_cls=False, lang="ch")  # need to run only once to download and load model into memory
for i in range(100):
    img_path = r'C:\Al\Software\AI_Model\Project\2D_model\OCR_Model\ocr.png'
    result = ocr.ocr(img_path, cls=True)
    print("模型检测用时：  ",time.time() - s)
    for idx in range(len(result)):
        res = result[idx]
        for line in res:
            print(line)
    # 显示结果
    from PIL import Image
    result = result[0]
    image = Image.open(img_path).convert('RGB')
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(image, boxes, txts, scores, font_path='./fonts/simfang.ttf')
    im_show = Image.fromarray(im_show)
    im_show.save('result.jpg')
    print("最终用时：  ",time.time() - s)
    print(f"执行第{i}次")