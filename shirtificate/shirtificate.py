from fpdf import FPDF

def main():
    pdf = FPDF()
    pdf.add_page()
    pdf.image("https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png")
    pdf.set_title("CS50 Shirtificate", size=24)
    pdf.set_author("Audrius Juknevicius")
    pdf.output("shirtificate.pdf")



if __name__ == "__main__":
    main()
