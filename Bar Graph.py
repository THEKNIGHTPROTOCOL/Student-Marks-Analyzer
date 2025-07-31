import pandas as pd
import matplotlib.pyplot as plt

# Sample student marks data  
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Math": [85, 67, 90, 56, 72],
    "Physics": [78, 59, 82, 49, 69],
    "Chemistry": [92, 75, 88, 60, 80],
    "Biology": [88, 60, 85, 58, 75],
    "English": [76, 70, 89, 61, 78]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate total marks
df["Total"] = df.iloc[:, 1:].sum(axis=1)

# Plot bar graph
plt.figure(figsize=(10, 6))
bars = plt.bar(df["Name"], df["Total"], color='mediumseagreen', edgecolor='black')
plt.title("Total Marks of Students", fontsize=16)
plt.xlabel("Student Name", fontsize=12)
plt.ylabel("Total Marks (out of 500)", fontsize=12)
plt.ylim(0, 500)

# Add text labels above bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 5, int(yval), ha='center', va='bottom')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("/mnt/data/student_marks_bargraph.png")
plt.show()
