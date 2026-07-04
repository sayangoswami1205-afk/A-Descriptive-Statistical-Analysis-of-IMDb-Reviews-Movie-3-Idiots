# 🎬 A Descriptive Statistical Analysis of IMDb Reviews — *3 Idiots*
**Audience Rating Analytics**
A data analysis project that explores audience opinion on the Bollywood film **3 Idiots (2009)** using descriptive statistics and graphical visualizations built from IMDb review data.
---
## 📌 Project Overview
**3 Idiots (2009)**, directed by Rajkumar Hirani, is one of the most successful Bollywood films, widely appreciated for its emotional storytelling, educational message, humour, and memorable characters. This project investigates audience opinion through IMDb review statistics.
### Objectives
- Analyze IMDb audience ratings
- Calculate descriptive statistics
- Study the distribution of ratings
- Examine audience sentiment
- Interpret graphical results
---
## 📊 Dataset
| Feature | Description |
|---|---|
| Movie | 3 Idiots |
| Source | IMDb |
| Rating Scale | 1–10 |
| Fields | Username, Rating, Review Title, Review Text |
| Analysis Tools | Python + Pandas |
---
## ⚙️ Methodology / Workflow
```
IMDb Reviews
    ↓
Cleaning
    ↓
Preprocessing
    ↓
Statistical Analysis
    ↓
Visualization
    ↓
Interpretation
```
**Statistical Measures used:** Mean, Median, Mode, Variance, Standard Deviation, Skewness, Frequency Distribution, Sentiment Analysis
---
## 📈 Key Statistical Results

| Measure | Value | Interpretation |
|---|---|---|
| Mean | 8.765 | Very high average audience rating |
| Median | 10 | Half of the viewers rated the movie 10 |
| Mode | 10 | Most frequent audience rating |
| Variance | 4.62 | Moderate spread of ratings |
| Standard Deviation | 2.15 | Audience opinions are fairly consistent |
| Skewness | -2.355 | Distribution is negatively (left) skewed |
| Sentiment | Positive | Majority of reviews express appreciation |

---

## 📉 Visualizations

The project includes the following graphical analyses (available in the `Output_Images/` folder):

- **Mean Rating Analysis** – overall average rating computation
- **Median & Mode Histograms** – central tendency visualization
- **Histogram of Ratings** – distribution shape with density overlay
- **Frequency Distribution (Bar Chart)** – rating interval frequencies (1–2, 3–4, 5–6, 7–8, 9–10)
- **Box Plot** – spread and outlier detection
- **Density Curve** – probability distribution of ratings
- **Sentiment Pie Chart** – Positive / Neutral / Negative review composition (85.3% / 9.3% / 5.5%)

---

## 🔍 Key Findings

- Ratings are heavily concentrated in the **8–10 range**, with the highest frequency near a perfect score of 10.
- The distribution is **negatively skewed**, meaning most viewers gave high ratings, with only a small number of low-rating outliers.
- The low standard deviation (2.15) indicates **strong audience consensus**.
- **85.3%** of reviews carry positive sentiment, confirming that audience appreciation is overwhelmingly favourable.

---

## ✅ Conclusion

This project analyzed IMDb audience reviews for *3 Idiots* using descriptive statistical techniques and graphical visualizations. The calculated Mean, Median, Mode, Variance, Standard Deviation, and Skewness — along with the Histogram, Box Plot, Density Curve, Frequency Distribution, and Sentiment Pie Chart — collectively confirm that viewers expressed a strong, positive opinion of the movie.

> *"Data reveals what the audience truly feels."*

---

## 👤 Author

**Sayan Goswami**
B.C. Roy Engineering College
Academic Session 2025–26

## 🛠️ Tools & Libraries

- Python
- Pandas
- Matplotlib / Seaborn (for visualizations)

---

## 📂 Repository Structure

```
├── Output_Images/                     # Generated charts and plots
├── 3_idiots_reviews_analysis.ipynb    # Jupyter notebook with full analysis
├── 3_idiots_reviews_analysis          # Dataset / analysis script
└── README.md                          # Project documentation
```
