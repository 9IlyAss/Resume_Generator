from project import Resume


def test_str():
    education = [
        {
            "Date": "2022-2020",
            "Place": "Agadir",
            "Field": "IT",
        }
    ]

    experience = [
        {
            "Date": "2022-2020",
            "Place": "Agadir",
            "Field": "IT",
            "Activite": "Build somthing",
        }
    ]

    skills = ["python", "js", "node"]

    resume = Resume(
        "ilyass",
        "zaid",
        "ilyss@as.com",
        "hi am sajdi",
        "5678",
        "edrftghj",
        education,
        experience,
        skills,
    )

    assert str(resume) == (
        f"Full Name: ilyass zaid\n"
        f"Email: ilyss@as.com\n"
        f"Phone: 5678\n"
        f"Address: edrftghj\n"
        f"Profile: hi am sajdi\n"
        f"Education: {education}\n"
        f"Experience: {experience}"
        f"Skills: python, js, node"
    )
