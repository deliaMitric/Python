#Create a Python script that does the following:
#Takes a directory path and a file extension as command line arguments (use sys.argv).
#Searches for all files with the given extension in the specified directory (use os module).
#For each file found, read its contents and print them.
#Implement exception handling for invalid directory paths, incorrect file extensions, and file access errors.
import os
import sys
def display_info_fis(director_path, file_extension):
    try:
        file_extension = file_extension.lower()
        valid_ext = [".txt", ".log", ".csv", ".json", ".doc", ".docx", ".pdf"]
        if not os.path.exists(director_path):
            raise FileNotFoundError(f"{director_path} nu e gasit!")
        if not os.path.isdir(director_path):
            raise NotADirectoryError(f"{director_path} nu e un director!")
        if file_extension not in valid_ext:
            raise Exception(f"Extensia {file_extension} este incorecta!")


        for element in os.listdir(director_path):
            complete_path = os.path.join(director_path, element)

            if os.path.isfile(complete_path) and os.path.splitext(complete_path)[1].lower() == file_extension:
                #display infos

                try:
                    file = open(complete_path, "r")
                    print(f"File {complete_path} content: ")
                    for line in file:
                        print(line.strip())
                except FileNotFoundError:
                    print("Fisierul nu a fost gasit!")
                except PermissionError:
                    print("Nu aveti acces pentru a deschide fisierul!")
                except:
                    print("Alta eroare legata de fisiere.")

    except FileNotFoundError as e:
        print(e)
    except NotADirectoryError as e:
        print(e)
    except Exception as e:
        print(f"Another exception: {e.args[0]}")

if __name__ == '__main__':
        if len(sys.argv) < 3:
            print("Prea putine argumente la linia de comanda!")
        else:

            directory_path = sys.argv[1]
            file_extension = sys.argv[2]
            display_info_fis(directory_path, file_extension)
