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
def study_plan():
    print("Here's your personalized study plan:")
    print("1. Review weak areas and practice problems.")
    print("2. Practice time management skills.")
    print("3. Take additional practice exams.")
    print("4. Access your e-resource here and curate your study plan! https://www.khanacademy.org/")
def main():
    welcome()
    create_profile()
    assessment()
    while True:
        answer = input("Do you need a personalized study plan? (yes/no) ")
        if answer == "yes":

