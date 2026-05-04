import pandas as pd
from ydata_profiling import ProfileReport

# Load dataset
df = pd.read_csv("iris_dataset.csv")

# Generate report
profile = ProfileReport(df, title="EDA Report")

# Save report
profile.to_file("report.html")

print("Report generated successfully!")
