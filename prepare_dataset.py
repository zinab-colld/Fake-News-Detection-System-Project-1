import pandas as pd

FAKE_PATH = "Fake.csv"
TRUE_PATH = "True.csv"

fake = pd.read_csv(FAKE_PATH)
true = pd.read_csv(TRUE_PATH)

fake["label"] = "fake"
true["label"] = "real"

df = pd.concat([true, fake], ignore_index=True)

df.drop_duplicates(subset=["text"], inplace=True)

df.to_csv("DATASET.csv", index=False, encoding="utf-8")

print("تم إنشاء DATASET.csv بنجاح")
