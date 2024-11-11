from flask import render_template, request
from dengue.utils.stepper import Stepper


def get_form() -> str:
    return render_template('form.html')


def post_form() -> str:
    if request.args.get('s'):
        Stepper.command(request.args['s'])
    return render_template('form.html', step=Stepper.get_step())
