#Create a Python script that calculates the total size of all files in a directory provided as a command line argument.
#The script should:
#Use the sys module to read the directory path from the command line.
#Utilize the os module to iterate through all the files in the given directory and its subdirectories.
#Sum up the sizes of all files and display the total size in bytes.
#Implement exception handling for cases like the directory not existing, permission errors, or other file access issues.
import sys
import os

def calculate_size(directory_path):
    dimension = 0
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"{directory_path} nu e gasit!")
        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"{directory_path} nu e un director!")

        for root, subdirectories, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    file_dimension = os.path.getsize(file_path)
                except PermissionError as e:
                    print(f"Eroare de permisiune pentur fisierul {file_path}")
                except Exception as e:
                    print(f"Alta exceptie: {e}")
                else:
                    dimension += file_dimension

    except FileNotFoundError as e:
        print(e)
    except NotADirectoryError as e:
        print(e)
    except Exception as e:
        print(f"Alta exceptie: {e}")
    else:
        print(f"Suma dimensiunilor fisierelor: {dimension} bytes")


if __name__ == '__main__':
        if len(sys.argv) < 2:
            print("Prea putine argumente la linia de comanda!")
        else:
            directory_path = sys.argv[1]
            calculate_size(directory_path)