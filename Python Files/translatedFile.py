class Student: 
	__name
	__studentId
	__email
	__GPA
	def __init__(self , name):
		self.name = name
		
	def __init__(self , name, studentId):
		self.name = name
		self.studentId = studentId
		
	def __init__(self , name, studentId, email):
		self.name = name
		self.studentId = studentId
		self.email = email
		
	def __init__(self , name, studentId, email, GPA):
		self.name = name
		self.studentId = studentId
		self.email = email
		self.GPA = GPA
		
	def setName(self , newName):
		self.name = newName
		
	def getName(self):
		return name
		
	def setGPA(self , newGPA):
		self.GPA = newGPA
		
	def getGPA(self):
		return GPA
		
	def main (): 
		Student s1 = new Student("Tony", 1)
		Student s2 = new Student("Jimmy", 2, "jimmyt@school.com", 2.6)
		print("Student 1 name is: " + s1.getName()) 
		s1.setName("Anthony")
		print("Student 1 new name is: " + s1.getName()) 
		print("Student 2 name is: " + s2.getName())
		print("Student 2 GPA is: " + s2.getGPA())
		s2.setGPA(3.6)
		print("Student 2 new GPA is: " + s2.getGPA())
		
	
Student.main()