# AI-Based Sentiment Analyzer

## Description
This project is a web-based sentiment analysis tool that uses a pre-trained model to analyze the sentiment of user-provided text. The application is built using Flask and utilizes MongoDB for storing user reviews and their corresponding sentiment results.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Ensure MongoDB is installed and running on your machine.

## Usage

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.

3. Enter text in the provided input box and click the "Analyze Sentiment" button to see the results.

## License
This project is licensed under the MIT License.
