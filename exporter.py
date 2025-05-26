from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import os

def export_schedule_to_pdf(schedule, folder="exported_plans"):
    os.makedirs(folder, exist_ok=True)

    for class_name, days in schedule.items():
        filename = os.path.join(folder, f"{class_name}_plan.pdf")
        doc = SimpleDocTemplate(filename, pagesize=A4)
        elements = []

        table_data = [["Dzień", "Godzina", "Przedmiot", "Nauczyciel", "Sala"]]
        for day, lessons in days.items():
            for subject, teacher, room, time in lessons:
                table_data.append([day, time, subject, teacher, room])

        
        table = Table(table_data, colWidths=[80, 80, 140, 140, 60])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#cccccc")),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ]))

        elements.append(table)
        doc.build(elements)
        print(f"📄 Zapisano PDF: {filename}")
