import sqlite3

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('excelexam_archive.db')
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS profiles (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        exam TEXT NOT NULL,
                        score REAL);''')
    conn.commit()

def save_profile(conn, name, email, exam, score):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO profiles (name, email, exam, score) VALUES (?, ?, ?, ?)", (name, email, exam, score))
    conn.commit()


def welcome():
    print("Welcome to ExcelExam!")
    print("We will help you assess your strengths and weaknesses and provide a personalized study plan.\n")

def create_profile():
    name = input("Enter your name: ")
    email = input("Enter your email address: ")
    exam = input("Enter the exam you're preparing for: ")
    print(f"Welcome, {name}! You're preparing for {exam}.")
    return name, email, exam

def assessment():
    score = float(input("\n Enter your exam score: "))
    if score >= 90:
        print("Great, you're doing excellent!")
    elif score >= 70:
        print("Good, you're on the right track!")
    elif score >= 50:
        print("Average, you might need to put in a bit more effort.")
    else:
        print("\nDon't worry, you can improve your score with practice!\n")
    return score

def study_plan(score, plans):
    for grade, plan in plans.items():
        if score >= grade:
            print("\nHere's your personalized study plan:")
            for step in plan:
                print(step)
            break

def main():
    conn = create_connection()
    create_table(conn)
    welcome()
    name, email, exam = create_profile()
    score = assessment()
    plans = {
        90: ["Continue your current study habits.", "Explore advanced topics."],
        70: ["Review weak areas and practice problems.", "Practice time management skills."],
        50: ["Review weak areas and practice problems.", "Practice time management skills.", "Take additional practice exams.", "Consider using online learning platform like Khan Academy or Coursera."],
        0: ["Review weak areas and practice problems.", "Practice time management skills.", "Take additional practice exams.", "Consider seeking help from a tutor or study group.", "Consider using online learning platform like Khan Academy or Coursera."]
    }
    save_profile(conn, name, email, exam, score);
    
    while True:
        answer = input("Do you need a personalized study plan? (yes/no) ")
        if answer == "yes":
            study_plan(score,plans)
            break
        elif answer == "no":
            print("Good luck in your examinations!")
            break
        else:
            print("Invalid input. Please answer 'yes' or 'no'.")


if __name__ == "__main__":
    main()