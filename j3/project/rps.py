print("1.Rock \n2.Paper \n3.Scissor")
choice1 = input("user1 choice: ")
choice2 = input("user2 choice: ")
if choice1 == "1" and choice2 == "1":
    print("user1 entered Rock and user2 entered Rock so nobody won...")
elif choice1 == "1" and choice2 == "2":
    print("user1 entered Rock and user2 entered Paper so user2 won...")
elif choice1 == "1" and choice2 == "3":
    print("user1 entered Rock and user2 entered Scissor so user1 won...")
elif choice1 == "2" and choice2 == "1":
    print("user1 entered Paper and user2 entered Rock so user1 won...")
elif choice1 == "2" and choice2 == "2":
    print("user1 entered Paper and user2 entered Paper so nobody won...")
elif choice1 == "2" and choice2 == "3":
    print("user1 entered Paper and user2 entered Scissor so user2 won...")
elif choice1 == "3" and choice2 == "1":
    print("user1 entered Scissor and user2 entered Rock so user2 won...")
elif choice1 == "3" and choice2 == "2":
    print("user1 entered Scissor and user2 entered Paper so user1 won...")
elif choice1 == "3" and choice2 == "3":
    print("user1 entered Scissor and user2 entered Scissor so nobody won...")
else:
    print("invalid number...")