from flask import render_template, request, redirect, url_for, Response
import joblib, os
import pandas as pd


def get_form(id: int) -> str:
    if request.args.get('a'):
        type_survey = request.args.get('a')
        return render_template('form.html', step=id, type_survey=type_survey)
    return render_template('form.html', step=id)


def post_form() -> str | Response:
    is_human = request.form.get('PNAMA')
    is_demam = request.form.get('KDEMA') == 'Iya'
    is_uji_lab = request.form.get('ULABO') == 'Sudah'

    general_symptoms = {
        'SKPLA': 'dengue.servere_headche',
        'NYMAT': 'dengue.pain_behind_the_eyes',
        'NYSEN': 'dengue.joint_muscle_aches',
        'RSMUL': 'dengue.metallic_taste_in_the_mouth',
        'HINFM': 'dengue.appetite_loss',
        'NYPER': 'dengue.addominal_pain',
        'MUMUN': 'dengue.nausea_vomiting',
        'MDIAR': 'dengue.diarrhoea'
    }
    df_general = pd.DataFrame({
        symptom: 1 if request.form.get(code) == 'Iya' else 0
        for code, symptom in general_symptoms.items()
    }, index=[0])

    if is_demam:
        df_fever = pd.DataFrame({
            'dengue.days': int(request.form.get('DDEMA')), 
            'current_temp': float(request.form.get('SUHUN')),
        }, index=[0])

    if is_uji_lab:
        df_lab = pd.DataFrame({
            'dengue.wbc': float(request.form.get('JWBCS')),
            'dengue.hemoglobin': float(request.form.get('HEMOG')),
            'dengue._hematocri': int(request.form.get('HEMAT')),
            'dengue.platelet': int(request.form.get('JPLAT')),
        }, index=[0])
    
    if is_demam and is_uji_lab:
        model = joblib.load(os.path.join(os.getcwd(), 'dengue/models', 'all_data.joblib'))
        prediction = model.predict(pd.concat([df_fever, df_lab, df_general], axis=1))
        return render_template('form.html', step=2, prediction=prediction[0])
    elif is_demam and not is_uji_lab:
        model = joblib.load(os.path.join(os.getcwd(), 'dengue/models', 'fever_general_data.joblib'))
        prediction = model.predict(pd.concat([df_fever, df_general], axis=1))
        return render_template('form.html', step=2, prediction=prediction[0])
    elif not is_demam and is_uji_lab:
        model = joblib.load(os.path.join(os.getcwd(), 'dengue/models', 'lab_general_data.joblib'))
        prediction = model.predict(pd.concat([df_lab, df_general], axis=1))
        return render_template('form.html', step=2, prediction=prediction[0])
    else:
        model = joblib.load(os.path.join(os.getcwd(), 'dengue/models', 'only_general_data.joblib'))
        prediction = model.predict(df_general)
        return render_template('form.html', step=2, prediction=prediction[0])
