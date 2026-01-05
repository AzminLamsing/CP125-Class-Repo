def count_bright_spots(pixels):
    count = 0
    for item in range (1,len(pixels)-1):
      if (pixels[item] > pixels[item + 1] and pixels[item] > pixels[item - 1]):
         count += 1
    return count