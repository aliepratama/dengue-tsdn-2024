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

    df_normalization = pd.DataFrame({
        'dengue.days': int(request.form.get('DDEMA')) if is_demam else 0,
        'current_temp': float(request.form.get('SUHUN')) * 9 / 5 + 32 if is_demam else 0,
        'dengue.wbc': float(request.form.get('JWBCS')) if is_uji_lab else 0,
        'dengue.hemoglobin': float(request.form.get('HEMOG')) if is_uji_lab else 0,
        'dengue._hematocri': int(request.form.get('HEMAT')) if is_uji_lab else 0,
        'dengue.platelet': int(request.form.get('JPLAT')) if is_uji_lab else 0,
    }, index=[0])
    normalizer = joblib.load(os.path.join(os.getcwd(), 'dengue/models', 'normalizer.joblib'))
    df_normalization = pd.DataFrame(normalizer(df_normalization), columns=df_normalization.columns)

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
            'dengue.days': df_normalization['dengue.days'], 
            'current_temp': df_normalization['current_temp'],
        }, index=[0])

    if is_uji_lab:
        df_lab = pd.DataFrame({
            'dengue.wbc': df_normalization['dengue.wbc'],
            'dengue.hemoglobin': df_normalization['dengue.hemoglobin'],
            'dengue._hematocri': df_normalization['dengue._hematocri'],
            'dengue.platelet': df_normalization['dengue.platelet'],
        }, index=[0])

    print(df_normalization)

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
