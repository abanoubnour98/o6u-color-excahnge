from flask import Flask, render_template, request
from PIL import Image
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def get_dominant_color(img):
    img = img.convert('RGBA')
    colors = img.getcolors(img.size[0] * img.size[1])
    most_common_color = max(colors, key=lambda x: x[0])[1]
    return most_common_color

def save_image(image):
    filename = image.filename
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    image.save(filepath)
    return filename

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        image = request.files['file']
        if image:
            img = Image.open(image)
            dominant_color = get_dominant_color(img)
            filename = save_image(image)
            hex_color = rgba_to_hex(dominant_color)
            return render_template('index.html', dominant_color=dominant_color, hex_color=hex_color, filename=filename)
    return render_template('index.html')


@app.route('/exchange', methods=['GET', 'POST'])
def exchange():
    if request.method == 'POST':
        hex_code = request.form['hex_code']
        file = request.form['file']
        return render_template('exchange.html', hex_code=hex_code, file=file)
    return render_template('exchange.html')

def rgba_to_hex(rgba_color):
    red = int(rgba_color[0])
    green = int(rgba_color[1])
    blue = int(rgba_color[2])
    hex_color = '#{:02x}{:02x}{:02x}'.format(red, green, blue)
    return hex_color

if __name__ == '__main__':
    app.run()
