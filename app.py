
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# ---- MAIL CONFIG ----
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'hopephysician90@gmail.com'  # your Gmail
app.config['MAIL_PASSWORD'] = 'outu iexx yeca yarc'     # the 16-char app password
app.config['MAIL_DEFAULT_SENDER'] = ('Hope Physicians', 'hopephysician90@gmail.com')

mail = Mail(app)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html', title="Services")

@app.route('/resources')
def resources():
    return render_template('resources.html', title="Resources")

@app.route('/portal')
def portal():
    return render_template('portal.html', title="Portal")

@app.route('/doctors')
def doctors():
    return render_template('doctors.html', title="Doctors")

@app.route('/departments')
def departments():
    return render_template('departments.html', title="Departments")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")



@app.route('/submit_appointment', methods=['POST'])
def submit_appointment():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    department = request.form.get('department')
    message = request.form.get('message')

    if not name or not email or not phone or not department:
        flash("Please fill in all required fields.", "danger")
        return redirect(url_for('home'))

    subject = f"New Appointment Request: {name}"
    body = f"""
New appointment request:

Name: {name}
Email: {email}
Phone: {phone}
Department: {department}
Message: {message}
"""

    try:
        msg = Message(subject, recipients=['hopephysician90@gmail.com'], body=body)
        mail.send(msg)
        flash("Appointment request sent successfully!", "success")
    except Exception as e:
        print(e)
        flash("Failed to send appointment. Please try again later.", "danger")

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
