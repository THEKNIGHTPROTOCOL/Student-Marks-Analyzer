import pandas as pd
from io import StringIO
   
# Embedded CSV data 
data = """
Roll No,Name,Maths,Science,English,Total,Average
101,Alice,85,90,78,253,84.33
102,Bob,76,80,69,225,75.00
103,Charlie,92,88,94,274,91.33
104,Diana,65,70,60,195,65.00
105,Ethan,88,85,82,255,85.00
106,Fatima,55,60,58,173,57.67
107,George,45,40,50,135,45.00
108,Helen,79,82,77,238,79.33
109,Ishaan,91,94,89,274,91.33
110,Jane,70,75,80,225,75.00
"""

# Load data into a DataFrame
df = pd.read_csv(StringIO(data))

# Display all student records
print("\n📋 All Student Records:\n")
print(df.to_string(index=False))

# Top Scorer(s)
top_score = df['Total'].max()
top_scorers = df[df['Total'] == top_score]
print(f"\n🏆 Top Scorer(s) with {top_score} Marks:")
print(top_scorers[['Roll No', 'Name', 'Total']].to_string(index=False))

# Average marks per subject
print("\n📊 Average Marks per Subject:")
print(df[['Maths', 'Science', 'English']].mean())

# Students below average (Average < 60)
below_avg = df[df['Average'] < 60]
print("\n⚠️ Students Below Average (Avg < 60):")
if below_avg.empty:
    print("None ✅")
else:
    print(below_avg[['Roll No', 'Name', 'Average']].to_string(index=False))
