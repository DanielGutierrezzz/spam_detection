def main(): #just a function that holds the code...
    #function that returns a list of common spam trigger words/phrases
    def get_spam_words():
        return [
            "free", "win", "winner", "cash", "urgent", "buy now", "click here", "subscribe",
            "credit card", "no cost", "guaranteed", "earn money", "100% free", "act now",
            "apply now", "congratulations", "selected", "limited time", "make money",
            "miracle", "offer", "order now", "password", "prize", "promise", "unsubscribe",
            "weight loss", "work from home", "bonus", "cheap", "click this link"
        ]

    #Function to check the text for spam words and return a score and list of found words blahh blahh blahh...
    def check_spam(message):
        spam_words = get_spam_words()  #Get the list of spam words or scam words, see what I did there... it rhymes!
        message = message.lower()  #Convert text to lowercase.
        score = 0  #Initialize spam score, starts at 0.
        found_words = []  #List to store found spam words

        #Check if each spam word is in the text
        for word in spam_words:
            if word in message:
                score += 1  #Increase score for each spam word fiund
                found_words.append(word)  #adds the word to the list

        return score, found_words  #Return the total score and the words

    #Function to return spam rating
    def spam_rating(score):
        if score == 0:
            return "Not Spam"
        elif score <= 3:
            return "Low"
        elif score <= 7:
            return "Medium"
        else:
            return "High"

    #Main Program Execution
    message = input("Enter your email message: ")  # Ask user to enter a message
    score, words_found = check_spam(message)  # Check the message and get score and spam words
    rating = spam_rating(score)  # Get the spam rating based on the score

    # Print results
    print("\n--- Results ---")
    print("Spam Score:", score)
    print("Spam Likelihood:", rating)
    print("Spam Words Found:", ", ".join(words_found) if words_found else "None")

# Call the main function
main()
# If you are reading this, this code ain't free, you got to send me 1,000,000 USD if you plan on using this code :D