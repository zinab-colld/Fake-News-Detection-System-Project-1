import pandas as pd

true = pd.read_csv(r"C:\Users\TS\Desktop\New folder\Fake.csv")
fake = pd.read_csv(r"C:\Users\TS\Desktop\New folder\True.csv")

# Add label
true["label"] = "real"
fake["label"] = "fake"

# Merge
df = pd.concat([true, fake], ignore_index=True)

# The Columns
df = df[["title", "text", "label"]]

#  Data cleaning
df = df.drop_duplicates(subset=["text"])
df["text"] = df["text"].astype(str).str.replace(r"\s+", " ", regex=True)

#save the data
df.to_csv("DATASET.CSV", index=False)

print("Done!")