from fpdf import FPDF

def main():
    pdf = FPDF()
    pdf.add_page()
    pdf.image("https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png", x="C")
    pdf.set_font("helvetica", style="B", size=24)
    pdf.set_title("CS50 Shirtificate")
    pdf.set_author("Audrius Juknevicius")
    pdf.output("shirtificate.pdf")



if __name__ == "__main__":
    main()
