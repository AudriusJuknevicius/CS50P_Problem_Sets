from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Setting font: helvetica bold 24
        self.set_font("helvetica", style="B", size=24)
        # Calculating width of title and setting cursor position:
        width = self.get_string_width(self.title) + 6
        self.set_x((210 - width) / 2)
        # Setting colors for text:
        self.set_text_color(255,255,255)
        # Setting thickness of the frame (1 mm)
        self.set_line_width(3)
        # Printing title:
        self.cell(
            width,
            9,
            self.title,
            border=1,
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
            fill=True,
        )
        # Performing a line break:
        self.ln(10)


    def chapter_title(self, num, label):
        # Setting font: helvetica 12
        self.set_font("helvetica", size=12)
        # Setting background color
        self.set_fill_color(0, 0, 0)
        # Printing chapter name:
        self.cell(
            0,
            6,
            f"Chapter {num} : {label}",
            new_x="LMARGIN",
            new_y="NEXT",
            align="L",
            fill=True,
        )
        # Performing a line break:
        self.ln(4)

    def chapter_body(self, filepath):
        # Reading text file:
        with open(filepath, "rb") as fh:
            txt = fh.read().decode("latin-1")
        # Setting font: Times 12
        self.set_font("Times", size=12)
        # Printing justified text:
        self.multi_cell(0, 5, txt)
        # Performing a line break:
        self.ln()
        # Final mention in italics:
        self.set_font(style="I")
        self.cell(0, 5, "(end of excerpt)")

    def print_chapter(self, num, title, filepath):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(filepath)


pdf = PDF()
pdf.set_title("CS50 Shirtificate")
pdf.set_author("Audrius Juknevicius")
pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
