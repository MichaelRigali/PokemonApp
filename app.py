from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Data for dynamic content
    image_url = 'https://example.com/image.jpg'
    button_text = 'Click Me'

    return render_template('index.html', image_url=image_url, button_text=button_text)

if __name__ == '__main__':
    app.run(debug=True)
