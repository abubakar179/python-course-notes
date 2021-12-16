colours = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
luckyNumbers = [1, 5, 7]
num = [1, 2, 3]
colours[1] = "purple"
print(colours[1])

num.extend(luckyNumbers) # extending lists (adding on another list)
print(colours)

luckyNumbers.append(2) # appending lists (adding on another item)
print(luckyNumbers)

luckyNumbers.insert(1, 123234345345) # inserting (adding items in certain places)
print(luckyNumbers)

luckyNumbers.remove(7) # removing items in list
print(luckyNumbers)

print(colours.index("red")) # find index of item in list

print(colours.count("purple")) # number of times something appears in list

colours.sort() # sorting in ascending order
print(colours)

list324 = [1, 2, 3, 9, 16]
print(list324)
list324.reverse() # reversing order

list2= list324.copy() # copying list
print(list2)

colours.clear() # clear lists
print(colours)

luckyNumbers.pop() # popping last item on list
print(luckyNumbers)

