from captcha.image import ImageCaptcha

image = ImageCaptcha(width=280,height=90)
data = image.generate('MEDIUM')
image.write('MEDIUM', 'out.png')                                                       
