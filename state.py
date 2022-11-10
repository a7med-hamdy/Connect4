class state:
    def __init__(self, board,col,Aiscore,humanscore,parent= None):
        self.board=board
        self.col=col
        self.Aiscore=Aiscore
        self.humanscore=humanscore
        self.parent=parent

       