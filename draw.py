# 1. 背景全透明
# 2. 畫實心 圓形
# 3. 內圈白底
# 4. 寫字
import sys
import Image
import ImageDraw
import ImageFont

def to_unicode_or_bust(obj, encoding='utf-8'):
     if isinstance(obj, basestring):
         if not isinstance(obj, unicode):
             obj = unicode(obj, encoding)
     return obj


if __name__ == "__main__":
    if len(sys.argv) > 1:
        word = sys.argv[1]
	word = " " + to_unicode_or_bust(word) + " "
    else:
	word = u"    測試    "

image = Image.new("RGBA", (500,500),(255,255,255,0))
draw = ImageDraw.Draw(image)

x, y =  image.size
eX, eY = 200, 100 #Size of Bounding Box for ellipse

# 畫白圈
draw.setink((255,255,0))
draw.setfill(1)
bbox =  (x/2 - eX/2, y/2 - eY/2, x/2 + eX/2, y/2 + eY/2)
draw.ellipse(bbox)

# 畫外圈
draw.setink((255,0,0))
draw.setfill(0)
bbox =  (x/2 - eX/2, y/2 - eY/2, x/2 + eX/2, y/2 + eY/2)
#draw.ellipse(bbox)

# 寫字
draw.setink((255,0,0))
font = ImageFont.truetype("kaiu.ttf", 40)
draw.text((x/2-eX+eX/4, y/2-eY/4), word, font=font)

image.save("test.png", "PNG")
