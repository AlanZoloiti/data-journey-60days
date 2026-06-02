# Day 8 — NumPy: np.select & NaN

## 🎯 Goal
Handle multiple conditions and missing values using vectorized operations.

---

## 🧠 What I Learned

- np.select → multiple conditions (if / elif / else)
- NaN → missing values
- pd.isna → correct way to check missing data
- importance of condition order

---

## ⚙️ Example

conditions = [
    (df['revenue'] > 50),
    (df['revenue'] > 30),
    (df['revenue'] > 10)
]

choices = ['high', 'medium', 'low']

df['spending_level'] = np.select(conditions, choices, default=None)

---

## 🔥 Key Insights

- np.select = scalable logic for multiple conditions  
- order matters (top-down evaluation)  
- NaN cannot be compared directly  
- use pd.isna instead of == np.nan  

---

## 🎯 Real-World Usage

- segmentation with multiple rules  
- handling missing data  
- feature engineering  

---