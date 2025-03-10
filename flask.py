from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form['text']
        qr = qrcode.make(text)
        img_io = BytesIO()
        qr.save(img_io, 'PNG')
        img_io.seek(0)
        return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='qrcode.png')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
