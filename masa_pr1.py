import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.impute import SimpleImputer  # Import SimpleImputer

# Load the data
data = pd.read_csv('C:/Users/smkp8/Downloads/ML model for machine images/2 nd ml/phishing_email.csv/Phishing_Email.csv')

# Handle missing values (replace NaN with empty string)
data['Email Text'].fillna('', inplace=True)

# Prepare the data
X = data['Email Text']  # Text data
y = data['Email Type']   # Email Type (target variable)

# Encode the target variable to numerical values (0 for safe mail, 1 for phishing mail)
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorize the email text using CountVectorizer
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Train a Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train_vectorized, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test_vectorized)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Print classification report for more detailed evaluation metrics
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))