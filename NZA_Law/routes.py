from NZA_Law import app, db, Message, mail
from flask import render_template, request, redirect, url_for

# Forms import
from NZA_Law.forms import CaseNotesForm #[INSERT FORMS HERE]

# Models import
from NZA_Law.models import Case#[INSERT MODELS HERE]

# Flask Login import
from flask_login import login_required, login_user, current_user, logout_user

# Home route - Josh
@app.route('/')
def home():
    return render_template("index.html")

# Register route - Mike


# Create Case route - Leland
@app.route('/create_cases', methods=['GET', "POST"])
@login_required
def create_cases():
    form = CaseNotesForm()
    if request.method == 'POST' and form.validate():
        caseNum = form.caseNum.data
        caseNotes = form.caseNotes.data
        lawyer_id = current_lawyer.id 
        print("\n", caseNum, caseNotes)
        case = case(caseNum, caseNotes, lawyer_id)

        db.session.add(case)
        db.session.commit()
        return redirect(url_for('create_cases'))
    cases = Case.query.all()
    return render_template('create_cases.html', form=form, cases=cases)

@app.route('/cases/<int:case_id>')


# Retrieve Case route - Stephanie


# Updating Case route - Stephanie


# Deleting Case route - Stephanie


# Login route - Josh
@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        logged_user = Lawyer.query.filter(Lawyer.email == email).first()
        if logged_user and check_password_hash(logged_user.passowrd, password):
            login_user(logged_user)
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))
    
    return render_template('login.html',form=form)


# Logout route - Josh
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))