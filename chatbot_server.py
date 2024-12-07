from flask import Flask, request, jsonify
from nltk.tokenize import word_tokenize
import nltk
from flask_cors import CORS
import nltk

# Download punkt if not already present
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')


# Download necessary NLTK resources
nltk.download('punkt')

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Predefined FAQ data (can be extended)
faq_data = {
    "hy":"how can i help you?",
    "admission dates": "Admissions start from June and end in August.",
    "fee structure": "hostel fee: 100000 ",
    "courses offered": "We offer various undergraduate and postgraduate courses.",
    "campus facilities": "The campus has a library, sports complex, and hostels.",
}

# Function to find the best response based on the query
def find_best_response(query):
    tokens = word_tokenize(query.lower())  # Tokenize the query
    print(f"Tokens: {tokens}")  # Log the tokens for debugging

    # Loop through the FAQ data to find the best match
    for key in faq_data:
        print(f"Checking key: {key}")  # Log the key being checked
        if any(word in key for word in tokens):  # Match any word in the query to the FAQ key
            print(f"Match found: {key}")  # Log the matched key
            return faq_data[key]
    
    # Default response if no match is found
    return "Sorry, I don't have an answer to that. Please contact support."

# Route for handling chatbot messages
@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_query = request.json.get("query", "")
        print(f"Received query: {user_query}")  # Log the incoming query

        # Get the response based on the query
        response = find_best_response(user_query)
        print(f"Response generated: {response}")  # Log the response

        return jsonify({"response": response})
    except Exception as e:
        print(f"Error: {e}")  # Log any errors that occur
        return jsonify({"response": "Oops! Something went wrong. Please try again later."}), 500

# Route for home page to test server status
@app.route('/')
def home():
    return "Welcome to the College Chatbot API!"

if __name__ == '__main__':
    app.run(debug=True)
