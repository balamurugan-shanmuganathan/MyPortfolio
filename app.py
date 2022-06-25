from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    user_img = os.path.join('static','img', 'Jack.jpeg')
    exl_logo = os.path.join('static','img', 'ExlLogo.png')
    cm_logo = os.path.join('static','img', 'Creditmantri.webp')
    ust_logo = os.path.join('static','img', 'USTGlobal.cms')
    return render_template('index.html',
                            user_img = user_img,
                            exl_logo= exl_logo,
                            cm_logo = cm_logo,
                            ust_logo = ust_logo
                            )
@app.route('/professional_projects')
def profession_project():
    project_img = os.path.join('static','img', 'Project.webp')
    delinquency_img = os.path.join('static','img', 'Delinquency.jpg')
    lendability_img = os.path.join('static','img', 'Lendability.jpg')
    income_img = os.path.join('static','img', 'Income.jpg')
    impactability_img = os.path.join('static','img', 'Impactability.jpeg')
    risk_img = os.path.join('static','img', 'Risk.jpg')
    return render_template('professional_projects.html', 
                            project_img = project_img,
                            delinquency_img =delinquency_img,
                            lendability_img = lendability_img,
                            income_img = income_img,
                            impactability_img = impactability_img,
                            risk_img = risk_img)

@app.route('/personal_projects')
def academic_projects():    
    employee_img = os.path.join('static','img', 'Employee.jpg')
    return render_template('personal_projects.html', 
                            eda_img = employee_img)


if __name__ == '__main__':
    app.run(debug=True)
