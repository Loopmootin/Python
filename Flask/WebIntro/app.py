# inspired by Paul Barry : Head First Python.

from flask import Flask, render_template, request
from LetterSearch import search4letters

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return "Hello"


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results'
    results = str(search4letters(phrase, letters))
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results)


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title="Welcome to search4letters on the web")


#####################################################################
# Port can be set at properties - Debug - Port Number.
if __name__ == '__main__':
    app.run('localhost', 4449)