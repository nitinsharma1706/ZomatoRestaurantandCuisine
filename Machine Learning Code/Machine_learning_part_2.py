# Importing the necessary libraries
import matplotlib.pyplot as plt  # For plotting
import pandas as pd  # For data manipulation and analysis
import pickle  # For serializing and deserializing Python objects

# Reading the data from the CSV file
df = pd.read_csv('Combined_data.csv')

# Removing unnecessary columns from the DataFrame
df.drop(columns=['Id', 'Urls', 'Restaurant_Name'], inplace=True)

# Calculating the frequency of each location
frq_loc = df.groupby("Location").size()

# Calculating the relative frequency of each location
frq_dis_loc = df.groupby("Location").size() / len(df)

# Creating a copy of the DataFrame and adding a new column for location frequency
df_frq_loc = df.copy()
df_frq_loc["loc_frq"] = df_frq_loc.Location.map(frq_dis_loc)

# Dropping the "Location" column from the DataFrame
df_frq_loc.drop("Location", axis=1, inplace=True)

# Displaying the first few rows of the DataFrame
df_frq_loc.head()

# Extracting the feature matrix (X) and the target variable (y)
X = df_frq_loc.drop(columns=['Cuisines', 'Latitude', 'Longitude', 'Rating', 'Delivery_review_number']).values
y = df_frq_loc['Cuisines'].values

# Splitting the data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2, test_size=0.2)

# Importing the Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier()

# Defining the hyperparameter search space for RandomizedSearchCV
no_of_decision_tree = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
max_no_features = ['sqrt', 'log2']
max_depth = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
criterian_for_decision_tree = ['gini', 'entropy']
min_sample_split = [1, 2, 3, 4, 5]

# Creating a dictionary of hyperparameters for RandomizedSearchCV
random_grid = {
    'n_estimators': no_of_decision_tree,
    'max_features': max_no_features,
    'max_depth': max_depth,
    'criterion': criterian_for_decision_tree,
    'min_samples_split': min_sample_split
}

# Performing randomized search cross-validation to find the best hyperparameters
from sklearn.model_selection import RandomizedSearchCV
rscv = RandomizedSearchCV(estimator=rfc, param_distributions=random_grid, n_iter=25, cv=5, n_jobs=-1)
rscv.fit(X_train, y_train)

# Displaying the best parameters found by RandomizedSearchCV
rscv.best_params_

# Displaying the best estimator found by RandomizedSearchCV
rscv.best_estimator_

# Creating the final Random Forest Classifier with the best hyperparameters
rc_final = RandomForestClassifier(n_estimators=80, min_samples_split=3, max_features='sqrt', max_depth=6, criterion='gini')

# Fitting the classifier to the training data
rc_final.fit(X_train, y_train)

# Making predictions on the test data
y_pred = rc_final.predict(X_test)

# Importing evaluation metrics
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report, confusion_matrix

# Calculating the accuracy score
accuracy_score(y_test, y_pred)

# Displaying the classification report
print(classification_report(y_test, y_pred))

# Saving the trained model to a file using pickle
filename = 'Cuisine_predictor.pkl'
pickle.dump(rc_final, open(filename, 'wb'))

# Loading the saved model from file
load_model = pickle.load(open(filename, 'rb'))

# Making predictions using the loaded model
load_model.predict(X_test)
