import pandas as pd


def high_performers(filename):
    df = pd.read_csv(filename)
    high_subject_score = df.loc[df["Math","Science","English","Physics","Chemistry"] > 85 ]
    name = set(high_subject_score["Name"])
    return {
        "count": len(name),
        "names": name
    }

result = high_performers("CP125-Class-Repo/labs/lab09/data/students.csv")
print(result)