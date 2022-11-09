class state:
    board=0
    remain=0
    k=0
    depth=0
    Aiscore=0
    humanscroe=0
    def __init__(self, board, remain,k,depth,Aiscore,humanscroe):
        self.board=board
        self.remain=remain
        self.k=k
        self.depth=depth
        self.Aiscore=Aiscore
        self.humanscroe=humanscroe

       