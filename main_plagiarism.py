"""
Avoid plagiarism
- detect two most likely books that might have plagiarism.
"""

import model.book as Book

class Person:
    
    def __init__(self, id, first_name, second_name, last_name):
        self.id = id
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name

class Company:
    
    def __init__(self, id, name, role, rfc, company_id):
        self.id = id
        self.name = name
        self.role = role
        self.rfc = rfc
        self.company_id = company_id

person = Person(1, "Ricardo", "none", "Rios Rodriguez")

print("ID: ", person.id)
print("First_name: ", person.first_name)
print("Second_name: ", person.second_name)
print("Last_name: ", person.last_name)

company = Company(1, "Company SA de CV", "Financial", "FINSA9023941C0", "COMP12345")

print("ID: ", company.id)
print("Name: ", company.name)
print("Role: ", company.role)
print("RFC: ", company.rfc)
print("Company_ID: ", company.company_id)

#book = Book(1, "Stars", "content")

#print("Book: ", book.id)