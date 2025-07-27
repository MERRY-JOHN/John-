import random
import time
import os

LEADERBOARD_FILE = "leaderboard.txt"

def generate_question(level):
    operations = ['+', '-', '*', '/']
    op = random.choice(operations[:min(level, len(operations))])  # avoid IndexError
    a = random.randint(1, 10 * level)
    b = random.randint(1, 10 * level)

    if op == '/':
        a = a * b  # ensure divisibility

    question = f"{a} {op} {b}"
    correct_answer = eval(question)
    return question, round(correct_answer, 2)

def update_leaderboard(name, score):
    with open(LEADERBOARD_FILE, "a") as f:
        f.write(f"{name} - {score}\n")

def show_leaderboard():
    print("\n🏆 Leaderboard:")
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as f:
            lines = f.readlines()
            entries = []
            for line in lines:
                parts = line.strip().split('-')
                if len(parts) == 2:
                    name, score_str = parts
                    try:
                        score = int(score_str.strip())
                        entries.append((name.strip(), score))
                    except ValueError:
                        continue
            # Sort by score descending
            sorted_entries = sorted(entries, key=lambda x: x[1], reverse=True)
            for name, score in sorted_entries[:5]:
                print(f"{name} - {score}")
    else:
        print("No scores yet.")

def play_game():
    print("🎮 Welcome to MathQuest – Solve & Win!")
    name = input("Enter your name: ")
    score = 0
    level = 1
    time_limit = 10

    for round_num in range(1, 6):
        print(f"\n📚 Level {level} - Round {round_num}")
        question, answer = generate_question(level)
        print(f"⏳ Solve within {time_limit} seconds: {question}")

        start_time = time.time()
        try:
            user_answer = float(input("Your answer: "))
        except ValueError:
            print("❌ Invalid input. Moving on...")
            continue
        end_time = time.time()

        time_taken = end_time - start_time

        if time_taken > time_limit:
            print("⏱️ Time's up!")
        elif abs(user_answer - answer) < 0.01:
            print("✅ Correct!")
            score += 10 * level
            if round_num % 2 == 0:
                level += 1
                time_limit = max(5, time_limit - 1)
        else:
            print(f"❌ Wrong! Correct answer was {answer}")

    print(f"\n🎉 Game Over! Your score: {score}")
    update_leaderboard(name, score)
    show_leaderboard()

if __name__ == "__main__":
    play_game()
