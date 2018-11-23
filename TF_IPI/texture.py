import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import matplotlib.patches as patches
import matplotlib.cm as cm

img = cv2.imread('img.jpeg', 0)
h, w = img.shape
print img.shape

fig, ax = plt.subplots(figsize=[w/100.0, h/100.0])
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
im = ax.imshow(img, cmap='gray')
NUM = h*w/30
ells = [Ellipse(xy=(np.random.rand(2) * [w, h]),
                width=np.random.rand()*5, height=np.random.rand()*5,
                angle=np.random.rand() * 360, fill=False, color='white')
        for i in range(NUM)]
for e in ells:
    ax.add_artist(e)
    e.set_clip_box(ax.bbox)
    e.set_alpha(np.random.rand())
ax.axis('off')
plt.box(False)
fig.canvas.draw()

X = np.array(fig.canvas.renderer._renderer)

img = X.copy()
cv2.imshow('image',img)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print img_gray.shape
cv2.imwrite('funciona.jpeg', img_gray)
