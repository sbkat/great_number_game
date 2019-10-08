from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = 'secretss'

@app.route('/')
def index():
    if "number" not in session:
        session["number"] = random.randint(1,100)
        session["counter"] = 0
    print(session["number"])
    return render_template('index.html')

@app.route('/submit', methods=["POST"])
def submit():
    guessed_num = request.form["guessed_number"]
    guessed_num = int(guessed_num)
    if guessed_num < session["number"]:
        session["result_message"] = "Too low!"
        session['counter'] += 1
    elif guessed_num > session["number"]:
        session["result_message"] = "Too high!"
        session['counter'] += 1
    else:
        session["result_message"] = "That was the number!"
        session['counter'] = session['counter']
    return redirect('/')
    
@app.route('/reset', methods=["POST"])
def reset():
    session.clear()
    session["result_message"] = "yas"
    return redirect ('/')

if __name__ == '__main__':
    app.run(debug=True)