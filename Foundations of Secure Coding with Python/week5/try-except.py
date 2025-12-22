try:
    with open('topper.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("File not found")
except IOError as e:
    print(f"An error occured! Try Again : {e}")