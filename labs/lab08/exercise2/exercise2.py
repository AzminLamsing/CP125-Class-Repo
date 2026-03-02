# Lab 08 Exercise 2: Text File Merger
# Write your code below:

def merge_lists(file1, file2, output_file):
    """
    Merge two lists of names, remove duplicates, and sort.

    Args:
        file1: path to first list file
        file2: path to second list file
        output_file: path to output file

    Returns:
        int: count of unique names
    """
    uniqeu_names = set()
    f = open(file1,"r")
    lines = f.readlines()
    for line in lines :
        uniqeu_names.add(line)

    f2 = open(file2,"r")
    lines2 = f2.readlines
    for line in lines2 :
        uniqeu_names.add(line)

    sorted_name = sorted(uniqeu_names)

    f3 = open(output_file,"r")
    lines3 = f3.readlines 
    for item in lines3 :
        sorted_name(lines3)

    return len(sorted_name)


    


# Test your code here
result = merge_lists("labs/lab08/exercise2/data/list1.txt", "labs/lab08/exercise2/data/list2.txt", "labs/lab08/exercise2/data/merged.txt")
print(f"Unique names: {result}")
