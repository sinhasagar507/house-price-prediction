# Ames Housing Price Prediction Project 

## Objective
- To predict housing prices in Ames, Iowa using the "Ames Housing Price Dataset."
- To develop a predictive model with high accuracy and deploy the model as an interactive web application using Streamlit.

## Introduction
The Ames Housing Price Dataset is a well-known dataset in the data science community, often used for regression tasks. This project aims to build a predictive model to estimate housing prices based on various features of the houses. After achieving satisfactory results, the model was deployed on the Streamlit platform to create an interactive web application.

## Data Collection

### Sources and Datasets
- **Ames Housing Price Dataset:**
  - A dataset that includes 79 explanatory variables describing (almost) every aspect of residential homes in Ames, Iowa.

### Data Used in this Project
- **Ames Housing Dataset:** Focused on predicting the sales price of homes in Ames, Iowa.

## Data Analysis
The analysis was conducted using Python, with steps outlined below:

### Data Preprocessing
- **Data Cleaning:** Handled missing values, outliers, and categorical variables to ensure the dataset was ready for modeling.
- **Feature Engineering:** Created new features to improve model performance, including polynomial features and interactions between variables.
- **Normalization:** Standardized numerical features to ensure uniformity in data input.

### Exploratory Data Analysis (EDA)
- **Statistical Analysis:** Conducted descriptive statistics to understand the distribution and central tendencies of the data.
- **Correlation Analysis:** Used heatmaps and scatter plots to identify relationships between variables and the target variable, SalePrice.
- **Visualization:** Created visualizations such as histograms, box plots, and pair plots to explore the data and understand its underlying structure.

### Model Building and Prediction
- **Model Selection:** Tested multiple regression models, including Linear Regression, Random Forest, and Gradient Boosting Machines (GBM).
- **Hyperparameter Tuning:** Used GridSearchCV and RandomizedSearchCV to find the optimal hyperparameters for the models.
- **Model Evaluation:** Evaluated model performance using metrics such as RMSE, MAE, and R² on both training and test datasets.

## Model Deployment
The final model was deployed as a web application using Streamlit. The deployment process involved the following:
- **Streamlit Integration:** Integrated the predictive model into a Streamlit app, allowing users to input housing features and obtain price predictions.
- **User Interface:** Developed a user-friendly interface to facilitate easy interaction with the model.

## Visualization
Various visualizations were created to effectively communicate the insights and model predictions:
- **Feature Importance Bar Chart:** Highlighted the most important features contributing to housing price predictions.
- **Scatter Plots:** Illustrated the relationship between the predicted prices and actual prices.
- **Residual Plots:** Used to evaluate the model's performance by visualizing the difference between actual and predicted prices.

## Results
Key outcomes from the project include:
- **Accurate Predictions:** The model demonstrated a high degree of accuracy in predicting housing prices in Ames, Iowa.
- **Important Features Identified:** Identified key features, such as OverallQual, GrLivArea, and GarageCars, as the most influential factors in predicting housing prices.
- **Interactive Application:** Successfully deployed the model on Streamlit, allowing users to interact with the model and obtain real-time predictions.

## Lessons Learned
- **Feature Engineering:** Effective feature engineering can significantly enhance model performance.
- **Model Selection:** Experimenting with different models and tuning their hyperparameters is crucial for achieving optimal results.
- **Deployment:** Streamlit provides an easy-to-use platform for deploying machine learning models as web applications, making it accessible to end-users.

## Challenges
- **Handling Missing Data:** Addressing missing values in the dataset was challenging and required careful consideration of the impact on model accuracy.
- **Model Overfitting:** Preventing overfitting during model training required the use of cross-validation and regularization techniques.
- **Deployment Issues:** Integrating the model with Streamlit and ensuring smooth user interaction posed some initial challenges, which were eventually resolved.

## Conclusion
This project successfully built and deployed a predictive model for estimating housing prices in Ames, Iowa. The model provides accurate predictions and is accessible through a user-friendly Streamlit application. The insights gained from this project can be applied to similar real estate prediction tasks.

## Tools and Technologies 
- EDA and Machine Learning: Pandas, Numpy, Matplotlib, Seaborn, SKLearn
- Testing and Deployment: FastAPI, Streamlit 

## Setup
1. Set up a virtual environment using [virtualenv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment) or [conda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) and add <code>Python>=3.1.0</code> as your interpreter. If using <code>conda</code> then perform <code>conda install pip</code> for effective package management.  
2. Add dependencies using <code>pip install -r requirements.txt</code>
3. Move into directory path which contains the file <code>app.py</code>. Run the app using <code>streamlit run app.py</code>

## Hosted Model
Head here to check your houses' selling price: https://sinhasagar507-house-price-prediction-app-ryqeid.streamlit.app

## Acknowledgments
This project was completed as part of an independent study on machine learning and model deployment. Special thanks to the data science community for providing the Ames Housing Price Dataset and to the developers of Streamlit for their robust and accessible platform.

## References
- **Ames Housing Dataset**: [Ames Housing Dataset on Kaggle](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data)
- **Streamlit Documentation**: [Streamlit Official Documentation](https://docs.streamlit.io/)
