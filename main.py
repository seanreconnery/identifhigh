import requests
import json
from flask import Flask, render_template, Markup, request
import time
from controller import indica_strains, sativa_strains, hybrid_strains, get_all_strains, search_by_pos_fx, search_by_med_fx, get_strain_by_id

app = Flask(__name__)

with open('full_db.json') as f:
    asdf = json.loads(f.read())

jobj = asdf
asdf = None

@app.route('/searchfx/positive', methods=['post'])
def search_positive_fx():
    search_items = list()
    item_pos = list()

    if 'giggly' in request.form:
        item_pos.append('Giggly')
        search_items.append('Giggly')

    if 'focused' in request.form:
        item_pos.append('Focused')
        search_items.append('Focused')

    if 'relaxed' in request.form:
        item_pos.append('Relaxed')
        search_items.append('Relaxed')

    if 'euphoric' in request.form:
        item_pos.append('Euphoric')
        search_items.append('Euphoric')

    if 'happy' in request.form:
        item_pos.append('Happy')
        search_items.append('Happy')

    if 'uplifted' in request.form:
        item_pos.append('Uplifted')
        search_items.append('Uplifted')

    if 'creative' in request.form:
        item_pos.append('Creative')
        search_items.append('Creative')

    if 'aroused' in request.form:
        item_pos.append('Aroused')
        search_items.append('Aroused')

    if 'tingly' in request.form:
        item_pos.append('Tingly')
        search_items.append('Tingly')

    if 'sleepy' in request.form:
        item_pos.append('Sleepy')
        search_items.append('Sleepy')

    if 'talkative' in request.form:
        item_pos.append('Talkative')
        search_items.append('Talkative')

    html_pos = search_by_pos_fx(jobj, item_pos)

    return render_template('search.html', respos=Markup(html_pos))



@app.route('/searchfx/medical', methods=['post'])
def search_medical_fx():
    search_items = list()
    item_med = list()

    ### medical effects
    if 'depression' in request.form:
        item_med.append('Depression')
        search_items.append('Depression')

    if 'headaches' in request.form:
        item_med.append('Headaches')
        item_med.append('Headache')
        search_items.append('Headaches')
        search_items.append('Headache')

    if 'fatigue' in request.form:
        item_med.append('Fatigue')
        search_items.append('Fatigue')

    if 'musclespasms' in request.form:
        item_med.append('Muscle Spasms')
        search_items.append('Muscle Spasms')

    if 'cramps' in request.form:
        item_med.append('Cramps')
        search_items.append('Cramps')

    if 'insomnia' in request.form:
        item_med.append('Insomnia')
        search_items.append('Insomnia')

    if 'inflammation' in request.form:
        item_med.append('Inflammation')
        search_items.append('Inflammation')

    if 'pain' in request.form:
        item_med.append('Pain')
        search_items.append('Pain')

    if 'stress' in request.form:
        item_med.append('Stress')
        search_items.append('Stress')

    if 'nausea' in request.form:
        item_med.append('Nausea')
        search_items.append('Nausea')

    if 'eyepressure' in request.form:
        item_med.append('Eye Pressure')
        search_items.append('Eye Pressure')

    if 'lackofappetite' in request.form:
        item_med.append('Lack of Appetite')
        search_items.append('Lack of Appetite')

    html_med = search_by_med_fx(jobj, item_med)

    return render_template('search.html', resmed=Markup(html_med))


@app.route('/strain/<id>', methods=['GET'])
def strain_by_id(id):
    html = get_strain_by_id(jobj, id)

    return render_template('strain.html', strains=Markup(html))


@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/hybrid')
def the_hybrids():
    html = hybrid_strains(jobj)
    return render_template('hybrid.html', strains=Markup(html))


@app.route('/indica')
def the_indicas():
    html = indica_strains(jobj)
    return render_template('indica.html', strains=Markup(html))


@app.route('/sativa')
def the_sativas():
    html = sativa_strains(jobj)
    return render_template('sativa.html', strains=Markup(html))


@app.route('/allofthem')
def all_strains():
    html = get_all_strains(jobj)
    return render_template('strains.html', strains=Markup(html))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)