# -*- coding:utf-8 -*-
# 文件名称：Hg-lyycc-智慧收银图片合成
# 作者:清许丶
# 谨记:遵守秩序，尊重选择。
# 创建时间：2020/12/1 11:04

from matplotlib import image
import matplotlib.pyplot as plt

# 原图
img = image.imread(r"C:\Users\LyyCc\Desktop\二维码.png")
# 分割图
msk = image.imread(r"C:\Users\LyyCc\Desktop\贴图.png")

plt.subplot(2, 2, 2)
plt.imshow(img)
plt.subplot(2, 2, 1)
plt.imshow(msk)
# 图像融合显示
# plt.subplot(2, 2, 3)
plt.imshow(img, alpha=0.6)
plt.imshow(msk, alpha=0.4)
plt.show()