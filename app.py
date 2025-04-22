from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = {}
    if request.method == 'POST':
        binary_input = request.form['binary']

        try:
            decimal = int(binary_input, 2)
            result['decimal'] = decimal
            result['octal'] = oct(decimal)[2:]
            result['hexadecimal'] = hex(decimal)[2:].upper()
        except ValueError:
            result['error'] = 'Entrada inválida. Use apenas 0 e 1.'

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
