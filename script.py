import os
import re
import socket
from collections import Counter

# File paths
DATA_DIR = "/home/data"
FILE1 = os.path.join(DATA_DIR, "IF-1.txt")
FILE2 = os.path.join(DATA_DIR, "AlwaysRememberUsThisWay-1.txt")
OUTPUT_DIR = os.path.join(DATA_DIR, "output")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "result.txt")

# Ensure output directory exists
print(f"Checking if output directory exists: {OUTPUT_DIR}")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Debug: Confirm directory exists
if os.path.exists(OUTPUT_DIR):
    print(f"✅ Output directory exists: {OUTPUT_DIR}")
else:
    print(f"❌ Output directory is missing!")

# Function to read and process files
def read_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"❌ Error: File not found - {filepath}")
        return ""

# Function to clean and tokenize text
def tokenize(text):
    text = text.lower()
    words = re.findall(r"\b\w+\b", text)  # Extract words
    return words

# Handle contractions
def handle_contractions(text):
    contractions = {"i'm": "i am", "can't": "cannot", "don't": "do not", "it's": "it is", "you're": "you are"}
    for contraction, expanded in contractions.items():
        text = text.replace(contraction, expanded)
    return text

# Get machine's IP address
def get_ip_address():
    return socket.gethostbyname(socket.gethostname())

# Process files
data1 = read_file(FILE1)
data2 = read_file(FILE2)

tokens1 = tokenize(data1)
tokens2 = tokenize(handle_contractions(data2))

# Count words
total_words_file1 = len(tokens1)
total_words_file2 = len(tokens2)
grand_total_words = total_words_file1 + total_words_file2

# Most common words
top3_file1 = Counter(tokens1).most_common(3)
top3_file2 = Counter(tokens2).most_common(3)

# Get container IP
ip_address = get_ip_address()

# Debug: Writing to the file
print(f"Writing results to {OUTPUT_FILE}...")

try:
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(f"Total words in IF-1.txt: {total_words_file1}\n")
        f.write(f"Total words in AlwaysRememberUsThisWay-1.txt: {total_words_file2}\n")
        f.write(f"Grand total words: {grand_total_words}\n")
        f.write(f"Top 3 words in IF-1.txt: {top3_file1}\n")
        f.write(f"Top 3 words in AlwaysRememberUsThisWay-1.txt (after contraction handling): {top3_file2}\n")
        f.write(f"Container IP Address: {ip_address}\n")
    print(f"✅ Successfully wrote to {OUTPUT_FILE}!")
except Exception as e:
    print(f"❌ Error writing to {OUTPUT_FILE}: {e}")

# Debug: Read file back to confirm it exists
if os.path.exists(OUTPUT_FILE):
    print(f"✅ result.txt exists! Reading contents:")
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        print(f.read())
else:
    print(f"❌ result.txt is still missing!")
