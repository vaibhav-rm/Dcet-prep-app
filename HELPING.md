# Contributing Questions to DCET Quiz App 📖

We welcome volunteers to expand our question database! Follow this guide to add your own questions to the app, either by directly editing the `questions.py` file or by uploading question papers for the community to parse.

---

## 🚀 How to Add Questions

### 1. **Using the `questions.py` File**
The `questions.py` file holds all the quiz questions in a structured format. Here's how you can add new questions:

#### Steps:
1. Open the `questions.py` file located in the project root.
2. Add your questions using the format below:

   ```python
    questions_list = [
    Question("What is the capital of France?", ["London", "Berlin", "Paris", "Madrid"], "Paris")
    ]
   ```

   TO:

      ```python
    questions_list = [
    Question("What is the capital of France?", ["London", "Berlin", "Paris", "Madrid"], "Paris"),
    Question("Which planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter", "Saturn"], "Mars")
    ]
   ```
3. Save the file and run the app to verify your questions (Don't forget to add a comma to the 2nd last Question in the list).

---

### 2. **Using the `question_papers` Folder**
If you have a question paper in PDF format or other supported formats:
1. Place the file in the `question_papers` folder.
2. Add a note in the README or create an issue in the repository to alert others about the upload.
3. Optionally, use parsing tools or scripts to extract questions from the document into the `questions.py` format.

---

## 💡 Guidelines for Adding Questions

1. **Structure Consistency:** 
   Ensure every question object has the keys `question`, `options`, and `answer`.

   ```python
    Question("Question goes here?", ["option1", "option2", "option3", "option4"], "correct Answer")
   ```
   
    Example:
    ```python
    Question("What is the capital of France?", ["London", "Berlin", "Paris", "Madrid"], "Paris")
   ```

2. **Number of Options:** 
   Each question must have exactly **four options**. The correct answer should match one of the provided options.

3. **Accuracy:** 
   Verify the correctness of each question and answer. 

4. **Language:** 
   Use simple, concise, and error-free English.

---

## 🛠️ How to Test Your Questions
- Run the app using:
  ```bash
  python main.py
  ```
- Start a quiz and ensure your questions appear correctly.
- Verify the app registers the correct and incorrect answers appropriately.

---

## 📤 Uploading Question Papers
1. Go to the `question_papers` folder in the repository.
2. Add your question paper file with a descriptive name (e.g., `DCET_2023.pdf`).
3. Commit and push the file to the repository, or raise a pull request with your addition.

---

## 🙌 Join the Community
- Help parse uploaded question papers into structured questions.
- Suggest improvements to the app's question-handling logic.
- Collaborate with other volunteers in enhancing the app!

Check out the [README](README.md) for more information on contributing to this project.

---

## 🌟 Thank You!
Every question you add helps a student prepare better. Together, we can make DCET preparation accessible and effective for everyone. 🎉