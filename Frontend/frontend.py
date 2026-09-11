import gradio as gr
import requests


# FastAPI backend URL
BASE_URL = "http://127.0.0.1:8000"


# ============================================================
# ADD STUDENT
# ============================================================

def add_student(name, course, marks):

    url = f"{BASE_URL}/students"

    params = {
        "name": name,
        "course": course,
        "marks": marks
    }

    response = requests.post(url, params=params)

    if response.status_code == 200:
        return response.json()

    return f"Error: {response.text}"


# ============================================================
# VIEW ALL STUDENTS
# ============================================================

def view_students():

    url = f"{BASE_URL}/students"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return f"Error: {response.text}"


# ============================================================
# VIEW ONE STUDENT
# ============================================================

def view_student(student_id):

    url = f"{BASE_URL}/students/{student_id}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return f"Error: {response.text}"


# ============================================================
# UPDATE STUDENT
# ============================================================

def update_student(student_id, marks):

    url = f"{BASE_URL}/students/{student_id}"

    params = {
        "marks": marks
    }

    response = requests.put(url, params=params)

    if response.status_code == 200:
        return response.json()

    return f"Error: {response.text}"


# ============================================================
# DELETE STUDENT
# ============================================================

def delete_student(student_id):

    url = f"{BASE_URL}/students/{student_id}"

    response = requests.delete(url)

    if response.status_code == 200:
        return response.json()

    return f"Error: {response.text}"


# ============================================================
# GRADIO UI
# ============================================================

with gr.Blocks(title="Student Management System") as app:

    gr.Markdown(
        """
        # 🎓 Student Management System

        Manage students using FastAPI + Supabase
        """
    )


    # --------------------------------------------------------
    # ADD STUDENT
    # --------------------------------------------------------

    with gr.Tab("Add Student"):

        name = gr.Textbox(
            label="Student Name",
            placeholder="Enter student name"
        )

        course = gr.Textbox(
            label="Course",
            placeholder="Enter course"
        )

        marks = gr.Number(
            label="Marks",
            precision=0
        )

        add_button = gr.Button("Add Student")

        add_output = gr.JSON(
            label="Response"
        )

        add_button.click(
            fn=add_student,
            inputs=[name, course, marks],
            outputs=add_output
        )


    # --------------------------------------------------------
    # VIEW STUDENTS
    # --------------------------------------------------------

    with gr.Tab("View Students"):

        view_button = gr.Button("View All Students")

        students_output = gr.JSON(
            label="Students"
        )

        view_button.click(
            fn=view_students,
            inputs=[],
            outputs=students_output
        )


    # --------------------------------------------------------
    # VIEW ONE STUDENT
    # --------------------------------------------------------

    with gr.Tab("View One Student"):

        student_id = gr.Number(
            label="Student ID",
            precision=0
        )

        view_one_button = gr.Button("View Student")

        student_output = gr.JSON(
            label="Student"
        )

        view_one_button.click(
            fn=view_student,
            inputs=student_id,
            outputs=student_output
        )


    # --------------------------------------------------------
    # UPDATE STUDENT
    # --------------------------------------------------------

    with gr.Tab("Update Student"):

        update_id = gr.Number(
            label="Student ID",
            precision=0
        )

        new_marks = gr.Number(
            label="New Marks",
            precision=0
        )

        update_button = gr.Button("Update Marks")

        update_output = gr.JSON(
            label="Response"
        )

        update_button.click(
            fn=update_student,
            inputs=[update_id, new_marks],
            outputs=update_output
        )


    # --------------------------------------------------------
    # DELETE STUDENT
    # --------------------------------------------------------

    with gr.Tab("Delete Student"):

        delete_id = gr.Number(
            label="Student ID",
            precision=0
        )

        delete_button = gr.Button("Delete Student")

        delete_output = gr.JSON(
            label="Response"
        )

        delete_button.click(
            fn=delete_student,
            inputs=delete_id,
            outputs=delete_output
        )


# ============================================================
# START GRADIO
# ============================================================

app.launch()