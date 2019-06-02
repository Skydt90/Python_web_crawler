import os

# Creates a new directory for the project on first startup
def create_project_directory(directory):
        if not os.path.exists(directory):
                print("Creating project: '" + directory + "'")
                os.makedirs(directory)

# Create overview files if they don't exist
def create_overview_files(project_name, base_url):
        queue = project_name + "/queue.txt"
        scraped = project_name + "/scraped.txt"
        
        if not os.path.isfile(queue):
                create_file(queue, base_url)
        if not os.path.isfile(scraped):
                create_file(scraped, "")
        else: 
                delete_file_content(scraped)
                delete_file_content(queue)

# Create a file for the content on a website
def create_content_file(data_file):       
        if not os.path.isfile(data_file):
                create_file(data_file, "")
        else: 
                delete_file_content(data_file)

# Creates a new file
def create_file(path, data):
        file = open(path, "w")
        file.write(data)
        file.close()
        
# Add data to existing files
def add_to_file(path, data):
        with open(path, "a") as file:
                file.write(data + "\n")

# Write data from list to md file
def write_to_mdfile(path, contents):
        with open(path, "w") as file:
                for entry in contents:
                        file.write(entry + "\n")

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

# Writes each line in a list to the file
def list_to_file(contents, file):
        formatted = add_md_formatting(contents)
        write_to_mdfile(file, formatted)

# Converts the input list to an md formatted list
def add_md_formatting(contents):
        formatted_list = []

        for line in contents:
                if line.startswith("h1"):
                        placeholder = "\n" + line.replace("h1", "# ") + "\n"
                        formatted_list.append(placeholder)
                elif line.startswith("h2"):
                        placeholder = "\n" + line.replace("h2", "## ")
                        formatted_list.append(placeholder)
                elif line.startswith("p"):
                        if not line.startswith("pNOTE") and not line.startswith("pAssignment") and not line.startswith("pre<") and not line.startswith("p#"):
                                placeholder = line.replace("p", "", 1) + "  "
                                formatted_list.append(placeholder)
                elif line.startswith("li"):
                        placeholder = "\n" + line.replace("li", "* ", 1)
                        formatted_list.append(placeholder)
                elif line.startswith("a"):
                        placeholder = line.replace("a", "", 1)
                        formatted_list.append(placeholder)  
        return formatted_list