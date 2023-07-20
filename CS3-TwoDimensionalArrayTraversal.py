def twoDimensionalArrayTraversal(field, figure):
    position = 0
    deep = 0

    while position <= len(field)-len(figure):

        # Pussh downward until impossible
        while True:
            field_copy = list(field)
            for i in range(3):
                for j in range(3):
                    if field_copy[deep+i][position+j] != 1:
                        field_copy[deep+i][position+j] = figure[i][j]
                    


        
        return position

    return -1



field2 =  [[0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [1, 1, 0, 1, 0],
          [1, 0, 1, 0, 1]]
figure2 = [[1, 1, 1],
          [1, 0, 1],
          [1, 0, 1]]

field1 = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [1, 0, 0],
         [1, 1, 0]]
figure1 = [[0, 0, 1],
          [0, 1, 1],
          [0, 0, 1]]

print(twoDimensionalArrayTraversal(field1, figure1))
print(twoDimensionalArrayTraversal(field2, figure2))