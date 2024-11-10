# Impledge Assessment - Compound Word Finder

This Python program reads word lists from input text files, identifies the longest and second-longest compound words, and displays them along with the time taken to process the file. A compound word is defined as a word that can be formed by concatenating other words from the same word list.

## Features
- Reads sorted word lists from text files (`Input_01.txt` and `Input_02.txt`).
- Identifies the longest and second-longest compound words.
- Efficiently handles large word lists with 100,000+ words.
- Outputs the time taken to process each file.
- Uses dynamic programming to check if a word can be formed by concatenating other words.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Prerna2kapoor/Impledge-Assesment-
2. Navigate to the project folder: 
    cd impledge-assessment
3.  Ensure that Python is installed:
  python --version

## Running the Program
1. Make sure the input text files (Input_01.txt, Input_02.txt) are in the same directory as the Python script.
2. Run the program:
      python compound_word_finder.py
3.The program will process the files and output the results, which include the longest compound word, the second-longest compound word, and the time taken to process each file.

## Example output:
Processing file: Input_01.txt ,   
Longest Compound Word: ratcatdogcat,
Second Longest Compound Word: catsdogcats,
Time taken to process file Input_01.txt: 0.00 milliseconds

Processing file: Input_02.txt
Longest Compound Word: ethylenediaminetetraacetates,
Second Longest Compound Word: electroencephalographically,
Time taken to process file Input_02.txt: 832.78 milliseconds

## Design Decisions and Approach
## Dynamic Programming for Compound Word Detection:
I used dynamic programming to check if a word can be formed by concatenating smaller words from the list. This approach helps avoid checking all possible combinations, thus speeding up the process.
## Set Data Structure:
The program stores words in a set for fast lookups. Using a set makes it efficient to check if a substring exists in the word list, improving performance.
## Efficient Time Measurement:
The program uses the time module to measure how long it takes to process the input files. The result is displayed in milliseconds.
## Handling Large Files:
The program is optimized to handle large word lists, even those containing more than 100,000 words, by using dynamic programming and optimized data structures.
## Time Complexity
The time complexity of checking if a word is a compound word is O(n) , where 𝑛 , n is the length of the word. The overall complexity depends on the number of words and their lengths. However, dynamic programming significantly speeds up the process by eliminating redundant checks
## Example Input Files
**Input_01.txt**: cat
cats
catsdogcats
catxdogcatsrat
dog
dogcatsdog
hippopotamuses
rat
ratcatdogcat 
## **Input_02.txt**:
A much larger file containing over 100,000 words. Ensure the file contains a sorted list of words (one word per line).

## Performance Considerations
The program is designed to efficiently handle large word lists, even those with 100,000+ words, by using dynamic programming and fast data structures like sets.

The time complexity for checking each word is approximately 
𝑂(𝑛2) [n square], O(n2) [ n square] , where n , n is the length of the word. The program uses memoization to speed up repeated checks.
The time taken to process each input file is displayed in milliseconds, ensuring that even large datasets can be processed efficiently.

## Contributing
Feel free to fork the repository and make changes. If you improve the code, submit a pull request with a description of your changes.

## Steps to contribute:
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -am 'Add feature').
Push to your branch (git push origin feature-branch).
Open a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
                                 #PRERNA KAPOOR
