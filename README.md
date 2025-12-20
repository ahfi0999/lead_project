# 🎯 Coaching Lead Conversion Predictor

A machine learning-powered web application that predicts the probability of lead conversion for coaching businesses. This tool helps identify high-potential leads and prioritize sales efforts to improve enrollment rates.

## 📋 Overview

This project uses historical lead data to train a machine learning model that predicts whether a prospective student (lead) will convert into a paying customer. The application provides an interactive web interface where sales teams can input lead information and receive instant conversion probability scores along with recommended actions.

## ✨ Features

- **Machine Learning Model**: Logistic Regression model trained on historical lead data
- **Interactive Web Interface**: Built with Streamlit for easy lead scoring
- **Real-time Predictions**: Instant conversion probability calculations
- **Lead Classification**: Automatically categorizes leads as HOT, WARM, or COLD
- **Actionable Recommendations**: Provides next-step suggestions for each lead category:
  - 🔥 HOT LEAD (≥80%): Call immediately
  - ⚠️ WARM LEAD (50-79%): Send email follow-up
  - ❄️ COLD LEAD (<50%): Keep in nurturing list
- **Multiple Input Factors**: Considers behavioral and demographic data including:
  - Time spent on website
  - Number of visits
  - Page views per visit
  - Occupation
  - Lead source
  - City
  - Last activity
  - Sales tags

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ahfi0999/lead_project.git
   cd lead_project
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

#### Step 1: Train the Model

Before running the application, you need to train the machine learning model using the historical data:

```bash
python training_script.py
```

This script will:
- Load the cleaned lead data from `data/leads_cleaned.csv`
- Perform one-hot encoding on categorical features
- Split the data into training and test sets
- Train a Logistic Regression model
- Save the trained model, scaler, and feature columns as `.pkl` files
- Display the model accuracy

**Expected output:**
```
Loading data...
Encoding categorical features...
Saving model columns...
Splitting and scaling data...
Training Logistic Regression model...
Model accuracy: XX.XX%
Training completed. Model saved as 'lead_scoring_model.pkl'
```

#### Step 2: Run the Web Application

Once the model is trained, launch the Streamlit web application:

```bash
streamlit run app.py
```

The application will open in your default web browser (typically at `http://localhost:8501`).

#### Step 3: Make Predictions

1. Use the sidebar to input lead information:
   - Adjust the time spent on website slider
   - Enter total visits and page views
   - Select categorical attributes (occupation, lead source, city, etc.)

2. Click the **"Predict Conversion Score"** button

3. View the results:
   - Conversion probability percentage
   - Lead classification (HOT/WARM/COLD)
   - Recommended action

## 📁 Project Structure

```
lead_project/
├── app.py                      # Streamlit web application
├── training_script.py          # Model training script
├── requirements.txt            # Python dependencies
├── datacleaning.ipynb         # Jupyter notebook for data exploration/cleaning
├── data/
│   └── leads_cleaned.csv      # Cleaned historical lead data
├── .gitignore                 # Git ignore file (excludes .pkl files)
└── README.md                  # Project documentation
```

### Generated Files (after training)

After running `training_script.py`, the following files will be generated:

- `lead_scoring_model.pkl` - Trained Logistic Regression model
- `scaler.pkl` - StandardScaler for feature normalization
- `model_columns.pkl` - Feature column names for consistent encoding

> **Note:** These `.pkl` files are ignored by git (see `.gitignore`) and must be generated locally.

## 🛠️ Technologies Used

- **Python** - Core programming language
- **Streamlit** - Web application framework
- **scikit-learn** - Machine learning library
  - Logistic Regression for classification
  - StandardScaler for feature normalization
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **joblib** - Model serialization

## 📊 Model Details

- **Algorithm**: Logistic Regression
- **Features**: Behavioral metrics (time spent, visits, page views) and categorical attributes (occupation, lead source, city, last activity, tags)
- **Preprocessing**: 
  - One-hot encoding for categorical variables
  - Standard scaling for numerical features
- **Target Variable**: Binary classification (Converted: 1 = Yes, 0 = No)

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

## 📝 License

This project is open source and available for educational and commercial use.

## 🙋‍♂️ Support

If you encounter any issues or have questions, please open an issue in the GitHub repository.

---

**Happy Lead Scoring! 🎉**
