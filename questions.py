
class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer


questions_list = [
    Question("What is the capital of France?", ["London", "Berlin", "Paris", "Madrid"], "Paris"),
    Question("Which planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter", "Saturn"], "Mars"),
    Question("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], "Blue Whale"),
    Question("Who painted the Mona Lisa?", ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Michelangelo"], "Leonardo da Vinci"),
    Question("What is the chemical symbol for gold?", ["Au", "Ag", "Fe", "Cu"], "Au"),
    Question("Which country is home to the kangaroo?", ["New Zealand", "South Africa", "Australia", "Brazil"], "Australia"),
    Question("What is the largest ocean on Earth?", ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "Pacific Ocean"),
    Question("Who wrote 'Romeo and Juliet'?", ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"], "William Shakespeare"),
    Question("What is the capital of Japan?", ["Seoul", "Beijing", "Tokyo", "Bangkok"], "Tokyo"),
    Question("Which element has the chemical symbol 'O'?", ["Osmium", "Oxygen", "Gold", "Silver"], "Oxygen")
]
