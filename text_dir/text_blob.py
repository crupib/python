from textblob import TextBlob

text = input("Enter a text that needs spelling correction: ")
blob = TextBlob(text)
blob_corrected = blob.correct()
print(blob_corrected.string)                                                                     
