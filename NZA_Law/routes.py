from NZA_Law import app, db, Message, mail
from flask import render_template, request, redirect, url_for

# Forms import
# from NZA_Law.forms import [INSERT FORMS HERE]

# Models import
# from NZA_Law.models import [INSERT MODELS HERE]

# Flask Login import
from flask_login import login_required, login_user, current_user, logout_user

# Home route - Josh
@app.route('/')
def home():
    return render_template("index.html")

# Register route - Mike


# Create Case route - Leland


# Retrieve Case route - Stephanie
@app.route('/cases/<int:case_id>')
@login_required
def case_detail(case_id):
    case = Case.query.get_or_404(case_id)
    return render_template('case_detail.html', case=case)



# Updating Case route - Stephanie
@app.route('/cases/update/<int:case_id>', methods= ['GET', 'POST'])
@login_required
def case_update(case_id):
    case = Case.query.get_or_404(case_id)
    update_form = CaseNotesForm()

    if request.method == 'POST' and update_form.validate():
        title = update_form.title.data
        content = update_form.content.data
        lawyer_id = current_lawyer.id

        case.title = title
        case.content = content
        case.lawyer_id = lawyer_id


        db.session.commit()
        return redirect(url_for('case_update', case_id=case.id))
    return render_template('case_update.html', update_form=update_form)






# Deleting Case route - Stephanie
@app.route('/cases/delete/<int:case_id>', methods=['POST'])
@login_required
def case_delete(case_id):
    case = Case.query.get_or_404(case_id)
    db.session.delete(case)
    db.session.commit()
    return redirect(url_for('home'))


# Login route - Josh


# Logout route - Josh