# -*- coding: utf-8 -*-
"""yolov5_local_test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1abD93TChAlBMWUrolN2e1fcSOfnYlx8h
"""

import torch
import cv2

# Model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='/content/last.pt')  # local model

# Image
img_a = cv2.imread("/content/a.jpg")
img_contali = cv2.imread("/content/contali.jpg")

# Inference
result_contali = model(img_contali,size=512)
result_a = model(img_a,size=512)

type(result_contali.pandas().xyxy[0])

result_contali.pandas().xyxy[0]

rows_num=(result_contali.pandas().xyxy[0]).shape[0]
print(rows_num)

print((result_contali.pandas().xyxy[0]).iloc[0][5])

for i in range(0,rows_num):
  if (result_contali.pandas().xyxy[0]).iloc[i][5] == 0:#class = 0 , name = contali
    xmin=int((result_contali.pandas().xyxy[0]).iloc[i][0])
    ymin=int((result_contali.pandas().xyxy[0]).iloc[i][1])
    xmax=int((result_contali.pandas().xyxy[0]).iloc[i][2])
    ymax=int((result_contali.pandas().xyxy[0]).iloc[i][3])
    print(xmin)

  image = cv2.rectangle(img_contali, (xmin, ymin), (xmax, ymax), (0,255,12), 2)
  img_bordered=cv2.putText(image, 'contali', (xmin, ymin+30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

cv2.imwrite("bordered.jpg",img_bordered)