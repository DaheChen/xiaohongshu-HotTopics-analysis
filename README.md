# Xiaohongshu Hot Topics Analysis

This repository is a **small-scale data analysis project** focusing on study-abroad related topics from Xiaohongshu (RED).  
It is part of my personal learning journey to practice:
- Data cleaning and preprocessing  
- Basic statistics and visualization  
- Building and publishing small projects on GitHub  

---

## 📊 Project Goals
1. Collect and store manually sampled posts from Xiaohongshu.  
2. Analyze interactions (likes, comments, favorites, collections).  
3. Identify top-performing posts and high-frequency keywords.  
4. Visualize insights using bar charts and word clouds.  
5. Document the process as a portfolio piece.  

---

## 📂 Repository Structure
```
xiaohongshu-HotTopics-analysis/
│
├── README.md              # Project description
├── requirements.txt       # Python dependencies
├── data/
│   ├── raw/               # Raw sampled data (Excel/CSV)
│   └── processed/         # Cleaned data
├── notebooks/
│   └── analysis.ipynb     # Jupyter Notebook exploration
├── src/
│   └── analysis.py        # Python analysis script
├── results/
│   ├── figures/           # Charts & wordclouds
│   └── summary.csv        # Summary statistics
└── LICENSE                # Open-source license
```

---

## ⚙️ Installation
Clone this repository and install dependencies:

```bash
git clone https://github.com/DaheChen/xiaohongshu-HotTopics-analysis.git
cd xiaohongshu-HotTopics-analysis
pip install -r requirements.txt
```

---

## 🚀 Usage
Run the main analysis script:

```bash
python src/analysis.py
```

Results (figures & tables) will be saved in the `results/` folder.

---

## 🧰 Requirements
See `requirements.txt`.  
Key libraries:
- pandas  
- matplotlib  
- seaborn  
- wordcloud  

---

## 📌 Notes
- The dataset used here is **manually sampled** and limited in scale.  
- This project is **for learning and research purposes only**.  
- No large-scale scraping of Xiaohongshu data is performed.  

---

## 📜 License
This project is licensed under the MIT License.
