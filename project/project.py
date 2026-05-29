import re
from datetime import date
from fpdf import FPDF


class Resume(FPDF):

    def __init__(
        self,
        first_name,
        last_name,
        email,
        profile,
        phone="",
        address="",
        education=None,
        experience=None,
        skills=None,
    ):
        super().__init__("P", "mm", "A4")
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._phone = phone
        self._address = address
        self._profile = profile
        self._education = education if education is not None else []
        self._experience = experience if experience is not None else []
        self._skills = skills if skills is not None else []

    @property
    def profile(self):
        return self._profile

    @property
    def education(self):
        return self._education

    @property
    def experience(self):
        return self._experience

    @property
    def skills(self):
        return self._skills

    def add_education(self, e):
        self._education.append(e)

    def add_experience(self, e):
        self._experience.append(e)

    def add_skill(self, e):
        self._skills.append(e)

    def __str__(self):
        return (
            f"Full Name: {self._first_name} {self._last_name}\n"
            f"Email: {self._email}\n"
            f"Phone: {self._phone}\n"
            f"Address: {self._address}\n"
            f"Profile: {self._profile}\n"
            f"Education: {self._education}\n"
            f"Experience: {self._experience}\n"
            f"Skills: {', '.join(self._skills)}"
        )

    def header(self):
        self.set_font("helvetica", "B", 28)
        self.cell(0, 12, f"{self._first_name} {self._last_name}", ln=1, align="C")
        self.set_font("helvetica", "", 10)
        contact_info = f"Email: {self._email}"
        if self._phone:
            contact_info += f"  |  Phone: {self._phone}"
        if self._address:
            contact_info += f"  |  Address: {self._address}"
        self.cell(0, 8, contact_info, ln=1, align="C")
        self.ln(4)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(5)


def main():
    (
        first_name,
        last_name,
        email,
        phone,
        address,
        profile,
        education,
        experience,
        skills,
    ) = get_info()

    resume = Resume(
        first_name,
        last_name,
        email,
        profile,
        phone,
        address,
        education,
        experience,
        skills,
    )

    resume.add_page()

    # --- PROFILE ---
    resume.set_font("helvetica", "B", 14)
    resume.cell(0, 8, "Profile", ln=1)
    resume.set_font("helvetica", "", 11)
    resume.multi_cell(190, 6, resume._profile)
    resume.ln(4)
    resume.line(10, resume.get_y(), 200, resume.get_y())
    resume.ln(4)

    # --- EXPERIENCE ---
    resume.set_font("helvetica", "B", 14)
    resume.cell(0, 8, "Experience", ln=1)

    for e in resume._experience:
        resume.set_font("helvetica", "B", 11)
        resume.cell(140, 6, f"{e['Field']} - {e['Place']}")
        resume.set_font("helvetica", "I", 11)
        resume.cell(50, 6, e["Date"], ln=1, align="R")
        resume.set_font("helvetica", "", 11)
        resume.multi_cell(190, 6, f"Activity: {e['Activite']}")
        resume.ln(2)

    resume.ln(2)
    resume.line(10, resume.get_y(), 200, resume.get_y())
    resume.ln(4)

    # --- EDUCATION ---
    resume.set_font("helvetica", "B", 14)
    resume.cell(0, 8, "Education", ln=1)

    for e in resume._education:
        resume.set_font("helvetica", "B", 11)
        resume.cell(140, 6, f"{e['Field']} - {e['Place']}")
        resume.set_font("helvetica", "I", 11)
        resume.cell(50, 6, e["Date"], ln=1, align="R")
        resume.ln(2)

    resume.ln(2)
    resume.line(10, resume.get_y(), 200, resume.get_y())
    resume.ln(4)

    # --- SKILLS ---
    resume.set_font("helvetica", "B", 14)
    resume.cell(0, 8, "Skills", ln=1)
    resume.set_font("helvetica", "", 11)
    resume.multi_cell(190, 6, ", ".join(resume._skills))

    resume.output("Resume.pdf")
    print("\nSuccess! 'Resume.pdf' has been generated.")


def get_info():
    print(
        "=======================================\n"
        "      Welcome to Resume Generator      \n"
        "======================================="
    )
    while True:
        first_name = input("First name: ").strip()
        last_name = input("Last name: ").strip()
        if first_name and last_name:
            break
        print("Name cannot be empty.")

    email = get_email()
    phone = input("Phone (optional): ").strip()
    address = input("Address (optional): ").strip()

    while True:
        profile = input("Profile summary: ").strip()
        if profile:
            break
        print("Profile cannot be empty.")

    education = get_education()
    experience = get_experience()
    skills = get_skills()

    return (
        first_name,
        last_name,
        email,
        phone,
        address,
        profile,
        education,
        experience,
        skills,
    )


def get_email():
    while True:
        email = input("Email: ").strip()
        if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            return email
        print("Invalid Email Format. Try again.")


def get_education():
    entries = []
    while True:
        print("\n--- Add Education Entry ---")
        while True:
            education_date = input("Education date start-end (e.g. 2018-2022): ")
            if validate_date(education_date):
                break
            print("Invalid Date Format ( ####-#### )")

        education_place = input("Education School/Place: ").strip()
        education_field = input("Degree/Field of Study: ").strip()

        entries.append(
            {
                "Date": education_date,
                "Place": education_place,
                "Field": education_field,
            }
        )

        again = input("Add another education entry? (y/n): ").strip().lower()
        if again != "y":
            break
    return entries


def get_experience():
    entries = []
    while True:
        print("\n--- Add Experience Entry ---")
        while True:
            experience_date = input("Experience date start-end (e.g. 2022-2024): ")
            if validate_date(experience_date):
                break
            print("Invalid Date Format ( ####-#### )")

        experience_place = input("Company/Place: ").strip()
        experience_field = input("Job Title/Field: ").strip()
        experience_activite = input("Key Responsibilities/Activities: ").strip()

        entries.append(
            {
                "Date": experience_date,
                "Place": experience_place,
                "Field": experience_field,
                "Activite": experience_activite,
            }
        )

        again = input("Add another experience entry? (y/n): ").strip().lower()
        if again != "y":
            break
    return entries


def validate_date(date_str):
    if re.match(r"^\d{4}-\d{4}$", date_str):
        start, end = map(int, date_str.split("-"))
        current_year = date.today().year
        return start <= current_year and end <= current_year and start <= end
    return False


def get_skills():
    while True:
        skills = input("\nSkills (separated by commas): ").split(",")
        cleaned = [skill.strip() for skill in skills if skill.strip()]
        if cleaned:
            return cleaned
        print("Please enter at least one skill.")


if __name__ == "__main__":
    main()
