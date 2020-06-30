import json
from flask import Flask, render_template, Markup, request


###     GET _INDICA_ STRAINS
def indica_strains(jobj):
    html = ''
    dd = 0
    for strain in jobj:
        dd += 1
        strainid = jobj[strain]['id']
        if not jobj[strain]['desc']:
            the_desc = "None"
        else:
            the_desc = jobj[strain]['desc'][0:200] + "..."

        stRace = jobj[strain]['race']
        posfx = '<div class="col-lg-12 pos-fx"><h5 class="handwriting">POSITIVE:</h5><ul>'
        negfx = '<div class="col-lg-12 neg-fx"><h5 class="handwriting">NEGATIVE:</h5><ul>'
        medfx = '<div class="col-lg-12 med-fx"><h5 class="handwriting">MEDICAL:</h5><ul>'

        if stRace == "indica":
            for x in jobj[strain]['effects']['positive']:
                posfx += "<li>" + x + "</li>"
            for x in jobj[strain]['effects']['negative']:
                negfx += "<li>" + x + "</li>"
            for x in jobj[strain]['effects']['medical']:
                medfx += "<li>" + x + "</li>"
            posfx += "</ul></div>"
            negfx += "</ul></div>"
            medfx += "</ul></div>"

            breed_indica = '<div class="col-lg-3 col-md-4 col-sm-6 portfolio-item"><div class="card h-100"><a href="/identifhigh/strain/' + str(strainid) + '"><img class="card-img-top" src="/identifhigh/static/img/indica_strain.png" alt="Indica"></a><div class="card-body"><h4 class="card-title"><a href="/identifhigh/strain/' + str(strainid) + '">'
            breed_indica += strain + '</a></h4><p class="card-text">' + the_desc + '</p>' + posfx + medfx + negfx + '</div></div></div>'

            html += breed_indica

    return html


###     GET _HYBRID_ STRAINS
def hybrid_strains(jobj):
    html = ''
    dd = 0
    for strain in jobj:
        dd += 1
        strainid = jobj[strain]['id']
        if not jobj[strain]['desc']:
            the_desc = "None"
        else:
            the_desc = jobj[strain]['desc'][0:200] + "..."

        stRace = jobj[strain]['race']
        posfx = '<div class="col-lg-12 pos-fx"><h5 class="handwriting">POSITIVE:</h5><ul>'
        negfx = '<div class="col-lg-12 neg-fx"><h5 class="handwriting">NEGATIVE:</h5><ul>'
        medfx = '<div class="col-lg-12 med-fx"><h5 class="handwriting">MEDICAL:</h5><ul>'

        if stRace == "hybrid":
            for x in jobj[strain]['effects']['positive']:
                posfx += "<li>" + x + "</li>"
            for x in jobj[strain]['effects']['negative']:
                negfx += "<li>" + x + "</li>"
            for x in jobj[strain]['effects']['medical']:
                medfx += "<li>" + x + "</li>"
            posfx += "</ul></div>"
            negfx += "</ul></div>"
            medfx += "</ul></div>"

            breed_hybrid = '<div class="col-lg-3 col-md-4 col-sm-6 portfolio-item"><div class="card h-100"><a href="/identifhigh/strain/' + str(strainid) + '"><img class="card-img-top" src="/identifhigh/static/img/hybrid_strain.png" alt="Hybrid"></a><div class="card-body"><h4 class="card-title"><a href="/identifhigh/strain/' + str(strainid) + '">'
            breed_hybrid += strain + '</a></h4><p class="card-text">' + the_desc + '</p>' + posfx + medfx + negfx + '</div></div></div>'

            html += breed_hybrid

    return html


