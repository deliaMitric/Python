#Exercitiul 1
#Write a function to return a list of the first n numbers in the Fibonacci string.
from itertools import zip_longest
def ex1():
    n = int(input("Cate numere din sirul Fibonacci doresti? "))
    first_numbers = []
    if n > 2:
        first_numbers.append(1)
        first_numbers.append(1)

        for index in range(2, n):
            length_list = len(first_numbers)
            current_number = first_numbers[length_list - 1] + first_numbers[length_list - 2]
            first_numbers.append(current_number)
    elif n == 1:
        first_numbers.append(1)

    print(first_numbers)
    return first_numbers

#Exericitiul 2
#Write a function that receives a list of numbers and returns a list of the prime numbers found in it
def ex2(list_of_numbers):
    prime_numbers =[number for number in list_of_numbers if (len([divizor for divizor in (2, number // 2+1) if number % divizor == 0])== 0 and number >= 2) or number == 2]
    print(prime_numbers)
    return prime_numbers

#Exercitiul 3
#Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited with b, a - b, b - a)

def ex3(first_list, second_list):

    list_intersection = list(filter(lambda element: element in first_list, second_list))
    list_reunion = list(set(first_list + second_list))
    difference_first_second = list(filter(lambda element: element not in second_list, first_list))
    difference_second_first = list(filter(lambda element: element not in first_list, second_list))

    print(list_intersection)
    print(list_reunion)
    print(difference_first_second)
    print(difference_second_first)

    return (list_intersection, list_reunion, difference_first_second, difference_second_first)

#Exercitiul 4
# Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers) and a start position (integer).
#The function will return the song composed by going through the musical notes beginning with the start position and following the moves given as parameter.
#Example : compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) will return ["mi", "fa", "do", "sol", "re"]

def ex4(musical_notes, moves, start_position):
    musical_notes_length = len(musical_notes)
    start_position %= musical_notes_length

    result_song = []
    result_song.append(musical_notes[start_position])
    current_position = start_position

    for move in moves:
        current_position = (current_position + move) % musical_notes_length
        result_song.append(musical_notes[current_position])

    print(result_song)
    return result_song

#Exercitul 5
#Write a function that receives as parameter a matrix and# will return the matrix obtained by
# replacing all the elements under the main diagonal with 0 (zero)
def ex5(initial_matrix):
    number_rows = len(initial_matrix)
    number_cols = len(initial_matrix[0])
    if number_cols == number_rows:
        result_matrix = [[initial_matrix[i][j] if i <= j else 0 for j in range(0, number_cols)] for i in range(0, number_rows)]

        for row in result_matrix:
            print(row)
        return result_matrix
    else:
        print("Matricea nu are diagonala principala! Scrieti o matrice patratica!")

#Exercitiul 6
#Write a function that receives as a parameter a variable number of lists and a whole number x.
# Return a list containing the items that appear exactly x times in the incoming lists.
def ex6(x,*lists):
    result_list= []
    big_list = []

    for one_list in lists:
        big_list.extend(one_list)

    for element in big_list:
        if big_list.count(element) == x and element not in result_list:
            result_list.append(element)

    print(result_list)
    return result_list

#Exercitiul 7
#Write a function that receives as parameter a list of numbers (integers)
# and will return a tuple with 2 elements. The first element of the tuple will be the number
# of palindrome numbers found in the list and the second element will be the greatest palindrome number.

def ex7(numbers):
    def palindrome(number):
        mirrored = 0
        number2 = number
        while number > 0:
            mirrored = mirrored * 10 + number % 10;
            number //= 10

        if mirrored == number2:
            return True
        return False

    palindrome_list =[element for element in numbers if palindrome(element)]
    maxim_palindrome = max(palindrome_list)
    print("Lista:",palindrome_list," maximul: ",maxim_palindrome)

    return(palindrome_list,maxim_palindrome)

#Exercitul 8
# Write a function that receives a number x, default value equal to 1, a list of strings,
# and a boolean flag set to True. For each string, generate a list containing the characters that have the ASCII
# code divisible by x if the flag is set to True, otherwise it should contain
# characters that have the ASCII code not divisible by x.

def ex8(strings, flag = True, x = 1):
    final_list = []

    for string in strings:
        if flag == True:
            character_list = [character for character in string if ord(character) % x == 0]
        elif flag == False:
            character_list = [character for character in string if ord(character) % x != 0]
        final_list.extend(character_list)

    print(final_list)
    print(x)
    return final_list

#EXercitiul9

def ex9(seats):
    rows = len(seats)
    cols = len(seats[0])
    final_list = []

    for j in range(0, cols):
        maxim_col = 0
        for i in range(0,rows):
            if seats[i][j] > maxim_col:
                maxim_col = seats[i][j]
            else:
                final_list.append((i, j))
    print(final_list)
    return final_list

#Exercitiul 10
def ex10(*lists):
    final_list = list(zip_longest(*lists))
    print(final_list)

    return final_list

#Exercitul 11
#Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple.
# Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]
def ex11(tuples_list):
    def key_tuple(one_tuple):
        if len(one_tuple) >= 2 and len(one_tuple[1]) >= 3:
            return one_tuple[1][2]
        return '\x00' #pun la incpeut tupla ce nu respecta conditiile

    sorted_list = sorted(tuples_list, key=key_tuple)
    print(sorted_list)
    return sorted_list


def main():
    #ex1()
    #ex2([1,2,4,7,11,24,23,16,100,97])
    #ex2([4,6,8,10,34])
    #ex3([1,2,3,4,5],[3,4,5,6,7])
    #ex4(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2)
    #ex5([[1,2,3],[4,5,6],[7,8,9]])
    #ex6(3,[1, 2, 3, 3, 4, 5],[3, 4, 4, 5, 6, 7],[5, 6, 6, 7, 8, "text"])
    #ex7([121,123321,1234,12, 343])
    #ex8(["test", "hello", "lab002"], x=2)
    #ex9([[1, 2, 3, 2, 1, 1],[2, 4, 4, 3, 7, 2],[5, 5, 2, 5, 6, 4],[6, 6, 7, 6, 7, 5]])
    #ex10([1, 2, 3], [10, 20, 30,40,40], ["a", "b", "c"])
    ex11([('abc', 'bcd'), ('abc', 'zza'),('abc', 'qw'),('abc','z')])

if __name__ == "__main__":
    main()
