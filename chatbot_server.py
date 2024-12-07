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
    "hi":"Hi There !",
    "ketan sup":"hi hi hi",
    "courses": "ABESIT offers undergraduate courses in B.Tech (CSE, IT, ECE, ME, CE) and MBA programs.",
    "admission": "You can apply online through our official website. Applications are open from April to July every year.",
    "hostel fees": "The hostel fees for ABESIT are ₹85,000 per year. This includes accommodation, meals, and utilities.",
    "location": "ABESIT is located in Ghaziabad, Uttar Pradesh, India.",
    "contact number": "You can contact the admissions office at +91-1234567890.",
    "semester start": "The new semester typically begins in the first week of August for all courses.",
    "library timings": "The library is open from 9:00 AM to 8:00 PM, Monday to Saturday.",
    "online materials": "You can access online study materials through the ABESIT Student Portal. Use your student ID and password to log in.",
    "sports facilities": "ABESIT offers a wide range of sports facilities, including a cricket ground, football field, basketball court, and indoor sports like table tennis and badminton.",
    "scholarships": "Yes, scholarships are available based on merit and financial need. Visit our Scholarship section on the official website for more details.",
    "fee payment": "Fees can be paid online through the ABESIT portal or directly at the accounts office on campus.",
    "events": "The upcoming events include the TechFest on January 20th and the Annual Cultural Fest on February 10th.",
    "campus visit": "Yes, campus visits are welcome. Please contact the admissions office to schedule your visit.",
    "exam schedule": "The exam schedule is published on the ABESIT portal two weeks before the exam dates.",
    "results": "Results are announced online on the ABESIT Student Portal. Use your student credentials to log in.",
    "what are placements results": "ABESIT has a strong placement cell, with top recruiters including TCS, Infosys, Wipro, and Cognizant.",
    "internships": "Internships are encouraged for all students. Opportunities are posted on the ABESIT Student Portal and through the placement cell.",
    "clubs": "ABESIT has various student clubs such as Robotics Club, Coding Club, Drama Club, and Sports Club. Visit the Clubs section on our website for more information.",
    "canteen": "The canteen offers a variety of food options at affordable prices and is open from 8:00 AM to 7:00 PM.",
    "transport": "ABESIT provides bus services for students and staff. Contact the transport office for routes and timings.",
    "what are the courses available":"ABESIT offers undergraduate courses in B.Tech (CSE, IT, ECE, ME, CE) and MBA programs.",
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
