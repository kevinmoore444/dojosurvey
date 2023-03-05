from flask import Flask, render_template, request, redirect, session
from survey_model import Survey
app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def directtohomepage():
    return render_template("form.html")


@app.route('/process', methods=['POST'])
def process():
    if not Survey.validator(request.form):
        return redirect('/')
    session['yourname'] = request.form['yourname']
    session['dojolocation'] = request.form['dojolocation']
    session['favoritelanguage'] = request.form['favoritelanguage']
    session['comment'] = request.form['comment']
    Survey.create(request.form)
    return redirect('/result')


@app.route('/result')
def displayresult():
    return render_template("result.html")

@app.route('/clear_session')
def go_back():
    session.clear
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)

