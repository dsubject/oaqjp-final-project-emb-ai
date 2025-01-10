# Emotion Detection Application

This project is an Emotion Detection application that uses embeddable AI libraries to analyze text and determine the dominant emotion. The application is packaged, tested, and deployed on the web using Flask.

---

## **Features**
- Detects five primary emotions in text: `anger`, `disgust`, `fear`, `joy`, and `sadness`.
- Identifies the dominant emotion based on the highest score.
- Provides an API endpoint for emotion analysis.
- Handles error cases for invalid or blank input.
- Fully compliant with Python's PEP8 standards (10/10 PyLint score).

---

## **How It Works**
1. Users submit text to the `/emotionDetector` API endpoint.
2. The application processes the text using the `EmotionDetection` library.
3. The system returns emotion scores and the dominant emotion in a formatted response.
4. Handles blank or invalid inputs gracefully.

---

## **API Endpoint**
### `/emotionDetector`
- **Method:** `POST`
- **Input:** JSON payload with the key `text`
    ```json
    {
      "text": "I love programming!"
    }
    ```
- **Output:**
    ```json
    {
        "anger": 0.01,
        "disgust": 0.02,
        "fear": 0.03,
        "joy": 0.95,
        "sadness": 0.04,
        "dominant_emotion": "joy"
    }
    ```

- **Error Handling:**
    - For blank input:
        ```json
        {
          "error": "Invalid text! Please try again!"
        }
        ```

---

## **Setup Instructions**
1. Clone the repository:
    ```bash
    git clone https://github.com/dsubject/oaqjp-final-project-emb-ai.git
    cd oaqjp-final-project-emb-ai/final_project
    ```
2. Install required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the application:
    ```bash
    python3.11 server.py
    ```
4. Access the application at [http://localhost:5000/emotionDetector](http://localhost:5000/emotionDetector).

---

## **Testing**
Unit tests are provided to validate the functionality of the emotion detection system:
1. Run the tests:
    ```bash
    python3.11 -m unittest test_emotion_detection.py
    ```
2. Verify all tests pass.

---

## **Static Code Analysis**
This project follows PEP8 guidelines and achieves a perfect PyLint score:
1. Run PyLint:
    ```bash
    pylint server.py
    ```
2. Ensure a `10/10` score is displayed.

---

## **Web Deployment**
The application is deployed locally using Flask. It is accessible at:
- [http://localhost:5000](http://localhost:5000)

Example Usage:
- Input: `I am excited to learn more about AI!`
- Output:
    ```
    For the given statement, the system response is 'anger': ..., 'disgust': ..., 'fear': ..., 'joy': ... and 'sadness': .... The dominant emotion is joy.
    ```

---

## **Project Highlights**
- Leveraged Watson embeddable AI libraries for NLP tasks.
- Demonstrated skills in Flask, unit testing, and Python packaging.
- Incorporated robust error handling and static code analysis.

---

## **Future Enhancements**
- Deploy the application on cloud platforms (e.g., AWS, Heroku, or Azure).
- Add support for additional emotions or languages.
- Provide a web-based interface for easier interaction.

---

## **Author**
Created by [dsubject](https://github.com/dsubject). 

This project was initially forked from ibm-developer-skills-network/oaqjp-final-project-emb-ai.

