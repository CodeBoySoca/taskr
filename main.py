from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

class Listings(db.Model):
    id = db.Column()
    description  = db.Column(db.Text)
    company_id = db.Column(db.Integer(), db.ForeignKey('companies.id'))
    title = db.Column(db.String(150))
    requirements = db.Column(db.Text())
    responsibilities = db.Column(db.Text())
    wage = db.Column(db.Integer())
    location = db.Column(db.String(255))
    job_type = db.Column(db.String(150))
    date_added = db.Column(db.Datetime())

class Applicants(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(150))
    birthdate = db.Column(db.Datetime)
    image = db.Column(db.String(255))
    resume = db.column(db.String(255))
    date_added = db.column(db.Datetime())
    title = db.Column(db.String(200))
    state = db.Column(db.String(150))
    city = db.Column(db.String(200))
    
class Employer(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(150))
    password = db.Column(db.String(150))
    date_added = db.Column(db.Datetime())
    
class Companies(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.Text())
    industry = db.Column(db.String(200))
    address = db.Column(db.String(255))
    city = db.Column(db.String(255))
    zip = db.column(db.String(100))
    image = db.Column(db.String(255))
    employer_id = db.Column(db.ForeignKey('employer.id'))
    date_added = db.column(db.Datetime())

@app.route('/')
def homepage():
    pass

@app.route('/register')
def register():
    pass

@app.route('/logout')
def logout():
    pass

@app.route('/sign-in')
def signin():
    pass

@app.route('/top-careers')
def top_careers():
    pass

@app.route('/search')
def search():
    pass

@app.route('/jobs')
def jobs():
    pass

@app.route('/account/<account_id>')
def account():
    pass

@app.route('/profile')
def profile():
    pass

@app.route('/listings/<listing_id>')
def listings():
    pass

@app.route('/applicants/<applicant_id>')
def applicants():
    pass

@app.route('/add/listing')
def add_listing():
    pass


if __name__ == '__main__':
    app.run()