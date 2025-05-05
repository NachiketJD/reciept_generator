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

@app.route('/generate', methods=['POST'])
def generate_pdf():
    title = request.form.get("title")
    items = request.form.getlist("item[]")
    subtotal = request.form.get("subtotal")
    discount = request.form.get("discount")
    total = request.form.get("total")

data = [["Date", "Name", "Subscription", "Price (Rs.)"]]

for item in items:
        fields = item.split(",")
        if len(fields) == 4:
            data.append(fields)