import pandas as pd
import matplotlib.pyplot as plt


def show_math_trend(filename):
    df = pd.read_csv(filename)
    # 2. Extract Math column
    math_scores = df["Math"]
    # 3. Create line chart
    plt.plot(df.index, math_scores)
    plt.xlabel= ("Student Index")
    plt.ylabel = ("Math Score")
    plt.title = ("Math Score Trends")
    plt.show()

    return len(df)


count = show_math_trend("CP125-Class-Repo/labs/lab09/data/students.csv")
print(count)