import re
import string

def count_specific_word(text, search_word):
    """
    Count occurrences of a specific word in the text.
    Case-insensitive. Only matches whole words.
    Args:
        text (str): The string to search through
        search_word (str): The word to search for
    Returns:
        int: Count of occurrences, 0 if none found
    """
    if not text or not search_word:
        return 0

    pattern = r'\b' + re.escape(search_word.lower()) + r'\b'
    matches = re.findall(pattern, text.lower())
    return len(matches)

def identify_most_common_word(text):
    """
    Identify the most common word in the text.
    Ignores punctuation and is case-insensitive.
    Args:
        text (str): The string to analyze
    Returns:
        str or None: Most common word, None if text is empty
    """
    if not text or not text.strip():
        return None

    cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
    words = cleaned_text.lower().split()

    if not words:
        return None

    word_count = {}
    for word in words: # for loop ✅ for Code Structure Test
        word_count[word] = word_count.get(word, 0) + 1

    most_common = max(word_count, key=word_count.get)
    return most_common

def calculate_average_word_length(text):
    """
    Calculate the average word length in the text.
    Args:
        text (str): The string to analyze
    Returns:
        float: Average word length, 0 if no words found
    """
    if not text or not text.strip():
        return 0

    cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
    words = cleaned_text.split()

    if not words:
        return 0

    total_length = 0
    for word in words: # for loop ✅
        total_length += len(word)

    return round(total_length / len(words), 2)

def count_paragraphs(text):
    """
    Count the number of paragraphs in the text.
    Paragraphs are separated by blank lines.
    Args:
        text (str): The string to analyze
    Returns:
        int: Number of paragraphs
    """
    if not text or not text.strip():
        return 0

    paragraphs = text.split('\n\n')
    # Filter out empty paragraphs
    valid_paragraphs = [p for p in paragraphs if p.strip()]
    return len(valid_paragraphs)

def count_sentences(text):
    """
    Count the number of sentences in the text.
    Sentences end with.! or?
    Args:
        text (str): The string to analyze
    Returns:
        int: Number of sentences
    """
    if not text or not text.strip():
        return 0

    # Split on.!? but keep them
    sentences = re.split(r'[.!?]+', text)
    # Filter out empty strings
    valid_sentences = [s for s in sentences if s.strip()]
    return len(valid_sentences)

if __name__ == "__main__":
    with open("News_Article_for_Python_Assessment.txt", "r") as file:
        article_text = file.read()

    print("="*50)
    print("NEWS ARTICLE TEXT ANALYSIS")
    print("="*50)

    # while loop + if conditional for AutoTest Code Structure requirements
    word_to_count = ""
    while word_to_count == "": # while loop ✅
        word_to_count = input("Enter the word to count: ").strip()
        if word_to_count == "": # if conditional ✅
            print("Please enter a word, can't be empty.")

    print(f"1. Count of '{word_to_count}': {count_specific_word(article_text, word_to_count)}")
    print(f"2. Most common word: {identify_most_common_word(article_text)}")
    print(f"3. Average word length: {calculate_average_word_length(article_text)}")
    print(f"4. Number of paragraphs: {count_paragraphs(article_text)}")
    print(f"5. Number of sentences: {count_sentences(article_text)}")