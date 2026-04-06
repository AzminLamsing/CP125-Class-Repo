import pandas as pd

def explore_data(filename):
    # Load CSV into DataFrame
    df = pd.read_csv(filename)
    
    # Total number of students (rows)
    total_students = len(df)
    
    # Subject columns (only the required ones, if they exist)
    subjects = [col for col in ["Math", "Science", "English"] if col in df.columns]
    
    # Calculate average Math score (rounded to 1 decimal)
    math_average = round(df["Math"].mean(), 1)
    
    # Find student with highest Math score
    highest_math_student = df.loc[df["Math"].idxmax(), "Name"]
    
    # Return results as dictionary
    return {
        "total_students": total_students,
        "subjects": subjects,
        "math_average": math_average,
        "highest_math_student": highest_math_student
    }
