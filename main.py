from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
import datetime

load_dotenv('.env')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_URI')
db = SQLAlchemy(app)


class Applicants(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(150))
    birthdate = db.Column(db.DateTime)
    image = db.Column(db.String(255))
    resume = db.Column(db.String(255))
    date_added = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    title = db.Column(db.String(200))
    state = db.Column(db.String(150))
    city = db.Column(db.String(200))
    
class Employer(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(150))
    password = db.Column(db.String(150))
    date_added = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    
class Companies(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.Text())
    industry = db.Column(db.String(200))
    address = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.column(db.String(150))
    image = db.Column(db.String(255))
    employer_id = db.Column(db.ForeignKey('employer.id'))
    date_added = db.Column(db.DateTime, default=datetime.datetime.utcnow)


class Listings(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    description  = db.Column(db.Text)
    company_id = db.Column(db.Integer(), db.ForeignKey('companies.id'))
    companies = db.relationship('Companies', backref="listings", lazy=True)
    title = db.Column(db.String(150))
    requirements = db.Column(db.Text())
    responsibilities = db.Column(db.Text())
    wage = db.Column(db.Integer())
    location = db.Column(db.String(255))
    job_type = db.Column(db.String(150))
    date_added = db.Column(db.DateTime, default=datetime.datetime.utcnow)

@app.route('/')
def homepage():
    return render_template('index.html')

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
    return render_template('careers.html')

@app.route('/search/<job>')
def search():
    pass

@app.route('/jobs')
def jobs():
    jobs = Listings.query.all()
    return render_template('jobs.html', listings=jobs, listing_count=len(jobs))

@app.route('/employers')
def employers():
    return render_template('employers.html')

@app.route('/account/<account_id>')
def account():
    pass

@app.route('/profile')
def profile():
    pass

@app.route('/listings/<listing_id>')
def listings(listing_id):
    listing = Listings.query.get(listing_id)
    return render_template('listing.html', listing=listing)

@app.route('/apply/<id>')
def apply(id):
    listing = Listings.query.get(id)
    return render_template('apply.html', listing=listing)


@app.route('/save/listing/<id>')
def save_listing():
    pass

@app.route('/applicants/<applicant_id>')
def applicants():
    pass

@app.route('/add/listing')
def add_listing():
    pass


if __name__ == '__main__':
    app.run()