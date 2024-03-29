# -*- coding: utf-8 -*-
"""Week3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RvXqynzXpf9Ba_a36Q7JQBBgNrOR7QY1

**Week 3**
"""

stuff = list()
stuff.append('python')
stuff.append('chuck')
stuff.sort()

print(stuff[0])
print(stuff.__getitem__(0))
print(list.__getitem__(stuff,0))

print(stuff.__getitem__(0))
print(list.__getitem__(stuff,0))

stuff = list()
dir(stuff)

class PartyAnimal: #class name
  def __init__(self): # constructor (instructions for an object)
    self.x = 0.9  #attricute, default (instance variable)
    print("Created an object of class PartyAnimal.")

  def party(self): #method of class PartyAnimal
    self.x = self.x + 1 #making use of an attribute
    print("So far", self.x)


an = PartyAnimal() #create an object of class Party Animal
an.party() #call the party method from our class of object
an.party()
an.party()

another = PartyAnimal()
print("Type", type(another))
print ("Dir", dir(another))
print ("Attribute type:", type(another.x))
print ("Method type:", type(another.party))

class StudySession:
  def __init__(self):
    self.count = 0
    print("Study session started, the object is being constructed.")

  def studyForOneHour(self):
    self.count += 1
    print("Hours studied:", self.count)

  def studyForGivenNumberOfHours(self,numberOfHours):
    self.count += numberOfHours
    print(f'Hours studied: {self.count}')

  def __del__(self):
    print("The study session has ended after", self.count, "hours.")

session = StudySession() # 0
session.studyForOneHour() # 1
session.studyForOneHour() # 2

session.studyForGivenNumberOfHours(3) # 5

# prior to overriding the object will call its deconstructor

session = "done studying" # overrides the object we created in the variable session
print("session contains", session) #output done studying

class bookClubMember:
  def __init__(self, member_name):
    self.read_count = 0
    self.name = member_name

  def read(self):
    self.read_count += 1
    print(self.name, "has read", self.read_count, 'books.')

alice = bookClubMember("Alice")
alice.read()

bob = bookClubMember("Bob")
bob.read()
alice.read()

# alice 2, bob 1

class bookReviewer(bookClubMember):
  def __init__(self,member_name):
    super().__init__(member_name)
    self.review_count = 0

  def review(self):
    self.read() #assume that maybe reviewing a book requires reading
    self.review_count += 1
    print(self.name, "has reviewed", self.review_count, "books.")

  sally = bookClubMember("Sally")
  sally.read()

  jim = bookReviewer("Jim")
  jim.read() #jim reads a book
  jim.review() #jim reviews a book

  print(dir(jim))
