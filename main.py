from fastapi import FastAPI, Response
from pydantic import BaseModel
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from io import BytesIO
from typing import Optional

app = FastAPI()

class ECGCFormData(BaseModel):
    policyholder: Optional[str] = ""
    policy_number: Optional[str] = ""
    policy_from: Optional[str] = ""
    policy_to: Optional[str] = ""
    max_liability: Optional[str] = ""
    shipment_declaration: Optional[str] = ""
    buyer_name: Optional[str] = ""
    buyer_address: Optional[str] = ""
    buyer_city: Optional[str] = ""
    buyer_country: Optional[str] = ""
    buyer_phone: Optional[str] = ""
    buyer_email: Optional[str] = ""
    contact_person: Optional[str] = ""
    buyer_registration: Optional[str] = ""
    buyer_fax: Optional[str] = ""
    buyer_website: Optional[str] = ""
    buyer_mobile: Optional[str] = ""
    buyer_vat: Optional[str] = ""
    bank_name: Optional[str] = ""
    bank_address: Optional[str] = ""
    bank_city: Optional[str] = ""
    bank_country: Optional[str] = ""
    bank_phone: Optional[str] = ""
    bank_email: Optional[str] = ""
    bank_fax: Optional[str] = ""
    swift_code: Optional[str] = ""
    buyer_account: Optional[str] = ""
    goods_description: Optional[str] = ""
    export_country: Optional[str] = ""
    destination_country: Optional[str] = ""
    lc_amount: Optional[str] = ""
    lc_terms: Optional[str] = ""
    ship_month: Optional[str] = ""
    ship_value: Optional[str] = ""
    current_credit: Optional[str] = ""
    current_terms: Optional[str] = ""
    revised_credit: Optional[str] = ""
    revised_terms: Optional[str] = ""
    cheque_no: Optional[str] = ""
    cheque_date: Optional[str] = ""
    cheque_for: Optional[str] = ""
    cheque_drawn_on: Optional[str] = ""
    cheque_place: Optional[str] = ""
    cheque_form_date: Optional[str] = ""
    cheque_amount: Optional[str] = ""
    date_of_shipment: Optional[str] = ""
    value: Optional[str] = ""
    term_of_payment: Optional[str] = ""
    payment_due_date: Optional[str] = ""
    realisation_date: Optional[str] = ""
    reason_delay: Optional[str] = ""

@app.get("/")
def root():
    return {"message": "ECGC PDF Generator is live. Use POST /generate-ecgc-pdf/"}

@app.post("/generate-ecgc-pdf/")
def generate_ecgc_pdf(data: ECGCFormData):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    c.setFont("Times-Roman", 14)                 # 📏 Font size for legibility
    c.setFillColorRGB(0, 0, 0)                   # 🔴 Bright red text for visibility

    # Page 1
    c.drawImage("C:/Users/Lenovo/OneDrive/Desktop/combinedpdf/1.png", 0, 0, width=width, height=height)
    c.drawString(250, 330, data.policyholder or "")
    c.drawString(170, 230, data.policy_number or "")
    c.drawString(190, 205, data.policy_from or "")
    c.drawString(300, 205, data.policy_to or "")
    c.drawString(270, 165, data.max_liability or "")
    c.drawString(280, 120, data.shipment_declaration or "")
    c.showPage()

    # Page 2
    c.drawImage("C:/Users/Lenovo/OneDrive/Desktop/combinedpdf/2.png", 0, 0, width=width, height=height)
    c.drawString(220, 830, data.buyer_name or "")
    c.drawString(150, 810, data.buyer_address or "")
    c.drawString(130, 780, data.buyer_city or "")
    c.drawString(380, 780, data.buyer_country or "")
    c.drawString(400, 770, data.buyer_fax or "")
    c.drawString(170, 770, data.buyer_phone or "")
    c.drawString(380, 755, data.buyer_website or "")
    c.drawString(400, 740, data.buyer_mobile or "")
    c.drawString(125, 755, data.buyer_email or "")
    c.drawString(175, 740, data.contact_person or "")
    c.drawString(200, 725, data.buyer_registration or "")
    c.drawString(370, 725, data.buyer_vat or "")
    c.drawString(125, 680, data.bank_name or "")
    c.drawString(150, 665, data.bank_address or "")
    c.drawString(120, 640, data.bank_city or "")
    c.drawString(380, 640, data.bank_country or "")
    c.drawString(400, 625, data.bank_fax or "")
    c.drawString(160, 625, data.bank_phone or "")
    c.drawString(125, 610, data.bank_email or "")
    c.drawString(410, 590, data.swift_code or "")
    c.drawString(165, 595, data.buyer_account or "")
    c.drawString(200, 555, data.goods_description or "")
    c.drawString(340, 525, data.export_country or "")
    c.drawString(265, 495, data.destination_country or "")
    c.drawString(170, 440, data.lc_amount or "")
    c.drawString(390, 435, data.lc_terms or "")
    c.drawString(140, 390, data.ship_month or "")
    c.drawString(340, 390, data.ship_value or "")
    c.drawString(180, 350, data.current_credit or "")
    c.drawString(390, 350, data.current_terms or "")
    c.drawString(180, 275, data.revised_credit or "")
    c.drawString(175, 275, data.revised_terms or "")
    c.drawString(108, 155, data.date_of_shipment or "")
    c.drawString(180, 155, data.value or "")
    c.drawString(250, 155, data.term_of_payment or "")
    c.drawString(310, 155, data.payment_due_date or "")
    c.drawString(380, 155, data.realisation_date or "")
    c.drawString(450, 155, data.reason_delay or "")
    c.showPage()

    # Page 3
    c.drawImage("C:/Users/Lenovo/OneDrive/Desktop/combinedpdf/3.png", 0, 0, width=width, height=height)
    c.drawString(160, 555, data.cheque_no or "")
    c.drawString(260, 555, data.cheque_date or "")
    c.drawString(400, 555, data.cheque_for or "")
    c.drawString(140, 540, data.cheque_drawn_on or "")
    c.drawString(110, 515, data.cheque_place or "")
    c.drawString(100, 500, data.cheque_form_date or "")
    c.drawString(260, 500, data.cheque_amount or "")

    c.save()
    buffer.seek(0)
    return Response(
        content=buffer.read(),
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=ecgc_form_144A.pdf"}
    )
