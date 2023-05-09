# დავალება #38 - CS50 Shirtificate
from fpdf import FPDF

user_name = str(input("Enter your name: "))
shirt_txt = (f"{user_name} took CS50")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()

pdf.set_font("Arial", "B", 50)
pdf.cell(0, 30, "CS50 Shirtificate", align="C")

pdf.image("shirtificate.png", x=5, y=70, w=200)

pdf.set_font("Arial", "B", 30)
pdf.set_text_color(255, 255, 255)
pdf.cell(-180, 250, txt=shirt_txt, align="C")


pdf.output("shirtificate.pdf")