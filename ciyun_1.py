import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

text = "hello"

# 返回两个数组，只不过数组维度分别为n*1 和 1* m
x, y = np.ogrid[:300, :300]

# 设置绘图区域
mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
mask = 255 * mask.astype(int)

# 绘制词云，repeat表示重复输入文本直到允许的最大词数max_words，scale设置放大比例
wc = WordCloud(background_color="white", repeat=True,max_words=32, mask=mask,scale=1.5)
wc.generate(text)

plt.axis("off")
plt.imshow(wc, interpolation="bilinear")
plt.show()

# 输出到文件
_ = wc.to_file("result.jpg")