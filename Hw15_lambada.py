# start
#1
import random
import statistics
#l_50_num = [random.randint(1, 101) for i in range(50)]
l_50_num: list[int]= [random.randint(1, 101) for i in range(50)]
print(l_50_num)
avg_l50 = statistics.mean(l_50_num)

print(list(filter(lambda x: x > 50, [random.randint(1, 101) for i in range(50)])))
print(list(filter(lambda x: x > 50, [l_50_num])))
print(list(filter(lambda x: x % 7 == 0, [l_50_num])))
print(l_50_num[10:99 + 1])
print(list(filter(lambda x: x // 10 == x % 10, [l_50_num])))
print(list(filter(lambda x: x // 10 + x % 10 == 9, [l_50_num])))
print(list(filter(lambda x: x > avg_l50, [l_50_num])))
print(list(filter(lambda x: x > max(l_50_num), [l_50_num]))) # the max number is 99

#2
print(list(filter(lambda x: len(x) > 8, ["V Auto Theft Grand ","Fortnite",
"The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch"])))
print(list(filter(lambda x: x.startswith("F") , ["V Auto Theft Grand ","Fortnite",
"The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch"])))
print(list(filter(lambda x: (" ") in x, ["V Auto Theft Grand ","Fortnite",
"The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch"])))
print(list(filter(lambda x: ("V") in x , ["V Auto Theft Grand ","Fortnite",
"The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch"])))

#3
l_20_num: list[int]= [random.randint(-50, 51) for n in range(20)]
print(list(map(lambda x: x ** 3, [l_20_num])))
print(list(map(lambda x: x % 10, [l_20_num])))
print(list(map(lambda x: x * 10 + 32, [l_20_num])))
print(list(map(lambda x: "positive" if x > 0 else "negative", [l_20_num])))

#4
print(list(map(lambda y : y[::-1], ["Mango","Orange","Banana","Apple",
"Strawberry", "Pineapple", "Grapes", "Watermelon"])))
print(list(map(lambda y : y[1], ["Mango","Orange","Banana","Apple",
"Strawberry", "Pineapple", "Grapes", "Watermelon"])))
print(list(map(lambda y : y.upper(), ["Mango","Orange","Banana","Apple",
"Strawberry", "Pineapple", "Grapes", "Watermelon"])))
print(list(map(lambda y : y[len(y //2)], ["Mango","Orange","Banana","Apple",
"Strawberry", "Pineapple", "Grapes", "Watermelon"])))
print(list(map(lambda y : ("!") if y[-1] == ("s") else y, ["Mango","Orange","Banana","Apple",
"Strawberry", "Pineapple", "Grapes", "Watermelon"])))

#5
#"global inside the func is that you use the cell memory from the outside"
#"the disadvantage of using global that you may affect on others func in file"