###     GET _SATIVA_ STRAINS
def sativa_strains(jobj):
    html = ''
    dd = 0
    for strain in jobj:
        dd += 1
        strainid = jobj[strain]['id']
        if not jobj[strain]['desc']:
            the_desc = "None"
        else:
            the_desc = jobj[strain]['desc'][0:200] + "..."

        stRace = jobj[strain]['race']
        posfx = '<div class="col-lg-12 pos-fx"><h5 class="handwriting">POSITIVE:</h5><ul>'
        negfx = '<div class="col-lg-12 neg-fx"><h5 class="handwriting">NEGATIVE:</h5><ul>'
        medfx = '<div class="col-lg-12 med-fx"><h5 class="handwriting">MEDICAL:</h5><ul>'

        if stRace == "sativa":
            for x in jobj[strain]['effects']['positive']:
                posfx += "<li>" + x + "</li>"
            for x in jobj[strain]['effects']['negative']:
                negfx += "<li>" + x + "</li>"
            for x in jobj[strain]['effects']['medical']:
                medfx += "<li>" + x + "</li>"

            posfx += "</ul></div>"
            negfx += "</ul></div>"
            medfx += "</ul></div>"

            breed_sativa = '<div class="col-lg-3 col-md-4 col-sm-6 portfolio-item"><div class="card h-100"><a href="/identifhigh/strain/' + str(strainid) + '"><img class="card-img-top" src="/identifhigh/static/img/sativa_strain.png" alt="Sativa"></a><div class="card-body"><h4 class="card-title"><a href="/identifhigh/strain/' + str(strainid) + '">'
            breed_sativa += strain + '</a></h4><p class="card-text">' + the_desc + '</p>' + posfx + medfx + negfx + '</div></div></div>'

            html += breed_sativa

    return html


###     GET _ALL_ STRAINS
def get_all_strains(jobj):
    html = ''
    breed_indica = ''
    breed_sativa = ''
    breed_hybrid = ''
    posfx = ''
    negfx = ''
    medfx = ''

    dd = 0
    for strain in jobj:
        dd += 1
        strainid = jobj[strain]['id']
        stRace = jobj[strain]['race']

        if not jobj[strain]['desc']:
            the_desc = "None"
        else:
            the_desc = jobj[strain]['desc'][0:200] + '...'

        posfx = '<div class="col-lg-12 pos-fx"><h5 class="handwriting"><u>POSITIVE</u>:</h5><ul>'
        negfx = '<div class="col-lg-12 neg-fx"><h5 class="handwriting"><u>NEGATIVE</u>:</h5><ul>'
        medfx = '<div class="col-lg-12 med-fx"><h5 class="handwriting"><u>MEDICAL</u>:</h5><ul>'

        if stRace == "indica":
            breed_indica = '<div class="col-lg-3 col-md-4 col-sm-6 portfolio-item"><div class="card h-100"><a href="/identifhigh/strain/' + str(strainid) + '"><img class="card-img-top" src="/identifhigh/static/img/indica_strain.png" alt="Indica"></a><div class="card-body"><h4 class="card-title"><a href="/identifhigh/strain/' + str(strainid) + '">'

            for x in jobj[strain]['effects']['positive']:
                posfx += "<li>" + x + "</li>"
            posfx += "</ul></div>"
            for x in jobj[strain]['effects']['negative']:
                negfx += "<li>" + x + "</li>"
            negfx += "</ul></div>"
            for x in jobj[strain]['effects']['medical']:
                medfx += "<li>" + x + "</li>"
            medfx += "</ul></div>"

            breed_indica += strain + '</a></h4><p class="card-text">' + the_desc + '</p><span>' + posfx + medfx + negfx + '</span></div></div></div>'
            html += breed_indica

        if stRace == "hybrid":
            breed_hybrid = '<div class="col-lg-3 col-md-4 col-sm-6 portfolio-item"><div class="card h-100"><a href="/identifhigh/strain/' + str(strainid) + '"><img class="card-img-top" src="/identifhigh/static/img/hybrid_strain.png" alt="Hybrid"></a><div class="card-body"><h4 class="card-title"><a href="/identifhigh/strain/' + str(strainid) + '">'

            for x in jobj[strain]['effects']['positive']:
                posfx += "<li>" + x + "</li>"
            for x in jobj[strain]['effects']['negative']:
                negfx += "<li>" + x + "</li>"
            for x in jobj[strain]['effects']['medical']:
                medfx += "<li>" + x + "</li>"
            posfx += "</ul></div>"
            negfx += "</ul></div>"
            medfx += "</ul></div>"

            breed_hybrid += strain + '</a></h4><p class="card-text">' + the_desc + '</p><span>' + posfx + medfx + negfx + '</span></div></div></div>'
            html += breed_hybrid


        if stRace == "sativa":
            breed_sativa = '<div class="col-lg-3 col-md-4 col-sm-6 portfolio-item"><div class="card h-100"><a href="/identifhigh/strain/' + str(strainid) + '"><img class="card-img-top" src="/identifhigh/static/img/sativa_strain.png" alt="Sativa"></a><div class="card-body"><h4 class="card-title"><a href="/identifhigh/strain/' + str(strainid) + '">'

            for x in jobj[strain]['effects']['positive']:
                posfx += "<li>" + x + "</li>"
            posfx += "</ul></div>"

            for x in jobj[strain]['effects']['negative']:
                negfx += "<li>" + x + "</li>"
            negfx += "</ul></div>"

            for x in jobj[strain]['effects']['medical']:
                medfx += "<li>" + x + "</li>"
            medfx += "</ul></div>"

            breed_sativa += strain + '</a></h4><p class="card-text">' + the_desc + '</p><span>' + posfx + medfx + negfx + '</span></div></div></div>'
            html += breed_sativa

    return html



