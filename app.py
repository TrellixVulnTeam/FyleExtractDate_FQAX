from PIL import Image
import os
import io
import time
from regex_date import run_func
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Lets define the modules that I will be using for the task
# Function to change the image bytes to text_data
def change_jpg_to_text(image_name):
    new_image_name = image_name + '.txt'
    # This thing creates a new new file in this directory 
    # with the name text_image.txt
    im = Image.open(image_name)
    # time.sleep(1)
    # Lets read that file up
    # f = open('{}'.format(image_name + '.txt'), 'r')
    time.sleep(3)
    # print(image_name + '.txt')
    output_string = pytesseract.image_to_string(image_name, lang = 'eng')
    return output_string

# FUnction to read the image_text file
def read_file(filename):
    output_string = ""
    filehandle = open(filename)
    while True:
        line = filehandle.readline()
        output_string += line
        if not line:
            # pass
            return str(output_string) 



from flask import Flask, jsonify, request,render_template

app = Flask(__name__)
@app.route('/extract_date',methods=['POST'])
def predicts():
    if request.method == 'POST':
       
        file = request.files['file']
        img_bytes = file.read()
        image = Image.open(io.BytesIO(img_bytes))
        image.save('newfile', "JPEG")
        text_string = change_jpg_to_text('newfile')
        result = run_func(text_string)
        return jsonify({'Dates Captured': result}) 

    else:
        return render_template('predict.html')
@app.route('/extract_date')
def runit():
    return render_template('predict.html')
    

if __name__ == "__main__":
    app.run()