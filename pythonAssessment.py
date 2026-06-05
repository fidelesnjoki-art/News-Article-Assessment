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
    
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    
    return max(word_counts, key=word_counts.get)

def calculate_average_word_length(text):
    """
    Calculate average length of words in text.
    Excludes punctuation and special characters.
    Args:
        text (str): The string to analyze
    Returns:
        float: Average word length, 0 if text is empty
    """
    if not text or not text.strip():
        return 0.0
    
    cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
    words = cleaned_text.split()
    
    if not words:
        return 0.0
    
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

def count_paragraphs(text):
    """
    Count number of paragraphs in text.
    Paragraphs defined by empty lines between blocks of text.
    Args:
        text (str): The string to analyze
    Returns:
        int: Number of paragraphs, 1 if text is empty per requirements
    """
    if not text or not text.strip():
        return 1
    
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    return len(paragraphs) if paragraphs else 1

def count_sentences(text):
    """
    Count number of sentences in text.
    Sentences defined by.,!, or? punctuation marks.
    Args:
        text (str): The string to analyze
    Returns:
        int: Number of sentences, 1 if text is empty per requirements
    """
    if not text or not text.strip():
        return 1
    
    sentences = re.split(r'[.!?]+', text)
    # Filter out empty strings from split
    sentences = [s.strip() for s in sentences if s.strip()]
    return len(sentences) if sentences else 1

def main():
    """
    Main driver for news article text analysis.
    Reads article file and runs all analysis tasks.
    """
    filename = "News_Article_for_Python_Assessment.txt"
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            article_text = file.read()
    except FileNotFoundError:
        print(f"Error: {filename} not found. Please check the file path.")
        return
    
    print("=" * 50)
    print("NEWS ARTICLE TEXT ANALYSIS")
    print("=" * 50)
    
    search_word = input("Enter the word to count: ").strip()
    word_count = count_specific_word(article_text, search_word)
    print(f"\n1. Count of '{search_word}': {word_count}")
    
    most_common = identify_most_common_word(article_text)
    print(f"2. Most common word: {most_common}")
    
    avg_length = calculate_average_word_length(article_text)
    print(f"3. Average word length: {avg_length:.2f}")
    
    paragraph_count = count_paragraphs(article_text)
    print(f"4. Number of paragraphs: {paragraph_count}")
    
    sentence_count = count_sentences(article_text)
    print(f"5. Number of sentences: {sentence_count}")
    
    print("=" * 50)

if __name__ == "__main__":
    main()