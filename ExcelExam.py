def welcome():
    print("Welcome to ExcelExam!")
    print("We will help you assess your strengths and weaknesses and provide a personalized study plan.")
def create_profile():
    name = input("Enter your name: ")
    email = input("Enter your email address: ")
    exam = input("Enter the exam you're preparing for: ")
    print(f"Welcome, {name}! You're preparing for {exam}.")
# assessment menu    
def assessment():
    score = float(input("Enter your exam score: "))
    if score >= 90:
        print("Great, you're doing excellent!")
    elif score >= 70:
        print("Good, you're on the right track!")
    elif score >= 50:
        print("Average, you might need to put in a bit more effort.")
    else:
        print("Don't worry, you can improve your score with practice!")

