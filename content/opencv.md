## opencv

有名的图像处理库，可以处理图像，视频，2D，3D 一切与图像有关的东西。opencv 也有和 Python 一样的问题，2.X 的版本与 3.X 的版本不兼容，虽然在使用的时候，导入 opencv 库的时候都叫 cv2 。但是并不是和其他的库一样 2.X 支持 python 2，3.X 支持 python 3 ，它的这俩版本都是支持 Python 2 的。。。

可以通过

```
cv2.__version__
```

查看 openCV 的版本

### 安装使用

在 [官网](http://opencv.org/downloads.html) 下载 opencv 安装，其实安装就是一个解压的过程，然后将 `/opencv/build/python/cv2.pyd` 复制到 python 的 `/Python27/Lib/site-packages` 目录下即可使用。

在 `/opencv/sources/samples/python` 有一些 opencv 的示例源码，可以尝试运行一下，可能需要安装 numpy 库。

下面使用的 openCV 若未特殊强调，都是使用 `3.0.0` 的版本

### 图片处理

#### 打开图片

```
# coding=utf-8

import cv2   
  
img = cv2.imread("code.jpg")   
cv2.namedWindow("Image")   
cv2.imshow("Image", img)   
cv2.waitKey (0)
cv2.destroyAllWindows()  
```

### 视频处理

### 打开摄像头

`S` 键保存图像，`Q` 键退出 

```
# coding=utf-8

import cv2
import time

cap = cv2.VideoCapture(0)

while(True):
    # 每次从视频数据流框架中抓取一帧图片
    ret, frame = cap.read()

    # 将图片显示在特定窗口上
    cv2.imshow('OpenCV Capture',frame)

    # 当按下 q 键时退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # 当按下 s 键时保存图像
    key = cv2.waitKey(1)
    if key == ord('s'):
        filename = time.strftime('%Y%m%d-%H%M%S') + ".jpg"
        cv2.imwrite(filename, frame)
```

用 openCV 2.4.13 的话，是这样

```
coding=utf-8

import cv2.cv as cv

capture = cv.CaptureFromCAM(0)

# 定义一个无限循环
while 1:

  # 每次从视频数据流框架中抓取一帧图片
    image = cv.QueryFrame(capture)

    # 将图片显示在特定窗口上
    cv.ShowImage("OpenCV Capture", image)

    # 当按下Esc键时退出循环
    c = cv.WaitKey(1)
    if c == 27:
        break
```