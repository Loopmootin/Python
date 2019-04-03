from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results'
    results = str(search4letters(phrase, letters))
    return render_template('result.html', the_phrase = phrase, the_letters = letters, the_title = title, the_results = results)


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title="Welcome to the search4letters on the web")

if __name__ == '__main__':
    app.run('localhost', 4449)