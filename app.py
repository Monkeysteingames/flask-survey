from flask import Flask, request, render_template, redirect, flash
from flask.helpers import get_flashed_messages
from flask_debugtoolbar import DebugToolbarExtension
import surveys

app = Flask(__name__)

app.config['SECRET_KEY'] = "chickenzarecool21837"
debug = DebugToolbarExtension(app)

DEBUG_TB_INTERCEPT_REDIRECTS = False

responses = []


@app.route('/')
def home_page():
    """Shows home page"""

    survey = surveys.satisfaction_survey
    return render_template('home.html', survey=survey)


@app.route("/questions/0")
def ask_question0():
    """Ask the user question 1"""
    get_flashed_messages
    survey = surveys.satisfaction_survey
    return render_template('question1.html', survey=survey)


@app.route('/questions/1')
def ask_question1():
    """Ask the user question 2"""
    get_flashed_messages
    survey = surveys.satisfaction_survey
    return render_template('question2.html', survey=survey)


@app.route('/questions/2')
def ask_question2():
    """Ask the user question 3"""
    get_flashed_messages
    survey = surveys.satisfaction_survey
    return render_template('question3.html', survey=survey)


@app.route('/questions/3')
def ask_question3():
    """"Ask the user question 4"""
    get_flashed_messages
    survey = surveys.satisfaction_survey
    return render_template('question4.html', survey=survey)


@app.route('/thanks')
def show_thanks_msg():
    """Display thank you message and end survey"""
    return render_template('thanks.html')


@app.route('/answer', methods=['GET', 'POST'])
def store_answer_continue_survey():
    """Saves our answer in the responses list and proceeds to the next question in the survey"""

    response = ''.join(list(request.args))
    responses.append(response)
    print(responses)
    if request.referrer.__contains__('/questions/0') and len(responses) <= 1:
        return redirect('/questions/1')
    elif request.referrer.__contains__('/questions/1') and len(responses) <= 2:
        return redirect('/questions/2')
    elif request.referrer.__contains__('/questions/2') and len(responses) <= 3:
        return redirect('/questions/3')
    elif request.referrer.__contains__('/questions/3') and len(responses) <= 4:
        return redirect('/thanks')
    else:
        if len(responses) == 1:
            flash('Invalid question')
            return redirect('/questions/1')
        elif len(responses) == 2:
            flash('Invalid question')
            return redirect('/questions/2')
        elif len(responses) == 3:
            flash('Invalid question')
            return redirect('/questions/3')
        else:
            return redirect('/thanks')
