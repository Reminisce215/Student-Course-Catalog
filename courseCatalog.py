import sys

import sqlite3

class Node:
	# takes student info
	def __init__(self, department,courseID,courseName,location,building):
		self.left = None
		self.right = None
		self.department = department
		self.courseID =courseID
		self.courseName = courseName
		self.location = location
		self.building = building

# inserts student info as nodes
def insert(node, department, courseID, courseName, location, building):

	#If the tree is empty, retur new a node
	if node is None:
		return Node(department, courseID, courseName, location, building)

	#otherwise recur down the tree
	if courseID < node.courseID:
		node.left= insert(node.left,department,courseID,courseName,location,building)
	else:
		node.right=insert(node.right,department,courseID,courseName,location,building)

	return node

def search(root, searchID):
	if root is None or root.courseID == searchID:
		return root
	if root.courseID < searchID:
		return search(root.right, searchID)
	return search(root.left, searchID)

def inorder(root):
	# keeps record of all student data
    if root:
        inorder(root.left)
        print(root.department + ", "+ str(root.courseID) +"," + root.courseName + ", " + root.location + ", " + root.building)
        inorder(root.right)


def deleteNode(root,department,courseID,courseName,location,building):
	#base case
	if root is None:
		return root

	#recursive calls for ancestors of node to be deleted
	if courseID < root.courseID:
		root.left = deleteNode(root.left,department,courseID,courseName,location,building)
		return root

	elif(courseID > root.courseID):
		root.right= deleteNode(root.right,department,courseID,courseName,location,building)
		return root

	# we reach when root is node to be deleted
	# if root node is a leaf node

	if root.left is None and root.right is None:
		return None

	#if one of the children is empty

	if root.left is None:
		temp= root.right
		root=None
		return temp

	elif root.right is None:
		temp=root.left
		root=None
		return temp

	#if both children exist
	succParent= root

	#find successor
	succ=root.right

	while succ.left != None:
		succParent= succ
		succ= succ.left

	#Delete successor. Since successor
	#is always left child of its parent
	#we can safely make successor's right
	#right child as left of its parent
	#If there is no succ, then assign
	#succ->right to succParent->right

	if succParent != root:
		succParent.left=succ.right
	else:
		succParent.right=succ.right

	#copy successor data to root
	root.courseID = succ.courseID

	return root




#////////////////////////////////////LOG IN//////////////////////////////////////////////////

connector=sqlite3.connect('SchoolManagement.db')
cursor=connector.cursor()

#FETCH NAME FROM DB
name=connector.execute('SELECT NAME FROM SCHOOL_MANAGEMENT')
myresult=name.fetchall()
nameList=myresult.copy()

#FETCH EMAIL FROM DB
email=connector.execute('SELECT EMAIL FROM SCHOOL_MANAGEMENT')
myresult=email.fetchall()
emailList=myresult.copy()

#FETCH PASSWORD FROM DB
password=connector.execute('SELECT PASSWORD FROM SCHOOL_MANAGEMENT')
myresult=password.fetchall()
passwordList=myresult.copy()

#authenticate student name
studentName=True
while(studentName):
    nameMatch = input("Please enter full student name")
    for i in (nameList):

        if nameMatch==''.join(i):
            studentName = False
#authenticate email
emailName=True
while(emailName):
    emailMatch = input("please enter email")
    for i in (emailList):

        if emailMatch==''.join(i):
            emailName = False

#authenticate password
passwordName=True
while(passwordName):
    passwordMatch = input("please enter password")
    for i in (passwordList):

        if passwordMatch==''.join(i):
            print("\nWelcome.")
            passwordName = False


#//////////////////////////////////////COURSE CATALOG/////////////////////////////////////////


cart=None
r = None
#/////////////////Available Courses
r=insert(r,"Math",318,"Probability","Abington","Woodland")
r=insert(r,"CMPSC",462,"Data Structures","University Park","Haverford")
r=insert(r,"CMPSC",430,"Database Design","Abington","Online")
r=insert(r,"English",202,"Technical Writing","Abington","Rydal")
r=insert(r,"CMPSC",463,"Algorithm Analysis","Abington","Woodland")
r=insert(r,"Math",360,"Discrete Mathematics","University Park","Thomas")
r=insert(r,"CMPSC",470,"Compiler Construction","Abington","Online")
r=insert(r,"Math",220,"Matrices","Abington","Woodland")


