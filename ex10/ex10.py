from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample dataset of emails and their labels (1 = spam, 0 = not spam)
emails = ["Win a free lottery now, claim your prize",
    "Meeting scheduled for tomorrow at 10 AM",
    "Congratulations, you won a free gift card",
    "Please review the attached project report",
    "Get cheap loans and credit cards instantly",
    "Lunch with the team at noon today",
    "You have been selected for a free vacation",
    "Reminder: submit your assignment by Friday",
    "Earn money fast working from home",
    "Can we reschedule our call to Monday",
    "Claim your free prize before it expires",
    "The client approved the new proposal",
    "Limited time offer, buy now and save big",
    "Your invoice for this month is attached",
    "Congratulations winner, click here to claim cash",
    "Please find the updated schedule attached"]
labels = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

# Convert text data into numerical feature vectors
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)
y = labels

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Train a Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluate the model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Test the model with new sample emails
test_emails = [
    "Free money waiting for you, click now",
    "Let's catch up over coffee this week",]
test_vectors = vectorizer.transform(test_emails)
results = model.predict(test_vectors)

for email, result in zip(test_emails, results):
    label = "SPAM" if result == 1 else "NOT SPAM"
    print(f"Email: '{email}' --> {label}")