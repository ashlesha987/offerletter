from fpdf import FPDF
import datetime
class PDF(FPDF):
    def header(self):
        # Logo
        self.image('woir logo.jpeg', 10, 5, w=60, h=40)
        objDate = datetime.strptime(strDate, '%m/%d/%y')
        self.set_font('Times','B',14)
        self.cell(150)
        self.cell(30, 10, datetime.strftime(objDate,'%b %d, %Y'), 1, 0, 'C')
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 0,
                  'Flat No. # 105, Gayathri Heights,Jubilee Enclave,HITEC City, Hyderabad,Telangana,India,Phone: +91-9555295300,E-mail: info@woir.in',
                  0, 0, 'C')

# Instantiation of inherited class
pdf= PDF()
pdf.t_margin= pdf.t_margin * 5
pdf.l_margin= pdf.l_margin * 2.5
pdf.alias_nb_pages()
pdf.add_page()
# Font Size
pdf.set_font('Times', '', 12.0)
# First part of the letter body
para1 = """In reference to your application we would like to congratulate you on being selected for an \
internship with WOIR Software India Pvt. Ltd., based at Hyderabad. Your training is scheduled \
as follows - 
"""
# Effective page width
effective_page_width = pdf.w - 2 * pdf.l_margin
# Placing first part of paragraph
try:
    pdf.multi_cell(effective_page_width, 5, para1)
except:
    print ("error")

pdf.ln(5)

pdf.output('trybody.pdf', 'F')