from flask import Flask, request, send_file, render_template
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import tempfile

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')