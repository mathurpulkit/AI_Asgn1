# runs the main code for the IDS
import ids
import ntile

n = 3
initial_state = [[1,8,2],[0,4,3],[7,6,5]]
init_board = ntile.ntile(n, initial_state)

answer = ids.ids(init_board)
print(answer)