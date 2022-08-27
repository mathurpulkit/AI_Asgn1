#runs the main code for bidirectional search
import bidir
import ntile

initial_state = [[1,8,2],
                 [0,4,3],
                 [7,6,5]]
game1 = ntile.ntile(3, initial_state)

four_by_four = [[5,1,2,3],
                [9,6,7,4], 
                [13,10,11,8],
                [14,15,0,12]]
game2 = ntile.ntile(4, four_by_four)

third_ex = [[15,2,1,12],
            [8,5,6,11],
            [4,9,10,7],
            [3,4,13,0]]
game3 = ntile.ntile(4, third_ex)

ans = bidir.bidirectional_search(game1)
ans2 = bidir.bidirectional_search(game2)
ans3 = bidir.bidirectional_search(game3)
print(ans)
print(ans2)
print(ans3)