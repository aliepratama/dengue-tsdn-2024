from flask import render_template, request, redirect, url_for, Response


def get_form(id: int) -> str:
    if request.args.get('a'):
        type_survey = request.args.get('a')
        return render_template('form.html', step=id, type_survey=type_survey)
    return render_template('form.html', step=id)


def post_form() -> str | Response:
    return redirect(url_for('form'))

