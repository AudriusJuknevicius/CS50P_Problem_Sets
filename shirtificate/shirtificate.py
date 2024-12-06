from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Setting font: helvetica bold 24
        self.set_font("helvetica", style="B", size=24)
        # Setting colors for text:
        self.set_text_color(255,255,255)
        # Setting thickness of the frame (1 mm)
        self.set_line_width(3)




pdf = PDF()
pdf.add_page()
pdf.image("https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png")
pdf.set_title("CS50 Shirtificate")
pdf.set_author("Audrius Juknevicius")
pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
