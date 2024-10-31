from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, EmailStr
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = FastAPI()
# Define a Pydantic model for email content
class EmailBodySchema(BaseModel):
    body: str
# SMTP configuration
SMTP_SERVER = "smtp.gmail.com"  # e.g., smtp.gmail.com
SMTP_PORT = 587  # Port for TLS
SMTP_USERNAME = "dbstestapexemail@gmail.com"
SMTP_PASSWORD = "vqmo sxxh fmrs yvcm"
RECIPIENT_EMAIL='t.junliang1214@gmail.com'

@app.post("/send-email-card-application/")
async def send_email(email: EmailBodySchema, body_text: str = Query(..., description="Body text of the email")):
    try:
        # Setup MIME
        message = MIMEMultipart()
        message["From"] = SMTP_USERNAME
        message["To"] = email.email_to
        message["Subject"] = 'Card Application'
        message.attach(MIMEText(body_text, "plain"))

        # Connect to SMTP server and send email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, email.email_to, message.as_string())
        server.quit()

        return {"message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.post("/send-email-otp/")
async def send_email(body: EmailBodySchema):
    try:
        # Setup MIME
        message = MIMEMultipart()
        message["From"] = SMTP_USERNAME
        message["To"] = RECIPIENT_EMAIL
        message["Subject"] = 'OTP'
        message.attach(MIMEText(body.body, "plain"))

        # Connect to SMTP server and send email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, RECIPIENT_EMAIL, message.as_string())
        server.quit()

        return {"message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))