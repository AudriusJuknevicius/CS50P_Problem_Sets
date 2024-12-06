from fpdf import FPDF

def main():
    name = input("Name: ")
    pdf = FPDF()
    pdf.add_page()

    pdf.set_title("CS50 Shirtificate")

    pdf.set_font("helvetica", style="B", size=42)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 50, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")

    pdf.image("https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png", x="C",y=+70)

    pdf.set_font("helvetica", style="B", size=24)
    #pdf.set_text_color(255, 255, 255)
    pdf.cell(align="C", text=name + " took CS50")

    pdf.output("shirtificate.pdf")



if __name__ == "__main__":
    main()
