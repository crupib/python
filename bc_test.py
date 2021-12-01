from barcode import EAN13
from barcode.writer import ImageWriter

number='123456789123'
mycode=EAN13(number, writer=ImageWriter())
mycode.save('new')                                                                            
