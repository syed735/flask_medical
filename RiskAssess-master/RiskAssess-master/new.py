from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Define data for the table
data = [['Patient Name', 'Patient Age', 'Test Results', 'Recommended Advice'],
        ['John Doe', '35', 'Positive', 'Quarantine for 14 days'],
        ['Jane Smith', '42', 'Negative', 'No further action needed'],
        ['Bob Johnson', '58', 'Positive', 'Consult a doctor']]

# Set up the PDF document
doc = SimpleDocTemplate("patient_table.pdf", pagesize=letter)
styles = getSampleStyleSheet()

# Define the table style
table_style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 14),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
    ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 12),
    ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
])

# Create the table and apply the style
table = Table(data)
table.setStyle(table_style)

# Add the table to the PDF document and save it
doc.build([table])
