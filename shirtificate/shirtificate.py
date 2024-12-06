from fpdf import FPDF


pdf = FPDF()
pdf.add_page(orientation="P", format="A4")
pdf.set_font('helvetica', size=12)
pdf.cell(text="hello world")
pdf.output("hello_world.pdf")

if __name__ == "__main__":
    main()

pdf = PDF()

