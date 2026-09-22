from flask import Flask, render_template_string

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Render Example</title>
</head>
<body>
    <h1>Hello, {{ name }}!</h1>
    <p>Welcome to the Flask render example.</p>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template, name="alice")

@app.route('/about')
def about():
    return render_template_string(html_template, name="bob")

if __name__ == '__main__':
    app.run(debug=True)