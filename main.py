from search import search
from state import state


if __name__== "__main__":
    board = 0
    s = search()
    while(True):
        print(f"{board: b}")
        a = int(input("enter column number "))
        while a > 6:
            a = int(input("error enter column number "))
        temp = board
        x = 1
        for i in range(a):
            x = x << 9
        temp = temp + x
        board = temp
        stat = s.search(state(board, a,0, 0, 0),"AI",5,alpha=None,beta=None)
        #s.print_nodes_edges()
        #print(stat)
        board = stat.board

        

