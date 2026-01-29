from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    text = ''
    translation = ''
    if request.method == 'POST':
        text = request.form.get('text', '')
        if text.strip():
            try:
                translation = GoogleTranslator(source='auto', target='kn').translate(text)
            except Exception as e:
                translation = f'Error: {e}'
    return render_template('index.html', text=text, translation=translation)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)

