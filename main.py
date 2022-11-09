

from search import search
from state import state


if __name__== "__main__":
    board = 0
    s = search()
    while(True):
        print(f"{board: b}")
        a = int(input("enter column number"))
        temp = board
        x = 1
        for i in range(a):
            x = x << 9
        temp = temp + x
        board = temp
        print(s.search(state(board, 0, 0, 0, 0),"AI",4,None,None))

        

