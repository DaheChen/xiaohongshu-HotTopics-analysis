import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# === Load Data ===
df = pd.read_excel("data/raw/xiaohongshu_sampling_template.xlsx")

# Convert likes to integer
def to_int(x):
    try:
        return int(str(x).replace("\u00a0", "").strip())
    except:
        return None

df["Likes"] = df["Likes"].apply(to_int)

# Select relevant columns
df_clean = df[["Title", "Hashtags", "Likes", "Comments", "Favorites", "COLLECT"]].copy()
df_clean["Total_Engagement"] = df_clean[["Likes", "Comments", "Favorites", "COLLECT"]].sum(axis=1)

# === Descriptive Statistics ===
print("Basic Statistics:")
print(df_clean.describe())

# === Top 5 Posts ===
top_posts = df_clean.sort_values(by="Total_Engagement", ascending=False).head(5)
print("\nTop 5 Posts by Engagement:")
print(top_posts[["Title", "Total_Engagement"]])

# === Visualization ===
# Bar chart for Top 5 posts
plt.figure(figsize=(10,6))
sns.barplot(data=top_posts, x="Total_Engagement", y="Title")
plt.title("Top 5 Xiaohongshu Posts by Engagement")
plt.xlabel("Total Engagement")
plt.ylabel("Post Title")
plt.tight_layout()
plt.savefig("results/figures/top_posts.png")
plt.close()

# Word cloud from titles and hashtags
text = " ".join(df_clean["Title"].dropna().tolist() + df_clean["Hashtags"].dropna().tolist())
wc = WordCloud(width=800, height=400, background_color="white").generate(text)
wc.to
