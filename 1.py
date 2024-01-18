import PyPDF2
import gtts
#get text from pdf file
def extract_text_from_pdf(pdf_path): 
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    return text

extracted_text = extract_text_from_pdf('./123.pdf')


tts = gtts.gTTS("Hello", lang='pl', slow=False )
tts.save("polish_2.mp3")


tts = gtts.gTTS(extracted_text, lang='pl', slow=False)
tts.save("german_2.mp3")