###     SEARCH BY _POSITIVE_ EFFECTS
def search_by_pos_fx(jobj, search_items):

    if len(search_items) == 0:
        return ""

    match_strains = []
    fx_pos = []

    count = 0
    html = ''

    for s in jobj:
        if not len(jobj[s]['effects']['positive']) == 0:
            for p in jobj[s]['effects']['positive']:
                fx_pos.append(p)

            set1 = set(fx_pos)
            itms = set(search_items)

            check_the_pos = all(p in set1 for p in itms)
            if check_the_pos is True:
                stRace = jobj[s]['race']
                strainid = jobj[s]['id']

                if not jobj[s]['desc']:
                    the_desc = "None"
                else:
                    the_desc = jobj[s]['desc'][0:200] + '...'

                posfx = '<div class="col-lg-12 pos-fx"><h5 class="handwriting">POSITIVE:</h5><ul>'
                negfx = '<div class="col-lg-12 neg-fx"><h5 class="handwriting">NEGATIVE:</h5><ul>'
                medfx = '<div class="col-lg-12 med-fx"><h5 class="handwriting">MEDICAL:</h5><ul>'

                for x in jobj[s]['effects']['positive']:
                    posfx += "<li>" + x + "</li>"
                for x in jobj[s]['effects']['negative']:
                    negfx += "<li>" + x + "</li>"
                for x in jobj[s]['effects']['medical']:
                    medfx += "<li>" + x + "</li>"
                posfx += "</ul></div>"
                negfx += "</ul></div>"
                medfx += "</ul></div>"

                if stRace == 'sativa':
                    satbreed = '<div class="col-lg-3 col-md-4 col-sm-12 portfolio-item"><div class="card h-100"><a href="/identifhigh/strain/' + str(strainid) + '"><img class="card-img-top" src="/identifhigh/static/img/sativa_strain.png" alt="Sativa"></a><div class="card-body"><h4 class="card-title"><a href="/identifhigh/strain/' + str(strainid) + '">' + s + '</a></h4><p class="card-text">' + the_desc + '</p>' + posfx + medfx + negfx + '</div></div></div>'
                    html += satbreed
                    match_strains.append(satbreed)

                elif stRace == 'indica':
                    indbreed = '<div class="col-lg-3 col-md-4 col-sm-12 portfolio-item"><div class="card h-100"><a href="/identifhigh/strain/' + str(strainid) + '"><img class="card-img-top" src="/identifhigh/static/img/indica_strain.png" alt="Indica"></a><div class="card-body"><h4 class="card-title"><a href="/identifhigh/strain/' + str(strainid) + '">' + s + '</a></h4><p class="card-text">' + the_desc + '</p>' + posfx + medfx + negfx + '</div></div></div>'
                    html += indbreed
                    match_strains.append(indbreed)

                elif stRace == 'hybrid':
                    hybreed = '<div class="col-lg-3 col-md-4 col-sm-12 portfolio-item"><div class="card h-100"><a href="/identifhigh/strain/' + str(strainid) + '"><img class="card-img-top" src="/identifhigh/static/img/hybrid_strain.png" alt="Hybrid"></a><div class="card-body"><h4 class="card-title"><a href="/identifhigh/strain/' + str(strainid) + '">' + s + '</a></h4><p class="card-text">' + the_desc + '</p>' + posfx + medfx + negfx + '</div></div></div>'
                    html += hybreed
                    match_strains.append(hybreed)

                count+=1

    return '<div class="row"><h4 class="handwriting">Matches <b><u>Positive</u></b> Effects</h4></div><div class="row">' + html + '</div>'


