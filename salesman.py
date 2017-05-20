import math

#data is the lst with coordinates of the cities

def tsp(data):
    matrix = []
    path = list()
    length = 0
    for el in data:
        temp_row = []
        for ele in data:
            if el == ele:
                temp_row.append(math.inf)
            else:
                temp_row.append(decart_dist(el, ele))
        matrix.append(temp_row)

    pointer = matrix[0]
    path.append(0)
    while len(path) != len(matrix):
        ind_min = pointer.index(min(pointer))
        if ind_min not in path:
            path.append(ind_min)
            length += pointer[ind_min]
            pointer = matrix[ind_min]


        else:
            ind_min = pointer.index(min(pointer))

            while ind_min in path:
                pointer[ind_min] = math.inf
                print(pointer)
                ind_min = pointer.index(min(pointer))
            path.append(ind_min)
            length += pointer[ind_min]
            pointer = matrix[ind_min]
    length += pointer[0]
    path.append(0)
    return length, path



def another_min(ind_min, pointer):
    pass

def decart_dist(el, ele):
    dist = math.sqrt((ele[0]-el[0])**2 + (ele[1]-el[1])**2)
    return dist

def demo_m(matrix):
    for el in matrix:
        for ele in el:
            if el.index(ele) != len(el)-1:
                print(ele, end=' ')
            else:
                print("\n")


def description():
    return "Takes data list with the coordinates of the cities \n and makes the matrix of distances, using the method decart_dist(el, ele) (by looking for the decart distance). If the two elements are the same, writes their distance as inf (to prevent taking this distance as minimum distance). \n The start of the path is 0. Starting from zero-sublist, takes the sublists of a matrix and looks for index of the minimum element, then adds it to the path (if element is already in the path, changes its value to inf and searches for index of the minimum element again) \n The next sublist to consider will be matrix[index of the min. element]. After all, to return to the initial city, we append 0 to the path list. \n === \n To find length of the route we add all minimal elements from matrix, whose indexes were taken to the list"




