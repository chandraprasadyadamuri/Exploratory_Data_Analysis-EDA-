# Exploratory_Data_Analysis-EDA-
# Iris Dataset - Data Profiling Project

## Overview

This project performs **Exploratory Data Analysis (EDA)** and **data profiling** on the famous Iris dataset using Python.

The goal is to:
- Understand dataset structure  
- Analyze feature distributions  
- Detect missing values and anomalies  
- Generate an automated profiling report  

---

## Dataset

This project uses the Iris Dataset, which contains measurements of iris flowers.

### Features:
- Sepal Length  
- Sepal Width  
- Petal Length  
- Petal Width  
- Target (species)

---

## Tools & Technologies Used

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- ydata-profiling  

---

## Project Structure

Iris-EDA/
│── eda.py
│── iris_dataset.csv
│── report.html

---

## Steps Performed

1. Data loading using Pandas  
2. Basic data inspection  
3. Automated profiling using `ydata-profiling`  
4. Analysis of:
   - Feature distributions  
   - Correlations  
   - Missing values  
   - Data types  
5. Report generation in HTML format  

---

## Code Used

```python
import pandas as pd
from ydata_profiling import ProfileReport

# Load dataset
df = pd.read_csv("iris_dataset.csv")

# Generate report
profile = ProfileReport(df, title="EDA Report")

# Save report
profile.to_file("report.html")

print("Report generated successfully!")
```

---

## Key Insights

- Dataset is clean with minimal or no missing values  
- Features are mostly numerical  
- Strong correlation exists between petal length and petal width  
- Clear separation between species based on measurements  
- Data distribution is well-balanced  

---

## Output

- `report.html` → Detailed automated EDA report  

---

## How to Run

1. Install required libraries:

```
pip install pandas numpy matplotlib seaborn ydata-profiling
```

2. Run the script:

```
python eda.py
```

3. Open `report.html` in your browser  

---

## Note

- The generated report file can be large  
- Open it locally in your browser for best performance  

---

## Conclusion

This project demonstrates how to quickly analyze a dataset using automated tools like ydata-profiling.

EDA is a crucial first step in any data science workflow, helping to uncover patterns, relationships, and potential issues in the dataset.
