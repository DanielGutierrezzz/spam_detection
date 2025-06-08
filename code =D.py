def get_spam_words():
    return [
        "free", "win", "winner", "cash", "urgent", "buy now", "click here", "subscribe",
        "credit card", "no cost", "guaranteed", "earn money", "100% free", "act now",
        "apply now", "congratulations", "selected", "limited time", "make money",
        "miracle", "offer", "order now", "password", "prize", "promise", "unsubscribe",
        "weight loss", "work from home", "bonus", "cheap", "click this link"
    ]

def check_spam(message):
    spam_words = get_spam_words()
    message = message.lower()
    score = 0
    found_words = []

    for word in spam_words:
        if word in message:
            score += 1
            found_words.append(word)

    return score, found_words

def spam_rating(score):
    if score == 0:
        return "Not Spam"
    elif score <= 3:
        return "Low"
    elif score <= 7:
        return "Medium"
    else:
        return "High"

# --- Main Program ---
message = input("Enter your email message: ")
score, words_found = check_spam(message)
rating = spam_rating(score)

print("\n--- Results ---")
print("Spam Score:", score)
print("Spam Likelihood:", rating)
print("Spam Words Found:", ", ".join(words_found) if words_found else "None")
