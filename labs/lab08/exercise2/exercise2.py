def merge_lists(file1, file2, output_file):
    uniqeu_names = set()
    
    # --- BACA FAIL 1 ---
    f = open(file1, "r")
    lines = f.readlines()
    for line in lines:
        uniqeu_names.add(line.strip()) # Ditambah .strip()
    f.close() # Amalan baik: tutup fail selepas digunakan

    # --- BACA FAIL 2 ---
    f2 = open(file2, "r")
    lines2 = f2.readlines() # DIBETULKAN: Tambah kurungan ()
    for i in lines2:
        uniqeu_names.add(i.strip()) # Ditambah .strip()
    f2.close()

    # --- SUSUN NAMA ---
    sorted_name = sorted(uniqeu_names)

    # --- TULIS KE FAIL OUTPUT ---
    f3 = open(output_file, "w") # DIBETULKAN: Tukar mod "r" kepada "w"
    
    # DIBETULKAN: Loop melalui list sorted_name, bukan lines3
    for item in sorted_name: 
        f3.write(item + "\n") # DIBETULKAN: Guna .write() dan letak \n
        
    f3.close()

    # Pulangkan jumlah nama yang unik
    return len(sorted_name)
# Test your code here
result = merge_lists("labs/lab08/exercise2/data/list1.txt", "labs/lab08/exercise2/data/list2.txt", "labs/lab08/exercise2/data/merged.txt")
print(f"Unique names: {result}")
