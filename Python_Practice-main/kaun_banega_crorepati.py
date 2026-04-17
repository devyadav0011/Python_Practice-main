print("🎉 Kaun Banega Crorepati 🎉\n")

questions = [
    ["What is the capital of India?", "China", "Japan", "Russia", "New Delhi", 4],
    ["Which is the largest ocean in the world?", "Indian Ocean", "Atlantic Ocean", "Pacific Ocean", "Arctic Ocean", 3],
    ["Which is the largest continent in the world?", "Africa", "Asia", "Europe", "Antarctica", 2],
    ["Which is the smallest continent in the world?", "Australia", "Europe", "Antarctica", "Africa", 1],
    ["Which is the largest country in the world?", "India", "USA", "China", "Russia", 4],
    ["Which is the smallest country in the world?", "Vatican City", "Monaco", "Nauru", "Tuvalu", 1],
    ["Which is the largest desert in the world?", "Sahara", "Gobi", "Kalahari", "Arctic", 4],
    ["Which is the largest river in the world?", "Amazon", "Nile", "Yangtze", "Mississippi", 1],
    ["Which is the largest island in the world?", "Greenland", "New Guinea", "Borneo", "Madagascar", 1],
    ["Which is the largest mountain in the world?", "K2", "Kangchenjunga", "Lhotse", "Mount Everest", 4],
    ["Which is the largest lake in the world?", "Caspian Sea", "Superior", "Victoria", "Huron", 1],
    ["Which is the largest waterfall in the world?", "Niagara", "Angel", "Victoria", "Iguazu", 2],
    ["Which is the largest volcano in the world?", "Mauna Loa", "Mount St. Helens", "Mount Vesuvius", "Krakatoa", 1],
    ["Which is the largest city in the world?", "Tokyo", "Delhi", "Shanghai", "Sao Paulo", 1],
    ["Which is the largest country by population in the world?", "India", "USA", "China", "Russia", 3],
    ["Which is the largest economy in the world?", "India", "USA", "China", "Japan", 2]
]

levels = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700]

money = 0

for i in range(len(questions)):
    q = questions[i]
    print(f"\nQuestion for Rs.{levels[i]}")
    print(q[0])
    print(f"1. {q[1]}")
    print(f"2. {q[2]}")
    print(f"3. {q[3]}")
    print(f"4. {q[4]}")
    
    reply = input("Enter your answer (1-4): ")

    if not reply.isdigit() or int(reply) not in [1, 2, 3, 4]:
        print("❌ Invalid input! Please enter a number between 1 and 4.")
        break
    
    reply = int(reply)
    if reply == q[5]:
        money = levels[i]
        print(f"✅ Correct answer!🎊 You have won Rs.{money}")
        if i == len(questions) - 1:
            print("🎊 Congratulations! You have completed the game and won Rs.700 🎊")
    else:
        print(f"❌ Wrong answer! You won Rs.{money}")
        break
