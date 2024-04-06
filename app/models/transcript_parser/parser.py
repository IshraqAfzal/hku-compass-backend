import PyPDF2
import re
from typing import BinaryIO


def extract_text_from_pdf(pdf_file: BinaryIO):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text


def extract_transcript_info(pdf_file: BinaryIO):
    pdf_text = extract_text_from_pdf(pdf_file)
    student_info = {}
    courses = []

    name_id_pattern = r"Official Name: (.+)\s(\d+)"
    match = re.search(name_id_pattern, pdf_text)
    if match:
        student_info["Name"] = match.group(1)
        student_info["Student ID"] = match.group(2)

    program_level_pattern = (
        r"Academic Career: (.+)\nAcademic Program: (.+)\nLevel: (.+)"
    )
    match = re.search(program_level_pattern, pdf_text)
    if match:
        student_info["Academic Career"] = match.group(1)
        student_info["Academic Program"] = match.group(2)
        student_info["Year of Study"] = match.group(3)

    course_pattern = r"([A-Z]{4}\s+\d{4})\s+(.+?)\s+(\d{4}-\d{2}\s+.+?)\s+(\S+)\s+(\S+)"
    matches = re.findall(course_pattern, pdf_text)
    for match in matches:
        course = {
            "Course Code": match[0],
            "Course Title": match[1],
            "Term": match[2],
            "Grade": match[3],
            "Units": match[4],
        }
        courses.append(course)

    student_info["Courses"] = courses

    return student_info