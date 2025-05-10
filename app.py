from flask import Flask,render_template, request
import pickle
import numpy as np

app = Flask(__name__)
scaler = pickle.load(open("scaler.pkl",'rb'))  # load trained model
model = pickle.load(open("Logistic_reg_model.pkl",'rb'))  # if you used a scaler



@app.route("/")
def Homepage():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    # Get data from form
    data = {
        "LoanPurpose": request.form.get("LoanPurpose"),
        "LoanAmount": float(request.form.get("LoanAmount")),
        "Age": float(request.form.get("Age")),
        "Gender": request.form.get("Gender"),
        "Income": float(request.form.get("Income")),
        "EmpExperience": float(request.form.get("EmpExperience")),
        "Education": request.form.get("Education"),
        "HomeOwnership": request.form.get("HomeOwnership"),
        "LoanInterest": float(request.form.get("LoanInterest")),
        "LoanPercent": float(request.form.get("LoanPercent")),
        "CreditHistory": float(request.form.get("CreditHistory")),
        "CreditScore": float(request.form.get("CreditScore")),
        "PreviousLoans": float(request.form.get("PreviousLoans"))
    }

# Convert categorical fields to encoded values as per your model
    education_mapping = {
        'High School': 0, 'Associate': 1, 'Bachelor': 2, 'Master': 3, 'Doctorate': 4
    }
    gender_mapping = {'Female': 0,'Male':1}
    home_mapping = {'Rent': 0, 'Own': 1, 'Mortage': 2, 'Other': 3}
    purpose_mapping = {
        'Personal': 0, 'Education': 1, 'Medical': 2,
        'Venture': 3, 'Home Improvement': 4, 'Debtconsolidation': 5
    }
    previous_loans = {'No':0,'Yes':1}

    # Prepare model input
    model_input = np.array([[
        data["Age"],
        data["Income"],
        data["EmpExperience"],
        data["LoanAmount"],
        data["LoanInterest"],
        data["LoanPercent"],
        data["CreditHistory"],
        data["CreditScore"],
        education_mapping.get(data["Education"], 0),
        gender_mapping.get(data["Gender"], 1),
        home_mapping.get(data["HomeOwnership"], 0),
        purpose_mapping.get(data["LoanPurpose"], 0),
        previous_loans.get(data["PreviousLoans"], 0),
    ]])

    # Scale
    model_input_scaled = scaler.transform(model_input)

    # Predict
    prediction = model.predict(model_input_scaled)

    result = 'Eligible For Loan' if prediction[0] == 1 else 'Not Eligible For Loan'
    return render_template("submit.html", result=result, data=data)


if __name__ == "__main__":
    app.run(debug=True)