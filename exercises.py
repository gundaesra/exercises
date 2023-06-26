# Gunda Esra Altınışık

##########################
###############################################
# Python Exercises
###############################################

###############################################
# TASK 1: Examine the types of data structures.
###############################################

x = 8
y = 3.2
z = 8j + 18
a = "Hello World"
b = True
c = 23 < 22
l = [1, 2, 3, 4,"String",3.2, False]
d = {"Name": "Jake",
     "Age": [27,56],
     "Adress": "Downtown"}
t = ("Machine Learning", "Data Science")
s = {"Python", "Machine Learning", "Data Science","Python"}


# ANSWER:

values = (x, y, z, a, b, c, l, d, t, s)

for i in values:
    print(i, "=", type(i))

###############################################
# TASK 2: Convert all letters of the given string expression to uppercase.
# Put space instead of commas and periods, separate them word by word.
# ###############################################

text = "The goal is to turn data into information, and information into insight."

# ANSWER:

new_text1 = text.upper()
new_text2 = new_text1.replace(",", "")
new_text3 = new_text2.replace(".", "")
new_text4 = new_text3.replace(" ", "','")
new_text5 = [print("['", new_text4, "']", sep="")]

# One line answer
text.upper().replace(",", "").replace(".", "").split(" ")

###############################################
# TASK 3: Do the following tasks for the given list.
###############################################

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# Step 1: Look at the number of elements of the given list.

len(lst)

# Step 2: Call the elements at index zero and ten.

lst[0]
lst[10]

# Step 3: Create a list ["D","A","T","A"] from the given list.

new_lst = lst[0:4]

# Step 4: Delete the element in the eighth index.

lst.pop(8)

# Step 5: Add a new element.

lst.append("!")

# Step 6: Re-add element "N" to the eighth index.

lst.insert(8, "N")

###############################################
# TASK 4: Apply the following steps to the given dictionary structure.
###############################################

dict = {'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}


# Step 1: Access the key values.

dict.keys()

# Step 2: Access the values.

dict.values()

# Step 3: Update the value 12 of the Daisy key to 13.

dict.update({"Daisy": ["England", 13]})

# Step 4: Add a new key value Ahmet and with a value of [Turkey,24].
dict.update({"Ahmet": ["Turkey", 24]})

# Step 5: Delete Antonio from dictionary.

dict.pop("Antonio")



###############################################
# TASK 5: Write a function that takes a list as an argument,
# assigns the odd and even numbers in the list to separate lists, and returns these lists.
# ###############################################

l = [2, 13, 18, 93, 22]

# ANSWER:

def split_even_odd(l):
    groups = [[], []]
    for i in l:
        if i % 2 == 0:
            groups[0].append(i)
        else:
            groups[1].append(i)
    print(groups)
    return groups

split_l = split_even_odd(l)


###############################################
# TASK 6: In the list given below are the names of the students who won degrees in
# engineering and medicine faculties.
# Respectively, the first three students represent the success rank of the engineering faculty,
# while the last three students belong to the rank of the medical faculty.
# Print student grades specific to faculty using enumarate.
###############################################

students = ["Diana", "Mark", "John", "Nadia", "Marry", "David"]

# ANSWER:

engineering = []
medicine = []

for index, student in enumerate(students, 1):
    if index <= 3:
        engineering.append(student)

    else:
        medicine.append(student)


for index, studentt in enumerate(engineering, 1):
    print("Engineering Faculty", index, ". student", studentt)

for index, studentt in enumerate(medicine, 1):
    print("Medicine Faculty", index, ". student", studentt)

###############################################
# TASK 7: There are 3 lists below. In the lists, there is a course code,
# credit and quota information. Print course information using zip.
################################################

course_code = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
course_credit = [3, 4, 2, 4]
quota = [30, 75, 150, 25]

# ANSWER:

list_zip = list(zip(course_credit, course_code, quota))
list_zip

for(x, y, z) in list_zip:
    print("The course", y, "that has", x, "credits has", z, "quota.")

###############################################
# TASK 8: Below are 2 sets.
# If the 1st set includes the 2nd set, you are expected to define the function that
# will print the common elements of the two,
# if not, the difference of the 2nd set from the 1st set.
###############################################

cluster1 = set(["data", "python"])
cluster2 = set(["data", "function", "qcut", "lambda", "python", "hi"])


# ANSWER:

if cluster1.issuperset(cluster2):
    print(cluster1.intersection(cluster2))
else:
    print(cluster2.difference(cluster1))

