import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
bg = np.array(Image.open("12.jpg"))
with open('/home/lsgo28/PycharmProjects/demo/ciyun.txt','r') as f:
    fl = f.read()
fl = fl.replace(',','\n')
wc = WordCloud(background_color="white",
    max_words=200,
    mask=bg,
    max_font_size=60,
    random_state=42,
    font_path='/home/lsgo28/PycharmProjects/demo/ziti.ttf').generate(fl)
image_color = ImageColorGenerator(bg)
plt.imshow(wc.recolor(color_func=image_color))
wc.to_file("ciyun.png")