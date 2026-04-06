import pandas as pd

def compare_averages(filename):
    df = pd.read_csv(filename)
    average = df[["math_scores","science_scores","english_scores"]].mean().round(1)

    best_subject = df.max(average)
    worst_subject = df.min(average)

    return {
        "Math": averages["Math"],
        "Science": averages["Science"],
        "English": averages["English"],
        "best_subject": best_subject,
        "worst_subject": worst_subject
    }

 
    
compare_averages()




