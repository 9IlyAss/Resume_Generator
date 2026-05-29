from fpdf import FPDF

class Resume :
    def __init__(self,first_name,last_name,email,profile,phone="",address="",education=None,experience=None,skills=None):
        self._first_name=first_name
        self._last_name=last_name
        self._email=email
        self._phone=phone
        self._address=address
        self._profile=profile
        self._education = education if education is not None else []
        self._experience = experience if experience is not None else []
        self._skills = skills if skills is not None else []
    
    def add_education(e):
        self._education.append(e)

    def add_experience(e):
        self._experience.append(e)

    def add_skill(e):
        self._skills.append(e)
    
    def __str__(self):
        return (
            f"Full Name: {self._first_name} {self._last_name}\n"
            f"Email: {self._email}\n"
            f"Phone: {self._phone}\n"
            f"Address: {self._address}\n"
            f"Profile: {self._profile}\n"
            f"Education: {self._education}\n"
            f"Experience: {self._experience}"
            f"Skills: {', '.join(self._skills)}"
        )


def main():
    print (
        f"=======================================\n\n"
        f"Welcome to Resume Generator \n\n"
        f"======================================="
        )
    first_name=input("First name: ")
    last_name=input("Last name: ")
    email=input("Email: ")
    phone=input("Phone (opional): ")
    address=input("Address (opional): ")
    profile=input("Profile: ")
    education_date,education_place,education_field=input("Education (Date,Place,Field): ")
    experience_date,experience_place,experience_field,experience_activite=input("Experience (Date,Place,Field,activite): ")
    skills=input("Skills (separet with , ): ")




if __name__== "__main__":
    main()