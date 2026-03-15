import re
from collections import Counter

def generate_notes(transcript):

    # Split transcript into sentences
    sentences = re.split(r'(?<=[.!?]) +', transcript)

    # Clean words
    words = re.findall(r'\w+', transcript.lower())

    # Remove common stopwords
    stopwords = {
        "the","is","in","and","to","of","a","it","that","this","for","on",
        "with","as","are","was","but","be","by","or","an","at","from"
    }

    words = [word for word in words if word not in stopwords]

    # Word frequency
    freq = Counter(words)

    # Score sentences
    sentence_scores = {}

    for sentence in sentences:
        for word in sentence.lower().split():
            if word in freq:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + freq[word]

    # Select top sentences
    important_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:5]

    # Create paragraph summary
    paragraph_summary = " ".join(important_sentences[:3])

    # Generate keyword tips
    keywords = [word for word, count in freq.most_common(5)]

    # Format notes
    notes = "VIDEO NOTES\n"
    notes += "====================\n\n"

    notes += "KEY POINTS:\n"
    for s in important_sentences:
        notes += f"• {s.strip()}\n"

    notes += "\nEXPLANATION:\n"
    notes += paragraph_summary + "\n"

    notes += "\nTIPS TO REMEMBER:\n"
    for k in keywords:
        notes += f"• Remember the concept related to '{k}'.\n"

    return notes