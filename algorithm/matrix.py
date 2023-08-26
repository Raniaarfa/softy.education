
import pprint

def create_matrix():
    number_of_rows =int(input("Enter the number of rows : "))
    number_of_columns = int(input("Enter the number of columns : "))

    matrix = []

    for i in range(number_of_columns):
        column= []
        for j in range(number_of_rows):
            number = int(input("Enter a number : "))
            column.append(number)
        matrix.append(column)
    
    # for x in range(number_of_rows):
    #     row = []
    #     for y in range(number_of_columns):
    #         number = int(input("Enter a number : "))
    #         row.append(number)
    #     matrix.append(row)
    
    pprint.pprint(matrix)

create_matrix()