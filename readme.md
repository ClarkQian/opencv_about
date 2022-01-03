# introduction

​	这个程序是利用张正友标定法实现相机标定的相关操作，可以获取相机的内参和外参。使用的黑白棋盘的尺寸是5*7，在colibration文件夹中提供了样例

## 环境

1. 安装numpy

   ```python
   pip install numpy -i https://pypi.douban.com/simple
   ```

   

2. 安装opencv

   ```python
   pip install opencv-python https://pypi.douban.com/simple
   ```

   

## 使用

1. 在colibration中添加各种角度的对于棋盘的拍照，最好在12 ~ 20 张。
2. 执行 python camera_colibration.py。
3. 从控制台的打印中获取内外参。