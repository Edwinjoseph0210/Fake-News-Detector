"""
Fake News Detector (Dummy)

Classify news text as fake or real using simple keyword matching.

Usage:
Run and enter a news headline to classify.

Note:
This is a very basic demo for illustration only.

"""

def classify_news(text):
    fake_keywords = ['fake', 'hoax', 'untrue', 'false']
    real_keywords = ['official', 'confirmed', 'verified', 'true']

    text_lower = text.lower()
    if any(word in text_lower for word in fake_keywords):
        return "Fake News"
    elif any(word in text_lower for word in real_keywords):
        return "Real News"
    else:
        return "Unknown"

def main():
    print("Enter news headline ('exit' to quit):")
    while True:
        headline = input("> ")
        if headline.lower() == 'exit':
            break
        print("Classification:", classify_news(headline))

if __name__ == "__main__":
    main()
