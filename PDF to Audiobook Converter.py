import PyPDF2
from gtts import gTTS

pdf_file_path = 'sample.pdf'
pdf_file = open(pdf_file_path, 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

text = ""
for page in pdf_reader.pages:
    text += page.extract_text()

pdf_file.close()

tts = gTTS(text=text, lang='en')
tts.save("audiobook1.mp3")

print("✅ Natural voice audiobook saved as 'audiobook1.mp3'")
