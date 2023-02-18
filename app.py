from typing import Collection
import pymongo
from dotenv import load_dotenv

from classes import Student

def main():
    
    student = Student("Ninrod", "Zeron", "99174999")
    student.save()

    student.LastName = "Marin"
    student.update ()
     
if __name__ == "___main__":
    load_dotenv()
    main()    
