#Write a script using the os module that renames all files in a specified directory to have a sequential number prefix.
# For example, file1.txt, file2.txt, etc.
# Include error handling for cases like the directory not existing or files that can't be renamed
import os
import sys


def rename_file(director_path):
    number_of_files = 0
    try:
        if not os.path.exists(director_path):
            raise FileNotFoundError(f"{director_path} nu e gasit!")
        if not os.path.isdir(director_path):
            raise NotADirectoryError(f"{director_path} nu e un director!")

        for element in os.listdir(director_path):
            old_path = os.path.join(director_path, element)

            #verificam daca elemwntul curent este fisier
            if os.path.isfile(old_path):
                number_of_files += 1
                #modificam numele ("pathul") fisierului
                new_name = str(number_of_files) + os.path.basename(old_path)
                new_path = os.path.join(director_path, new_name)
                try:
                    os.rename(old_path, new_path)
                except PermissionError as e:
                    print(f"Nu este permisa schimbarea numelui fisierului {old_path}")
    except FileNotFoundError as e:
        print(e)
    except NotADirectoryError as e:
        print(e)
    except Exception as e:
        print(f"Alta exceptie: {e}")

if __name__ == '__main__':
        if len(sys.argv) < 2:
            print("Prea putine argumente la linia de comanda!")
        else:
            directory_path = sys.argv[1]
            rename_file(directory_path)