#CATALOG MENU
while(True):
	print("\n\n\t\t\tCOURSE CATALOG\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t",nameMatch.split()[0],"-",emailMatch)
	x = input("Please choose one of the following options:\n\t1.Search Catalog \n\t2.Delete from cart\n\t3.Print enrollment cart\n\t4.Print available courses in catalog.\n\t5.Exit the program.\nEnter an option: ")

	#search and add course using ID
	if x == "1":
		ID=int(input("\nEnter the course ID to be searched: "))
		searchedRoot = search(r, ID)
		if searchedRoot is None:
			print("Course not found!")
		else:
			print("The details of the courses are: " + searchedRoot.department +", "+ str(searchedRoot.courseID) + ", " + searchedRoot.courseName + ", " + searchedRoot.location + ", " + searchedRoot.building)
			choice=input("Press 1 to add course,  Press 2 to return to main menu.")

			if choice=="1":
				if ID==318:
					cart = insert(cart, "Math", 318, "Probability", "Abington", "Woodland")
					r = deleteNode(r, "Math", 318, "Probability", "Abington", "Woodland")
				if ID == 462:
					cart = insert(cart, "CMPSC", 462, "Data Structures", "University Park", "Haverford")
					r = deleteNode(r, "CMPSC", 462, "Data Structures", "University Park", "Haverford")
				if ID == 430:
					cart = insert(cart, "CMPSC", 430, "Database Design", "Abington", "Online")
					r = deleteNode(r, "CMPSC", 430, "Database Design", "Abington", "Online")
				if ID == 202:
					cart = insert(cart, "English", 202, "Technical Writing", "Abington", "Rydal")
					r = deleteNode(r, "English", 202, "Technical Writing", "Abington", "Rydal")

				if ID == 463:
					cart = insert(cart, "CMPSC", 463, "Algorithm Analysis", "Abington", "Woodland")
					r = deleteNode(r, "CMPSC", 463, "Algorithm Analysis", "Abington", "Woodland")

				if ID == 360:
					cart = insert(cart, "Math", 360, "Discrete Mathematics", "University Park", "Thomas")
					r = deleteNode(r, "Math", 360, "Discrete Mathematics", "University Park", "Thomas")
				if ID == 470:
					cart = insert(cart, "CMPSC", 470, "Compiler Construction", "Abington", "Online")
					r = deleteNode(r, "CMPSC", 470, "Compiler Construction", "Abington", "Online")

				if ID == 220:
					cart = insert(cart, "Math", 220, "Matrices", "Abington", "Woodland")
					r = deleteNode(r, "Math", 220, "Matrices", "Abington", "Woodland")

	#delete course from cart using ID
	elif x== "2":

		ID = int(input("\nEnter ID of course to delete: "))
		searchedRoot = search(cart,ID)
		if searchedRoot is None:
			print("Course not found!")
		else:
			print("Course has been deleted!")
			if ID == 318:
				r = insert(r, "Math", 318, "Probability", "Abington", "Woodland")
				cart = deleteNode(cart, "Math", 318, "Probability", "Abington", "Woodland")
			if ID == 462:
				r = insert(r, "CMPSC", 462, "Data Structures", "University Park", "Haverford")
				cart = deleteNode(cart, "CMPSC", 462, "Data Structures", "University Park", "Haverford")
			if ID == 430:
				r = insert(r, "CMPSC", 430, "Database Design", "Abington", "Online")
				cart = deleteNode(cart, "CMPSC", 430, "Database Design", "Abington", "Online")
			if ID == 202:
				r = insert(r, "English", 202, "Technical Writing", "Abington", "Rydal")
				cart = deleteNode(cart, "English", 202, "Technical Writing", "Abington", "Rydal")

			if ID == 463:
				r = insert(r, "CMPSC", 463, "Algorithm Analysis", "Abington", "Woodland")
				cart = deleteNode(cart, "CMPSC", 463, "Algorithm Analysis", "Abington", "Woodland")

			if ID == 360:
				r = insert(r, "Math", 360, "Discrete Mathematics", "University Park", "Thomas")
				cart = deleteNode(cart, "Math", 360, "Discrete Mathematics", "University Park", "Thomas")
			if ID == 470:
				r = insert(r, "CMPSC", 470, "Compiler Construction", "Abington", "Online")
				cart = deleteNode(cart, "CMPSC", 470, "Compiler Construction", "Abington", "Online")

			if ID == 220:
				r = insert(r, "Math", 220, "Matrices", "Abington", "Woodland")
				cart = deleteNode(cart, "Math", 220, "Matrices", "Abington", "Woodland")

	#display current enrollment cart
	elif x == "3":
		if cart == None:
			print("\nThere are currently no courses in enrollment cart")
		else:
			print("\nDisplaying current enrollment cart:")
			inorder(cart)#originally r

	#display available courses
	elif x == "4":
		if r == None:
			print("\nThere are currently no courses available in course catalog")
		else:
			print("\nDisplaying available courses")
			inorder(r)


	#exit course catalog
	elif x == "5":
		print("\nExiting the application!")
		break

	else:
		print("\nRetry!...")