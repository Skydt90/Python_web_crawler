import os
import re

# Creates a new directory for the project on first startup
def create_project_directory(directory):
        if not os.path.exists(directory):
                print("Creating project: '" + directory + "'")
                os.makedirs(directory)

# Create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
        queue = project_name + "/queue.txt"
        crawled = project_name + "/crawled.txt"
        contents = project_name + "/contents.md"
        
        if not os.path.isfile(queue):
                write_file(queue, base_url)
        if not os.path.isfile(crawled):
                write_file(crawled, "")
        if not os.path.isfile(contents):
                write_file(contents, "")

# Creates a new file
def write_file(path, data):
        f = open(path, "w")
        f.write(data)
        f.close()

# Add data to existing files
def add_to_file(path, data):
        with open(path, "a") as file:
                file.write(data + "\n")

# Add data from list to md file
def add_data_to_mdfile(path, contents):
        f = open(path, "a")
        for entry in contents:
                f.write(entry + "\n")
        f.close()


# Delete the contents of a file
def delete_file_content(path):
        with open(path, "w"):
                pass

# Read a file and convert each line to set items
def file_to_set(file_name):
        results = set()
        with open(file_name, "rt") as f:
                for line in f:
                        results.add(line.replace("\n", ""))
        return results

# Iterate through a set, each item will be a new line in the file
def set_to_file(links, file):
        delete_file_content(file)
        for link in sorted(links):
                add_to_file(file, link)

def list_to_file(contents, file):

        formatted = add_md_formatting(contents)
        add_data_to_mdfile(file, formatted)

def add_md_formatting(contents):
        formatted_list = []

        for line in contents:
                if line.startswith("h1"):
                        placeholder = "\n\n" + line.replace("h1", "# ") + "\n\n"
                        formatted_list.append(placeholder)
                elif line.startswith("h2"):
                        placeholder = "\n" + line.replace("h2", "## ")
                        formatted_list.append(placeholder)
                elif line.startswith("p"):
                        if not line.startswith("pNOTE") and not line.startswith("pAssignment"):
                                placeholder = line.replace("p", "", 1) + "  "
                                formatted_list.append(placeholder)
                elif line.startswith("li"):
                        placeholder = "\n" + line.replace("li", "* ", 1)
                        formatted_list.append(placeholder)
                elif line.startswith("a"):
                        placeholder = line.replace("a", "", 1)
                        formatted_list.append(placeholder)  
        return formatted_list
