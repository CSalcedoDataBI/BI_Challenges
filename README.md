# 📊 BI Challenges | Real-World Data Solutions

[![GitHub stars](https://img.shields.io/github/stars/CSalcedoDataBI/BI_Challenges?style=flat-square)](https://github.com/CSalcedoDataBI/BI_Challenges)
[![Forks](https://img.shields.io/github/forks/CSalcedoDataBI/BI_Challenges?style=flat-square)](https://github.com/CSalcedoDataBI/BI_Challenges)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python)](https://www.python.org/)
[![PySpark](https://img.shields.io/badge/Apache%20Spark-3.0%2B-E25A1C?logo=apache-spark)](https://spark.apache.org/)
[![Power Query](https://img.shields.io/badge/Power%20Query-M%20Language-F2C811?logo=powerbi)](https://docs.microsoft.com/en-us/powerquery-m/)

> **Collection of solutions to real-world Excel & BI challenges** from Excel BI community. Learn how to solve complex data problems using **Python**, **PySpark**, and **Power Query (M)**.

---

## 📖 Table of Contents

- [🎯 About This Repository](#-about-this-repository)
- [📂 Challenges by Source](#-challenges-by-source)
- [🛠️ Technologies Used](#-technologies-used)
- [📋 Challenge Index](#-challenge-index)
- [🚀 Getting Started](#-getting-started)
- [🤝 Contributing](#-contributing)
- [📚 Resources](#-resources)

---

## 🎯 About This Repository

This repository documents **solutions to community-driven BI challenges**:

✅ **Challenges from Excel BI** — Official Excel challenge problems  
✅ **Challenges from OMID** — Data transformation & analysis problems  
✅ **Multiple Solution Approaches** — Python, PySpark, Power Query (M)  
✅ **Complete Documentation** — Problem statement + step-by-step solution  
✅ **Runnable Notebooks** — Jupyter notebooks & Power Query scripts included  
✅ **Real Data Sets** — Actual data files for testing & learning  

**Learning Goals:**
- Master data transformation techniques
- Compare solution approaches (Python vs PySpark vs M)
- Understand distributed computing with Spark
- Optimize query performance

---

## 📂 Challenges by Source

### 🏆 Excel BI Challenges

The [Excel BI Community](https://www.linkedin.com/in/excelbi/) publishes weekly Excel challenges on LinkedIn. This section contains my solutions.

**Challenges Included:**

| # | Challenge | Problem | Solutions | Difficulty |
|---|-----------|---------|-----------|------------|
| 403 | **Excel Challenge 403** | Generate 5-year intervals with cumulative sums and percentages | [PySpark](#) | ⭐⭐ |
| 410 | **Excel Challenge 410** | Optimize complex data queries using Power Query | [M Language](#) | ⭐⭐⭐ |
| 416 | **Excel Challenge 416** | Generate sequences from strings (numeric patterns) | [PySpark + Python](#) | ⭐⭐⭐⭐ |

→ **[Explore All Excel BI Solutions](EXCEL_BI/)**

---

### 👤 OMID Challenges

Solutions to data challenges from [OMID Motamedisedeh](https://www.linkedin.com/in/omid-motamedisedeh/), focusing on practical BI scenarios.

→ **[Explore All OMID Solutions](OMID_BI/)**

---

## 🛠️ Technologies Used

| Technology | Purpose | Examples |
|-----------|---------|----------|
| **Python** | Data cleaning, analysis, scripting | Pandas, NumPy, data processing |
| **PySpark** | Distributed processing at scale | Large datasets, transformations |
| **Power Query (M)** | ETL in Excel/Power BI | Complex queries, merges, pivots |
| **Jupyter Notebooks** | Interactive learning & documentation | Step-by-step problem solving |
| **Git** | Version control & collaboration | Tracking solutions |

---

## 📋 Challenge Index

### EXCEL_BI/

```
EXCEL_BI/
├── 403_EXCEL_CHALLENGE/
│   ├── README.md                 # Challenge statement & approach
│   ├── Excel_Challenge_403.ipynb # PySpark solution in Jupyter
│   ├── files/
│   │   ├── Excel_BI.png          # Challenge screenshot
│   │   └── data.xlsx             # Sample data
│   └── solution.py               # Python/PySpark code
│
├── 410_EXCEL_CHALLENGE/
│   ├── README.md
│   ├── Power_Query_Solution.m    # M language code
│   └── files/
│       └── Challenge_410.pbix    # Power BI example
│
└── 416_EXCEL_CHALLENGE/
    ├── README.md
    ├── Sequence_Generator.ipynb  # Multi-approach solution
    └── files/
        └── sequences_output.csv
```

### OMID_BI/

```
OMID_BI/
├── Challenge_001/
├── Challenge_002/
└── ...
```

---

## 🚀 Getting Started

### 1️⃣ **Clone the Repository**

```bash
git clone https://github.com/CSalcedoDataBI/BI_Challenges.git
cd BI_Challenges
```

### 2️⃣ **Choose a Challenge**

Navigate to any challenge folder:

```bash
cd EXCEL_BI/403_EXCEL_CHALLENGE
```

### 3️⃣ **Read the Documentation**

Open `README.md` to understand the problem:

```bash
cat README.md  # or open in your editor
```

### 4️⃣ **Run the Solution**

#### **Option A: Jupyter Notebook** (Interactive)

```bash
jupyter notebook Excel_Challenge_403.ipynb
```

#### **Option B: Python Script** (Quick)

```bash
python solution.py
```

#### **Option C: Power Query** (In Power BI)

1. Open the `.pbix` file in Power BI Desktop
2. Go to **Data → Transform Data**
3. Review the `solution.m` code in Power Query Editor

### 5️⃣ **Explore & Adapt**

- Modify the data source paths
- Change parameters (thresholds, intervals, etc.)
- Test with your own datasets
- Compare different approaches

---

## 💡 Example: Challenge 403 Walkthrough

### **Problem Statement**
> Generate the sum and percentage for 5-year intervals from a year-value dataset.

**Input:**
```
Year  | Value
------|-------
1990  | 100
1992  | 150
2000  | 200
2005  | 300
2015  | 400
```

**Expected Output:**
```
Year Group | Sum of Value | % of Value
-----------|--------------|----------
1990-1994  | 250          | 14%
1995-1999  | 0            | 0%
2000-2004  | 200          | 11%
2005-2009  | 300          | 17%
2010-2014  | 0            | 0%
2015-2019  | 400          | 23%
Grand Total| 1750         | 100%
```

### **Solution: PySpark Approach**

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, floor, sum as _sum, round

spark = SparkSession.builder.appName("Challenge_403").getOrCreate()

# Load data
df = spark.read.csv("data.csv", header=True)

# Calculate 5-year intervals
df_grouped = df.withColumn(
    "YearGroup", 
    ((col("Year") - 1990) / 5).cast("int") * 5 + 1990
).groupBy("YearGroup").agg(_sum("Value").alias("Sum_Value"))

# Calculate percentages
total = df_grouped.agg(_sum("Sum_Value")).collect()[0][0]
df_result = df_grouped.withColumn(
    "Percent", 
    round((col("Sum_Value") / total) * 100, 0)
)

df_result.show()
```

→ **[Full walkthrough →](EXCEL_BI/403_EXCEL_CHALLENGE/README.md)**

---

## 📚 How to Use This Repository

### **For Learning**
- Start with Challenge 403 (⭐⭐ difficulty)
- Follow the Jupyter notebooks step-by-step
- Compare Python vs PySpark vs Power Query approaches
- Modify code and experiment

### **For Reference**
- Use solution patterns for your own projects
- Adapt SQL/PySpark queries for similar problems
- Learn Power Query (M) idioms and best practices
- See how to structure complex data workflows

### **For Community**
- Share your own solutions via pull requests
- Add new challenges from other communities
- Improve documentation & code comments
- Help others learn

---

## 🤝 Contributing

Have a new challenge or solution? We welcome contributions!

### How to Contribute

1. **Fork** the repository
2. **Create a folder:** `CHALLENGE_SOURCE/NNN_DESCRIPTION/`
3. **Add files:**
   - `README.md` — Problem statement & your approach
   - `solution.py` or `solution.m` — Your code
   - `files/` — Data files & screenshots
4. **Push & open a Pull Request**

### Guidelines

- ✅ Include the **original problem statement** (with source link)
- ✅ Document your **approach & logic**
- ✅ Provide **runnable code** (Jupyter or Python script)
- ✅ Add **sample data** or instructions to get it
- ✅ Show **expected output** with screenshots
- ✅ Compare **multiple approaches** if applicable

---

## 📞 Support & Questions

- 📧 **Email:** [csalcedo90@gmail.com](mailto:csalcedo90@gmail.com)
- 💼 **LinkedIn:** [Cristobal Salcedo](https://www.linkedin.com/in/cristobal-salcedo)
- 🐛 **Issues:** [GitHub Issues](https://github.com/CSalcedoDataBI/BI_Challenges/issues)

---

## 📚 Resources

### Excel BI
- 🔗 [Excel BI LinkedIn](https://www.linkedin.com/in/excelbi/)
- 🔗 [Weekly Challenges](https://www.linkedin.com/in/excelbi/)

### OMID BI
- 🔗 [OMID's Profile](https://www.linkedin.com/in/omid-motamedisedeh/)

### Tools & Documentation
- 📖 [PySpark Documentation](https://spark.apache.org/docs/latest/api/python/)
- 📖 [Power Query (M) Reference](https://docs.microsoft.com/en-us/powerquery-m/)
- 📖 [Pandas Documentation](https://pandas.pydata.org/docs/)
- 📖 [Jupyter Notebooks](https://jupyter.org/)
- 📖 **[Power BI, Deneb & Fabric guides](https://csalcedodatabi.com/)** at csalcedodatabi.com — tutorials on Power BI visuals, Deneb/Vega-Lite templates and Microsoft Fabric data agents (in Spanish)

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

You're free to use, modify, and distribute these solutions for educational and commercial purposes.

---

## 🌟 Show Your Support

If these solutions help your learning journey:

⭐ **Star this repository** — Help others find it  
🔄 **Fork & contribute** — Add your own solutions  
💬 **Share feedback** — Tell us what you'd like  

---

<div align="center">

**Made with ❤️ by [Cristobal Salcedo](https://www.csalcedodatabi.com)**

**Powered by Python, PySpark & Power Query**

</div>
