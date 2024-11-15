from flask import render_template
import os, json


def get_home():
    heatmap = json.load(open(os.path.join(os.getcwd(), 'dengue/models/heatmap_geo.json')))
    return render_template('index.html', map_plot=heatmap)
