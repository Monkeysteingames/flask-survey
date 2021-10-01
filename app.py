from flask import Flask, request, render_template, redirect, flash
from flask.globals import session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)

app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

RESPONSES_KEY = "responses"


@app.route('/')
def home_page():
    """Shows home page"""

    return render_template('survey.html', survey=survey)


@app.route('/start-survey', methods=['POST'])
def begin_survey():
    """Wipe the session of response"""

    session[RESPONSES_KEY] = []

    return redirect('/questions/0')


@app.route("/questions/<int:question_id>")
def ask_question(question_id):
    """Ask the user question"""
    responses = session['responses']

    if (len(responses) is not question_id):
        flash('Attempted to access invalid question')
        return redirect(f'/questions/{len(responses)}')

    if (len(responses) == len(survey.questions)):
        # if we've answered each question then show thanks message and end survey
        return redirect("/thanks")

    question = survey.questions[question_id]

    return render_template('question.html', question=question, question_num=question_id)


@app.route('/thanks')
def handle_survey_completed():
    """Display thank you message and end survey"""
    return render_template('thanks.html')


@app.route('/answer', methods=['POST'])
def store_answer_continue_survey():
    """Saves our answer in the responses list and proceeds to the next question in the survey"""

    choice = request.form['answer']

    responses = session['responses']
    responses.append(choice)
    session['responses'] = responses

    if (len(responses) == len(survey.questions)):
        # if we've answered each question then show thanks message and end survey
        return redirect("/thanks")
    else:
        # move on to the next question
        return redirect(f"/questions/{len(responses)}")
