from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')  # Use '.' to point to the current folder

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/enterpage')
def enterpage():
    return render_template('enterpage.html')


@app.route('/reveal', methods=['POST'])
def reveal():
    adjective = request.form.get('adjective')
    noun = request.form.get('noun')
    verb_past = request.form.get('verb_past')
    plural_noun = request.form.get('plural_noun')
    number = request.form.get('number')

    return render_template(
        'reveal.html',
        adjective=adjective,
        noun=noun,
        verb_past=verb_past,
        plural_noun=plural_noun,
        number=number
    )

    
if __name__ == '__main__':
    app.run(debug=True)