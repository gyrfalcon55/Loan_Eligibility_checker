
# Loan Eligibility Prediction Model

This project aims to predict the eligibility of an individual for a loan based on 13 input parameters using a **Logistic Regression** model. The model is optimized using **GridSearchCV** for cross-validation and hyperparameter tuning. The project is built with **HTML**, **CSS**, **Bootstrap**, **Python**, and **Flask**, offering a user-friendly web interface to make predictions.

## Features

- **Machine Learning Model**: The model uses **Logistic Regression** to predict loan eligibility.
- **Cross-Validation**: **GridSearchCV** is used for cross-validation and hyperparameter tuning to enhance model performance.
- **Input Parameters**: The model takes 13 different parameters as input to assess loan eligibility.
- **Accuracy**: Achieved an impressive accuracy score of **89%** after model training and optimization.

## Technologies Used

- **HTML**: For creating the web interface.
- **CSS**: For styling the front-end.
- **Bootstrap**: For responsive design.
- **Python**: For the backend logic and machine learning model.
- **Flask**: A micro-framework used to deploy the machine learning model as a web application.

## Installation and Setup

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/loan-eligibility-prediction.git
   cd loan-eligibility-prediction
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:

   ```bash
   python app.py
   ```

4. Open your web browser and navigate to `http://127.0.0.1:5000` to interact with the loan eligibility prediction application.

## Model Training

1. The **Logistic Regression** model is trained using a dataset with 13 features.
2. **GridSearchCV** is employed to find the optimal hyperparameters for the model, improving the prediction accuracy.
3. The final model achieved an **89% accuracy** after training and validation.

## Input Parameters

The following 13 parameters are taken as input to predict loan eligibility:
1. Gender
2. Age
3. Income
4. Credit score
5. Loan amount
6. Loan term
7. Employment status
8. Education level
9. Marital status
10. Number of dependents
11. Property area
12. Previous loan history
13. Loan type

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Logistic Regression** from **scikit-learn** for machine learning implementation.
- **GridSearchCV** for hyperparameter tuning.
- **Flask** for creating a web interface to interact with the model.