###     SEARCH BY _MEDICAL_ EFFECTS
def search_by_med_fx(jobj, search_items):

    if len(search_items) == 0:
        return ""

    match_strains = []
    fx_med = []
    count = 0
    html = ''

    for s in jobj:
        # iterate thru the MEDICAL effects.. but lets make sure there actually IS something to check for
        if len(jobj[s]['effects']['medical']) > 0:
            # NOT empty, there's something to display..
            for m in jobj[s]['effects']['medical']:
                fx_med.append(m)

            set1 = set(fx_med)
            itms = set(search_items)
            # POSITIVE EFFECTS
            check_med = all(pf in set1 for pf in itms)
            if check_med is True:
                stRace = jobj[s]['race']
                strainid = jobj[s]['id']

                if not jobj[s]['desc']:
                    the_desc = "None"
                else:
                    the_desc = jobj[s]['desc'][0:200] + '...'

                posfx = '<div class="col-lg-12 pos-fx"><h5 class="handwriting">POSITIVE:</h5><ul>'
                negfx = '<div class="col-lg-12 neg-fx"><h5 class="handwriting">NEGATIVE:</h5><ul>'
                medfx = '<div class="col-lg-12 med-fx"><h5 class="handwriting">MEDICAL:</h5><ul>'

                for x in jobj[s]['effects']['positive']:
                    posfx += "<li>" + x + "</li>"
                for x in jobj[s]['effects']['negative']:
                    negfx += "<li>" + x + "</li>"
                for x in jobj[s]['effects']['medical']:
                    medfx += "<li>" + x + "</li>"
                posfx += "</ul></div>"
                negfx += "</ul></div>"
                medfx += "</ul></div>"

                if stRace == 'sativa':
                    satbreed = '<div class="col-lg-3 col-md-4 col-sm-12 portfolio-item"><div class="card h-100"><a href="/identifhigh/strain/' + str(strainid) + '"><img class="card-img-top" src="/identifhigh/static/img/sativa_strain.png" alt="Sativa"></a><div class="card-body"><h4 class="card-title"><a href="/identifhigh/strain/' + str(strainid) + '">' + s + '</a></h4><p class="card-text">' + the_desc + '</p>' + posfx + medfx + negfx + '</div></div></div>'
                    html += satbreed
                    match_strains.append(satbreed)

                if stRace == 'indica':
                    indbreed = '<div class="col-lg-3 col-md-4 col-sm-12 portfolio-item"><div class="card h-100"><a href="/identifhigh/strain/' + str(strainid) + '"><img class="card-img-top" src="/identifhigh/static/img/indica_strain.png" alt="Sativa"></a><div class="card-body"><h4 class="card-title"><a href="/identifhigh/strain/' + str(strainid) + '">' + s + '</a></h4><p class="card-text">' + the_desc + '</p>' + posfx + medfx + negfx + '</div></div></div>'
                    html += indbreed
                    match_strains.append(indbreed)

                if stRace == 'hybrid':
                    hybreed = '<div class="col-lg-3 col-md-4 col-sm-12 portfolio-item"><div class="card h-100"><a href="/identifhigh/strain/' + str(strainid) + '"><img class="card-img-top" src="/identifhigh/static/img/hybrid_strain.png" alt="Sativa"></a><div class="card-body"><h4 class="card-title"><a href="/identifhigh/strain/' + str(strainid) + '">''' + s + '</a></h4><p class="card-text">' + the_desc + '</p>' + posfx + medfx + negfx + '</div></div></div>'
                    html += hybreed
                    match_strains.append(hybreed)

                count += 1

    return '<div class="row"><h4 class="handwriting">Matches <b><u>Medical</u></b> Effects</h4></div><div class="row">' + html + '</div>'




