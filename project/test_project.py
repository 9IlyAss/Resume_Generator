from project import Resume, validate_date


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
        f"Experience: {experience}\n"
        f"Skills: python, js, node"
    )


def test_validate_date_valid():
    assert validate_date("2020-2024") == True
    assert validate_date("2018-2022") == True


def test_validate_date_invalid():
    assert validate_date("2025-2020") == False
    assert validate_date("20-2020") == False
    assert validate_date("abcd-efgh") == False
    assert validate_date("2030-2035") == False


def test_add_skill():
    resume = Resume(
        "ilyass",
        "zaid",
        "test@test.com",
        "profile"
    )

    resume.add_skill("Python")

    assert resume.skills == ["Python"]


def test_add_education():
    resume = Resume(
        "ilyass",
        "zaid",
        "test@test.com",
        "profile"
    )

    education = {
        "Date": "2020-2022",
        "Place": "Agadir",
        "Field": "IT",
    }

    resume.add_education(education)

    assert resume.education == [education]


def test_add_experience():
    resume = Resume(
        "ilyass",
        "zaid",
        "test@test.com",
        "profile"
    )

    experience = {
        "Date": "2022-2024",
        "Place": "Company",
        "Field": "Developer",
        "Activite": "Build apps",
    }

    resume.add_experience(experience)

    assert resume.experience == [experience]