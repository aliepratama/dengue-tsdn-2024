from flask import render_template, request, url_for, flash, redirect
from PIL import Image
import io, os

def get_scan():
    return render_template('scan.html')

def post_scan():
    allowed_extensions = {'.png', '.jpg', '.jpeg'}
    image_file = request.files.get('image_url')
    if not image_file:
        flash('No file uploaded.', 'error')
        return redirect(url_for('scan'))
    if not any(image_file.filename.lower().endswith(ext) for ext in allowed_extensions):
        flash('Invalid file format. Please upload a .png or .jpg file.', 'error')
        return redirect(url_for('scan'))
    image = Image.open(io.BytesIO(image_file.read()))
    if image.width > 800 or image.height > 800:
        flash('Image resolution exceeds 800x800 pixels.', 'error')
        return redirect(url_for('scan'))
    if image_file:
        image = image.resize((256, 256))
        image = image.convert('RGB')
        image.save(os.path.join(os.getcwd(), 'dengue/static/dist/images/temp.jpg'))
        return result(url_for('static', filename='dist/images/temp.jpg'))
    return render_template('scan.html')

def sample(id:int = 1):
    return result(url_for('static', filename=f'dist/images/sample{id}.jpg'))

def result(image):
    return render_template('result.html', preview=image)