def get_strain_by_id(jobj, id):
    html = ''
    dd = 0
    for strain in jobj:
        dd += 1
        strainid = jobj[strain]['id']
        stRace = jobj[strain]['race']

        if int(strainid) == int(id):
            # found the matching strain
            if not jobj[strain]['desc']:
                the_desc = "None"
            else:
                the_desc = jobj[strain]['desc']

            posfx = '<div class="col-lg-3 d-flex mr-auto"><h5 class="handwriting">POSITIVE:</h5><br><ul>'
            negfx = '<div class="col-lg-3 d-flex mr-auto"><h5 class="handwriting">NEGATIVE:</h5><br><ul>'
            medfx = '<div class="col-lg-3 d-flex mr-auto"><h5 class="handwriting">MEDICAL:</h5><br><ul>'

            if stRace == "indica":
                for x in jobj[strain]['effects']['positive']:
                    posfx += "<li>" + x + "</li>"
                posfx += "</ul></div>"

                for x in jobj[strain]['effects']['negative']:
                    negfx += "<li>" + x + "</li>"
                negfx += "</ul></div>"

                for x in jobj[strain]['effects']['medical']:
                    medfx += "<li>" + x + "</li>"
                medfx += "</ul></div>"

                breed_indica = '''
                    <div class="row">
                    <div class="col-lg-3">
                    <img class="img-fluid rounded mb-4" src="/identifhigh/static/img/indica_strain.png" alt="Indica">
                    </div>
                    <div class="col-lg-9">
                    '''
                breed_indica += '<h2>' + strain + '</h2><p class="card-text">' + the_desc + '</p>'
                breed_indica += '</div>' + posfx + medfx + negfx + '</div>' + '</div>'

                html = breed_indica
                return html


            if stRace == "hybrid":
                for x in jobj[strain]['effects']['positive']:
                    posfx += "<li>" + x + "</li>"
                for x in jobj[strain]['effects']['negative']:
                    negfx += "<li>" + x + "</li>"
                for x in jobj[strain]['effects']['medical']:
                    medfx += "<li>" + x + "</li>"
                posfx += "</ul></div>"
                negfx += "</ul></div>"
                medfx += "</ul></div>"

                breed_hybrid = '''
                    <div class="row">
                    <div class="col-lg-3">
                    <img class="img-fluid rounded mb-4" src="/identifhigh/static/img/hybrid_strain.png" alt="Hybrid">
                    </div>
                    <div class="col-lg-9">
                    '''
                breed_hybrid += '<h2>' + strain + '</h2><p class="card-text">' + the_desc + '</p>'
                breed_hybrid += '</div>' + posfx + medfx + negfx + '</div>' + '</div>'

                html = breed_hybrid
                return html


            if stRace == "sativa":
                for x in jobj[strain]['effects']['positive']:
                    posfx += "<li>" + x + "</li>"
                for x in jobj[strain]['effects']['negative']:
                    negfx += "<li>" + x + "</li>"
                for x in jobj[strain]['effects']['medical']:
                    medfx += "<li>" + x + "</li>"
                posfx += "</ul></div>"
                negfx += "</ul></div>"
                medfx += "</ul></div>"

                breed_sativa = '''
                    <div class="row">
                    <div class="col-lg-3">
                    <img class="img-fluid rounded mb-4" src="/identifhigh/static/img/sativa_strain.png" alt="Sativa">
                    </div>
                    <div class="col-lg-9">
                    '''
                breed_sativa += '<h2>' + strain + '</h2><p class="card-text">' + the_desc + '</p>'
                breed_sativa += '</div>' + posfx + medfx + negfx + '</div>' + '</div>'

                html = breed_sativa
                return html

            return html
    return html






############################################

