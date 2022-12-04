from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def directtohomepage():
    return render_template("form.html")


@app.route('/process', methods=['POST'])
def process():
    session['yourname'] = request.form['yourname']
    session['dojolocation'] = request.form['dojolocation']
    session['favoritelanguage'] = request.form['favoritelanguage']
    session['comment'] = request.form['comment']
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

