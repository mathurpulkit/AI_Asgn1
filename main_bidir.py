#runs the main code for bidirectional search
import bidir
import ntile
import time
initial_game = [[1,8,2],
                 [0,4,3],
                 [7,6,5]]
game1 = ntile.ntile(3, initial_game)

four_by_four = [[5,1,2,3],
                [9,6,7,4], 
                [13,10,11,8],
                [14,15,0,12]]
game2 = ntile.ntile(4, four_by_four)

five_by_five = [[1,0,2,4,5],
                [6,7,3,8,10],
                [11,12,9,13,15],
                [16,17,18,14,19],
                [21,22,23,24,20]]
game3 = ntile.ntile(5, five_by_five)

tough_ex = [[15,2,1,12],
            [8,5,6,11],
            [4,9,10,7],
            [3,4,13,0]]
game4 = ntile.ntile(4, tough_ex)

tic = time.time()
ans = bidir.bidirectional_search(game1)
toc = time.time()
print(ans, "\ntime:", toc-tic)
tic = time.time()
ans2 = bidir.bidirectional_search(game2)
toc = time.time()
print(ans2, "\ntime:", toc-tic)
tic = time.time()
ans3 = bidir.bidirectional_search(game3)
toc = time.time()
print(ans3, "\ntime:", toc-tic)
tic = time.time()
ans4 = bidir.bidirectional_search(game4)
toc = time.time()
print(ans4, "\ntime:", toc-tic)