'''
This is example demo of multiple key sorting feature in python 
It uses itemgetter from operator and sorted (method).
'''
def main():
    table = [
                    ["Co","tableCo","4","1","1","C8C8C8","3296FA"],
                    ["Mo","tableMo","1","1","1","AAFFFF","3296FA"],
                    ["Se","tableSe","1","2","1","FFFFC8","3296FA"],
                    ["St","tableSt","3","1","1","FFFFFF","3296FA"]
                ]
    print('\n\n'+'*'*90)
    print("\t\t\t unsorted table")
    printTableWithhighlighting(table)


    from operator import itemgetter

    sortedList = sorted(table, key = itemgetter(3,2))
    print('\n\n'+'*'*90)
    print("\t\t\tsortedList by indexes 3 and then 2")
    printTableWithhighlighting(sortedList,3,2)

    sortedList = sorted(table, key = itemgetter(2,3))
    print('\n\n'+'*'*90)
    print("\t\t\tSortedList by indexes 2 and then 3")
    printTableWithhighlighting(sortedList,2,3)


def printTableWithhighlighting(table, index1=None, index2=None):
    print('*'*90)
    for row in table:
        counter = 0
        for item in row:
            if counter == index1:
                print("\033[92m {}\033[00m\t".format(item)).expandtabs(10),
            elif counter == index2:
                print("\033[91m {}\033[00m\t".format(item)).expandtabs(10),
            else:
                print("\033[94m {}\033[00m\t".format(item)).expandtabs(10),
            counter +=1 
        print('') 
    print('*'*90)

if __name__ == "__main__":
    main()
