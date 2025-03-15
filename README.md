📘 Text to Maths Problem Solver and Search Data Assistant
🔍 A Streamlit-based chatbot that solves math problems and fetches information using Google Gemma 2 and Wikipedia API.

🚀 Features
🧮 Math Solver: Solves mathematical expressions logically with step-by-step reasoning.
🧠 Reasoning Tool: Answers logic-based and reasoning questions.
🌐 Wikipedia Search: Retrieves relevant information from Wikipedia.
🔑 Uses Google Gemma 2 via LangChain and Groq API.
📌 Installation
Clone the repository

git clone https://github.com/your-username/your-repo.git
cd your-repo

Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

Install dependencies
pip install -r requirements.txt

🔑 API Key Setup
Obtain a Groq API Key from Groq.
Enter the API key in the Streamlit sidebar when prompted.

▶️ Usage
Run the Streamlit app:
streamlit run apps.py

🛠️ Tech Stack
Python 🐍
Streamlit 🎨 (UI)
LangChain 🔗 (LLM Integration)
Google Gemma 2 🤖 (AI Model)
Groq API 🔑 (LLM Backend)
Wikipedia API 📚 (Knowledge Retrieval)

📝 How It Works
Enter a math problem or query
The AI processes it using LangChain and Google Gemma 2
Gets the result using Wikipedia API (if needed)
Displays the answer step by step

🔧 Future Improvements
Improve error handling.
Add support for more LLMs.
Enhance UI/UX.

🤝 Contributing
Feel free to fork the repo, create a branch, and submit a pull request! 😊

📜 License
This project is licensed under the MIT License.
