from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('helvetica', size=12)
pdf.cell(text="hello world")
pdf.output("hello_world.pdf")

def add_page(self, orientation="P", format="A4")
    self._add_page = orientation, format
