from IPython.display import Image as IPythonImage
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
def display_cover(top,bottom ):
    """This fucntoin
    """
    import requests
    
    name='album_art_raw.png'

    album_art_raw = requests.get('https://picsum.photos/500/500/?random')
    # and save it as 'album_art_raw.png'
    with open(name,'wb') as album_art_raw_file:
       album_art_raw_file.write(album_art_raw.content)
    
    
    
    img = Image.open("album_art_raw.png")
    draw = ImageDraw.Draw(img)

    
    band_name_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 25) #25pt font
    album_name_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20) # 20pt font

    
    band_x, band_y = 50, 50
    album_x, album_y = 50, 400

 
    outline_color ="black"

    draw.text((band_x-1, band_y-1), top, font=band_name_font, fill=outline_color)
    draw.text((band_x+1, band_y-1), top, font=band_name_font, fill=outline_color)
    draw.text((band_x-1, band_y+1), top, font=band_name_font, fill=outline_color)
    draw.text((band_x+1, band_y+1), top, font=band_name_font, fill=outline_color)

    draw.text((album_x-1, album_y-1), bottom , font=album_name_font, fill=outline_color)
    draw.text((album_x+1, album_y-1), bottom , font=album_name_font, fill=outline_color)
    draw.text((album_x-1, album_y+1), bottom , font=album_name_font, fill=outline_color)
    draw.text((album_x+1, album_y+1), bottom , font=album_name_font, fill=outline_color)

    draw.text((band_x,band_y),top,(255,255,255),font=band_name_font)
    draw.text((album_x, album_y),bottom,(255,255,255),font=album_name_font)

    return img
img=display_cover(top='Python',bottom='Data Science')
img.save('gaurav.png')


import requests
wikipedia_link='https://en.wikipedia.org/wiki/Special:Random'
raw_random_wikipedia_page=requests.get(wikipedia_link)
page=raw_random_wikipedia_page.text
print(page)


a=page.find('<title>')
b=page.find('</title>')
c=len('<title>')
d=page[a+c:b]
band_title=d.replace(' - Wikipedia','')




wikipedia_link='https://en.wikipedia.org/wiki/Special:Random'
raw_random_wikipedia_page=requests.get(wikipedia_link)
page=raw_random_wikipedia_page.text
print(page)



a=page.find('<title>')
b=page.find('</title>')
c=len('<title>')
d=page[a+c:b]
album_title=d.replace(' - Wikipedia','')
print("Your band: ", band_title)
print("Your album: ", album_title)

img=display_cover(top=band_title,bottom=album_title)
img.save('gaurav2.png')

IPythonImage(filename='gaurav.png')
IPythonImage(filename='gaurav2.png')

