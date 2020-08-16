from NZA_Law import app, db, Message, mail
from flask import render_template, request, redirect, url_for

# Forms import
from NZA_Law.forms import CaseNotesForm, LoginForm, LawyerInfoForm #[INSERT FORMS HERE]

# Models import
from NZA_Law.models import Case, Lawyer, check_password_hash #[INSERT MODELS HERE]

# Flask Login import
from flask_login import login_required, login_user, current_user, logout_user

# Home route - Josh
@app.route('/')
def home():
    return render_template("index.html")

# Register route - Mike
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = LawyerInfoForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        print("\n", username, password, email)
        user = Lawyer(username, email, password)
        db.session.add(user)
        db.session.commit()
    
    return render_template("register.html", form=form)

# Create Case route - Leland
@app.route('/create_cases', methods=['GET', "POST"])
@login_required
def create_cases():
    form = CaseNotesForm()
    if request.method == 'POST' and form.validate():
        caseNum = form.caseNum.data
        caseNotes = form.caseNotes.data
        lawyer_id = current_user.id 
        print("\n", caseNum, caseNotes)
        case = Case(caseNum, caseNotes, lawyer_id)

        db.session.add(case)
        db.session.commit()
        return redirect(url_for('create_cases'))
    cases = Case.query.all()
    return render_template('create_case.html', form=form, cases=cases)

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
        if logged_user and check_password_hash(logged_user.password, password):
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

# Route for who
@app.route('/who')
def who():
    return render_template('who.html')

# Route for what
@app.route('/what')
def what():
    return render_template('what.html')

# Route for contact
@app.route('/contact')
def contact():
    return render_template('contact.html')