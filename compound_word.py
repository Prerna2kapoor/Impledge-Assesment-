import time

def load_words(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def is_compound_word(word, word_set):
    # Dynamic programming approach to check if a word is compound
    dp = [False] * (len(word) + 1)
    dp[0] = True  # Empty string is always a valid base

    for i in range(1, len(word) + 1):
        for j in range(i):
            # Check if the substring can be formed and that we are not using the whole word
            if dp[j] and word[j:i] in word_set and word[j:i] != word:
                dp[i] = True
                break

    return dp[len(word)]

def find_longest_compound_words(words):
    word_set = set(words)
    longest = ""
    second_longest = ""

    for word in words:
        if len(word) > 1 and is_compound_word(word, word_set):
            if len(word) > len(longest):
                second_longest = longest
                longest = word
            elif len(word) > len(second_longest) and word != longest:
                second_longest = word

    return longest, second_longest

def main():
    input_files = ['Input_01.txt', 'Input_02.txt']
    
    for file in input_files:
        start_time = time.time()
        words = load_words(file)
        longest, second_longest = find_longest_compound_words(words)
        end_time = time.time()
        
        time_taken = (end_time - start_time) * 1000  # Convert to milliseconds
        
        print(f"Processing file: {file}")
        print(f"Longest Compound Word: {longest}")
        print(f"Second Longest Compound Word: {second_longest}")
        print(f"Time taken to process file {file}: {time_taken:.2f} milliseconds\n")

if __name__ == "__main__":
    main()