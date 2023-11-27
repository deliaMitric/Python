#Write a Python script that counts the number of files with each extension in a given directory. The script should:
#Accept a directory path as a command line argument (using sys.argv).
#Use the os module to list all files in the directory.
#Count the number of files for each extension (e.g., .txt, .py, .jpg) and print out the counts.
#Include error handling for scenarios such as the directory not being found, no read permissions, or the directory being empty.
import os
import sys
def count_file_ext(directory_path):
    extensions_file = {}
    fisiere_gasite = False
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"{directory_path} nu e gasit!")
        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"{directory_path} nu e un director!")
        elements_list = os.listdir(directory_path)
        if len(elements_list) == 0:
            raise Exception(f"Directorul {directory_path} nu contine elemente!")

        for element in elements_list:
            complete_path = os.path.join(directory_path, element)
            if os.path.isfile(complete_path):
                fisiere_gasite = True
                extension = os.path.splitext(complete_path)[1]
                if extension not in extensions_file:
                    extensions_file[extension] = [complete_path]
                else:
                    extensions_file[extension].append(complete_path)
        if not fisiere_gasite:
            raise Exception(f"Directorul {directory_path} nu contine fisiere!")

    except FileNotFoundError as e:
        print(e)
    except NotADirectoryError as e:
        print(e)
    except PermissionError as e:
        print("Eroare legata de permisiuni")
    except Exception as e:
        if len(e.args) > 0:
            print(e.args[0])
        else:
            print(e)
    else:
        print(f"Numarul de fisiere pentru extensiile gasite in {directory_path}")
        for key, list in extensions_file.items():
            print(f"EXTENSIE: {key} -- NUMAR_FISIERE {len(list)}")

if __name__ == '__main__':
        if len(sys.argv) < 2:
            print("Prea putine argumente la linia de comanda!")
        else:
            directory_path = sys.argv[1]
            count_file_ext(directory_path)
