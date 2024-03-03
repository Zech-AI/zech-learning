import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample data about World War I and II
data = {
    'world_war_i': 'World War I, also known as the First World War or the Great War, was a global war originating in Europe that lasted from 28 July 1914 to 11 November 1918.',
    'world_war_ii': 'World War II, also known as the Second World War, was a global war that lasted from 1939 to 1945, although conflicts reflecting the ideological clash between what would become the Allied and Axis blocs began earlier.',
    # Add more data as needed
}

# Preprocess the data
corpus = list(data.values())
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

# Function to find the most relevant document based on the user's question
def answer_question(question):
    question_vec = vectorizer.transform([question])
    similarities = cosine_similarity(X, question_vec)
    most_similar_index = similarities.argmax()
    most_similar_key = list(data.keys())[most_similar_index]
    return data[most_similar_key]

# Sample questions
questions = [
    "What was World War I?",
    "When did World War II end?",
    # Add more questions as needed
]

# Answer the questions
for question in questions:
    answer = answer_question(question)
    print("Question:", question)
    print("Answer:", answer)
    print()
