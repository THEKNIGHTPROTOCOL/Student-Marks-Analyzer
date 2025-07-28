import pandas as pd 

# Load the student data from CSV
df = pd.read_csv('students.csv')

# Display all student records
print("\n📋 All Student Records:")
print(df)

# Calculate total and average if not already in CSV
if 'Total' not in df.columns or 'Average' not in df.columns:
    df['Total'] = df[['Maths', 'Science', 'English']].sum(axis=1)
    df['Average'] = df['Total'] / 3

# Top Scorer
top_scorer = df.loc[df['Total'].idxmax()]
print(f"\n🏆 Top Scorer: {top_scorer['Name']} - {top_scorer['Total']} Marks")

# Average marks per subject
print("\n📊 Average Marks per Subject:")
print(df[['Maths', 'Science', 'English']].mean())

# Students who scored below average
below_avg = df[df['Average'] < 60]
print("\n⚠️ Students Below Average (Avg < 60):")
print(below_avg[['Roll No', 'Name', 'Average']])

# Save updated data (optional)
df.to_csv("students_updated.csv", index=False)
