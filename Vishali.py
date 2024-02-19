import os
import socket
from collections import Counter
import string

def list_files(directory):
    return [file for file in os.listdir(directory) if file.endswith('.txt')]

def count_words(file_path):
    with open(file_path, 'r') as file:
        return len(file.read().split())

def get_top_words(file_path, top_count=3):
    with open(file_path, 'r') as file:
        words = file.read().split()
        words = [word.strip(string.punctuation).capitalize() for word in words]
        return Counter(words).most_common(top_count)

def get_machine_ip_address():
    return socket.gethostbyname(socket.gethostname())

def main():
    data_directory = '/home/data'
    output_directory = '/home/output'
    result_file_path = os.path.join(output_directory, 'result.txt')

    text_files = list_files(data_directory)
    
    limerick_file_path = os.path.join(data_directory, 'Limerick.txt')
    if_file_path = os.path.join(data_directory, 'IF.txt')

    word_count_limerick = count_words(limerick_file_path)
    word_count_if = count_words(if_file_path)

    top_words_if = get_top_words(if_file_path)

    machine_ip_address = get_machine_ip_address()

    with open(result_file_path, 'w') as result_file:
        result_file.write("List of all the text files in the directory:\n")
        result_file.writelines(f"{text_file}\n" for text_file in text_files)
        result_file.write(f"No of words in Limerick.txt: {word_count_limerick}\n")
        result_file.write(f"No of words in IF.txt: {word_count_if}\n")
        result_file.write(f"Total number of words: {word_count_if + word_count_limerick}\n")
        result_file.write("Top 3 words with their counts in IF.txt:\n")
        result_file.writelines(f"{word} -> count: {count}\n" for word, count in top_words_if)
        result_file.write(f"IP address of the machine: {machine_ip_address}\n")

    with open(result_file_path, 'r') as result_file:
        print(result_file.read())

if __name__ == "__main__":
    main()
