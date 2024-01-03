import pyttsx3
from pypdf import PdfReader
pdfreader = PdfReader("sample.pdf")
numPages = len(pdfreader.pages)
speaker = pyttsx3.init()
for page_num in range(numPages):   
    text = pdfreader.pages[page_num].extract_text()  ## extracting text from the PDF
    cleaned_text = text.strip().replace('\n',' ')  ## Removes unnecessary spaces and break lines
    speaker.say(cleaned_text)
    speaker.runAndWait()
speaker.stop()
