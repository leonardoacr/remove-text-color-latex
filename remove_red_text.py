import os
import re


def create_new_folder(folder_path, file_name):
    output_folder = os.path.join(os.path.dirname(
        folder_path), "removed red text color")
    os.makedirs(output_folder, exist_ok=True)
    return os.path.join(output_folder, file_name)


def remove_red_text_color():
    folder_path = input(
        "Enter the folder path containing the .tex file (C:\\{...}.tex): ")

    try:
        file_name = os.path.basename(folder_path)

        output_file_path = create_new_folder(folder_path, file_name)

        with open(folder_path, "r") as input_file, open(output_file_path, "w") as output_file:
            tex_content = input_file.read()
            modified_tex_content = re.sub(
                r"\\textcolor{red}{((?:[^{}]*|{[^{}]*})*)}", r"\1", tex_content, flags=re.DOTALL)
            output_file.write(modified_tex_content)

        print("Red text color removed successfully.")
        input("Press Enter to exit.")

    except Exception as e:
        print("An error occurred:", str(e))
        input("Press Enter to exit.")


remove_red_text_color()
