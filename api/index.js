

const express = require("express");
const nodemailer = require("nodemailer");
const bodyParser = require("body-parser");

const app = express(); 

app.use(bodyParser.json());

// SMTP Configuration
const SMTP_SERVER = "smtp.gmail.com";
const SMTP_PORT = 587;
const SMTP_USERNAME = "dbstestapexemail@gmail.com";
const SMTP_PASSWORD = "vqmo sxxh fmrs yvcm";
const RECIPIENT_EMAIL = "t.junliang1214@gmail.com";

// Nodemailer Transporter Setup
const transporter = nodemailer.createTransport({
    host: SMTP_SERVER,
    port: SMTP_PORT,
    secure: false, // true for port 465, false for other ports
    auth: {
        user: SMTP_USERNAME,
        pass: SMTP_PASSWORD,
    },
});

// Send email for card application
app.post("/send-email-card-application", async (req, res) => {
    const { body } = req.body;

    try {
        await transporter.sendMail({
            from: SMTP_USERNAME,
            to: RECIPIENT_EMAIL,
            subject: "Card Application",
            text: body,
        });

        res.json({ message: "Email sent successfully" });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Send email for OTP
app.post("/send-email-otp", async (req, res) => {
    const { body } = req.body;

    try {
        await transporter.sendMail({
            from: SMTP_USERNAME,
            to: RECIPIENT_EMAIL,
            subject: "OTP",
            text: body,
        });

        res.json({ message: "Email sent successfully" });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});
// Simple Route 
app.get("/", (req, res) => { 
res.send("Welcome to the learning space."); 
}); 
let port = 3001; 
app.listen(port, () => { 
console.log(`⚡ Sever running on http://localhost:${port}`); 
}); 