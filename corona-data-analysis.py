import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (make sure the file is in the same folder)
df = pd.read_csv("covid19_israel.csv", encoding='utf-8')

# Drop any rows with missing values to clean the data
df.dropna(inplace=True)

# Filter only rows where the corona test result was positive
positive = df[df['corona_result'] == 'חיובי']

# Count total number of tests by gender
total_by_gender = df['gender'].value_counts()

# Count number of positive cases by gender
positive_by_gender = positive['gender'].value_counts()

# Calculate positive rate (as percentage) by gender
positive_rate = (positive_by_gender / total_by_gender) * 100

# Create a bar chart to visualize the results
plt.figure(figsize=(6, 5))
positive_rate.plot(kind='bar', color='purple')
plt.title("Positive COVID-19 Test Rate by Gender", fontsize=14)
plt.xlabel("Gender")
plt.ylabel("Positive Test Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()

# Save the figure and display it
plt.savefig("positive_rate_by_gender.png")
plt.show()

