from flask import render_template, request, redirect, url_for, Response
from dengue.utils.stepper import Stepper


def get_form() -> str:
    print(Stepper.get_step())
    return render_template('form.html', step=Stepper.get_step())


def post_form() -> str | Response:
    if request.form.get('s'):
        Stepper.command(request.form['s'])
        return redirect(url_for('form'))
    return render_template('form.html')
