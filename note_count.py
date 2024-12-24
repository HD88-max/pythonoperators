amount = int(input("Enter the amount you want to deposit: "))

note_1 = amount//20
print("£20:",note_1)
note_2 = (amount%20)//10
print("£10:",note_2)
note_3 = ((amount%20)%10)//5
print("£5:" ,note_3)