def populate_search_items(jobj, search_items):

    if len(search_items) == 0:
        return ""

    match_strains = list()
    fx_pos = list()
    fx_med = list()
    count = 0
    html = ''
    for s in jobj:
        if not len(jobj[s]['effects']['positive']) == 0:
            for p in jobj[s]['effects']['positive']:
                fx_pos.append(p)
        if not len(jobj[s]['effects']['medical']) == 0:
            for p in jobj[s]['effects']['medical']:
                fx_med.append(p)

            set1 = set(fx_pos)
            set2 = set(fx_med)
            itms = set(search_items)

            check_the_pos = all(p in itms for p in set1)
            check_the_med = all(p in itms for p in set2)

            print(check_the_med)
            print(check_the_pos)

            if check_the_pos is True:
                if check_the_med is True:

                    stRace = jobj[s]['race']

                    if not jobj[s]['desc']:
                        the_desc = "None"
                    else:
                        the_desc = jobj[s]['desc'][0:200] + '...'

                    posfx = '<div class="col-lg-12 pos-fx"><h4 class="handwriting">POSITIVE:</h4><ul>'
                    for x in jobj[s]['effects']['positive']:
                        posfx += "<li>" + x + "</li>"
                    posfx += "</ul></div>"
                    negfx = '<div class="col-lg-12 neg-fx"><h4 class="handwriting">NEGATIVE:</h4><ul>'
                    for x in jobj[s]['effects']['negative']:
                        negfx += "<li>" + x + "</li>"
                    negfx += "</ul></div>"
                    medfx = '<div class="col-lg-12 med-fx"><h4 class="handwriting">MEDICAL:</h4><ul>'
                    for x in jobj[s]['effects']['medical']:
                        medfx += "<li>" + x + "</li>"
                    medfx += "</ul></div>"

                    if stRace == 'sativa':
                        satbreed = '<div class="col-lg-3 col-md-4 col-sm-12 portfolio-item"><div class="card h-100"><a href="#"><img class="card-img-top" src="../static/img/sativa_strain.png" alt="Sativa"></a><div class="card-body"><h4 class="card-title"><a href="#">' + s + '</a></h4><p class="card-text">' + the_desc + '</p>' + posfx + medfx + negfx + '</div></div></div>'
                        html += satbreed

                        match_strains.append(satbreed)

                    elif stRace == 'indica':
                        indbreed = '<div class="col-lg-3 col-md-4 col-sm-12 portfolio-item"><div class="card h-100"><a href="#"><img class="card-img-top" src="../static/img/indica_strain.png" alt="Sativa"></a><div class="card-body"><h4 class="card-title"><a href="#">' + s + '</a></h4><p class="card-text">' + the_desc + '</p>' + posfx + medfx + negfx + '</div></div></div>'
                        html += indbreed

                        match_strains.append(indbreed)

                    elif stRace == 'hybrid':
                        hybreed = '<div class="col-lg-3 col-md-4 col-sm-12 portfolio-item"><div class="card h-100"><a href="#"><img class="card-img-top" src="../static/img/hybrid_strain.png" alt="Sativa"></a><div class="card-body"><h4 class="card-title"><a href="#">' + s + '</a></h4><p class="card-text">' + the_desc + '</p>' + posfx + medfx + negfx + '</div></div></div>'
                        html += hybreed

                        match_strains.append(hybreed)
                    else:
                        hybreed = '<div class="col-lg-3 col-md-4 col-sm-12 portfolio-item"><div class="card h-100"><a href="#"><img class="card-img-top" src="../static/img/hybrid_strain.png" alt="Sativa"></a><div class="card-body"><h4 class="card-title"><a href="#">' + s + '</a></h4><p class="card-text">' + the_desc + '</p>' + posfx + medfx + negfx + '</div></div></div>'
                        html += hybreed

                        match_strains.append(hybreed)

                    count+=1
        fx_pos.clear()
        fx_med.clear()

    return '<h4 class="handwriting">Matches <b><u>Positive</u></b> Effects</h4>' + html



def check_for_effect(jobj, search_items):
    match_strains = list()
    fx_pos = list()
    count = 0
    html = ''
    print("CHECKING FOR EFFECT....")
    for s in jobj:
        for p in jobj[s]['effects']['positive']:
            fx_pos.append(p)

    set1 = set(fx_pos)
    itms = set(search_items)
    # POSITIVE EFFECTS
    if all(p in itms for p in set1):
        print("ALL MATCHED - positive")

    return "ALL MATCHED"