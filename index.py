import re


def calculate_profanity_degree(tweet, racial_slurs):
    words = re.findall(r'\b\w+\b', tweet.lower())
    total_words = len(words)
    profanity_count = 0

    for word in words:
        if word in racial_slurs:
            profanity_count += 1

    return profanity_count / total_words if total_words > 0 else 0


def main():
    racial_slurs = ['racial_slur1', 'racial_slur2',
                    'racial_slur3']

    with open('tweets.txt', 'r') as file:
        tweets = file.readlines()

    for tweet in tweets:
        degree = calculate_profanity_degree(tweet, racial_slurs)
        print(f"Tweet: {tweet.strip()}")
        print(f"Profanity degree: {degree}")
        print()


if __name__ == '__main__':
    main()
