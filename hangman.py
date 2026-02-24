import random

print("🤡🎮 WELCOME TO HANGMAN — WHERE YOUR BRAIN IS TESTED 😂")
print("💀 Guess the word before the man is *emotionally damaged*")
print("❤️ You get 6 lives. Use them wisely...\n")

words = ["apple", "banana", "cherry", "grape", "orange"]
word = random.choice(words)

guessed_letters = []
attempts = 6

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\n🧩 WORD:", display.strip())
    print("🧠 Your brain remembers:", guessed_letters)
    print("💔 Lives left:", attempts)

    if "_" not in display:
        print("\n🎉🎉 YOU DID IT!!!")
        print("😎 The hangman is safe today. Word guessed like a BOSS!")
        break

    guess = input("👉 Drop a letter (no pressure 😏): ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("🚨 Bro… ONE letter. Not a word. Not a number. 😑")
        continue

    if guess in guessed_letters:
        print("🔁 Déjà vu! You already tried that 😂")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ NICE! That letter exists 😎🔥")
    else:
        attempts -= 1
        print("❌ WRONG! The hangman is crying now 😭")

if attempts == 0:
    print("\n💀💀 GAME OVER 💀💀")
    print("😵 You killed the hangman.")
    print("📢 The correct word was:", word)
