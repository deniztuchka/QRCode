from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    qr_code = None
    if request.method == 'POST':
        text = request.form['text']
        qr = qrcode.make(text)

        img_io = BytesIO()
        qr.save(img_io, 'PNG')
        img_io.seek(0)

        # QR kodunu base64 formatına çevirerek HTML'de göstermek için
        qr_code = base64.b64encode(img_io.getvalue()).decode()

    return render_template('index.html', qr_code=qr_code)

if __name__ == '__main__':
    app.run(debug=True)
