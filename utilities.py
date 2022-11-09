from state import state
class utilities:


    def points(self,sta,row,col,B):
        #check vertical
        score=0
        board=sta
        if row>2:
            equal=0
            temp=board
            for i in range(3):
                bit=temp & (1<<((9*col)+3+row-i-1))
                bit=bit>>((9*col)+3+row-i-1)
                equal+=(bit^B)
            if equal==0:
                score+=1

        #check horzontal
        start=col+3
        end=col-3
        while start>6:
            start-=1
        while end<0:
            end+=1


        startr=row+3
        endr=row-3
        while startr>5:
            startr-=1
        while endr<0:
            endr+=1


        tmpend=end

        while tmpend<=start-3:
            equal=0
            exsit=1
            temp=board
            temp2=board
            for i in range(4):
                if (temp>>(9*(tmpend+i)) & 7) > row:
                    exsit=0
                    break
                bit=temp2 & (1<<((9*tmpend+i)+3+row))
                bit=bit>>((9*tmpend+i)+3+row)
                equal+=(bit^B)
            if exsit and equal==0:
                score+=1
            tmpend+=1

        # check left diagonal
        tmpendh=end
        tmpendr=endr
        while tmpendh<=start-3 and tmpendr<=startr-3:
            equal=0
            exsit=1
            temp=board
            temp2=board
            j=tmpendr
            for i in range(4):
                if (temp>>(9*(tmpendh+i)) & 7) >= j:
                    exsit=0
                    break
                bit=temp2 & (1<<((9*tmpend+i)+3+j))
                bit=bit>>((9*tmpend+i)+3+j)
                equal+=(bit^B)
            if exsit and equal==0:
                score+=1
            tmpendh+=1
            tmpendr+=1


        tmpendh=start
        tmpendr=endr
        # check right diagonal 
        while tmpendh<=start-3 and tmpendr<=startr-3:
            equal=0
            exsit=1
            temp=board
            temp2=board
            j=tmpendr
            for i in range(4):
                if (temp>>(9*(tmpendh+i)) & 7) >= j:
                    exsit=0
                    break
                bit=temp2 & (1<<((9*tmpend+i)+3+j))
                bit=bit>>((9*tmpend+i)+3+j)
                equal+=(bit^B)
            if exsit and equal==0:
                score+=1
            tmpendh-=1
            tmpendr+=1
        
        return score


    def action(self,sta,type):
        bit=1
        score=sta.Aiscore
        if type=="h":
            bit=0
          
        actions=[]
        scoreh=sta.humanscroe
        score=sta.Aiscore
        remain=sta.remain-1
        k=sta.k
        depth=sta.dep+1
        for i in range(7):
            temp=sta.board
            temp2=sta.board
            row=(temp>>(9*i)) & 7
            row=row>>(9*i)
            if (row)<7:
                next=temp2 |(bit << ( (9*i)+(3+row) ) )
                row+=1
                next=temp2 |( 7 <<  (9*i) )
                next=temp2 & ( row <<  (9*i) )
                z=self.points(next,row,i,bit)
                if type=="h":
                    actions.append(state(next,remain,k,depth,score,scoreh+z))
                else:
                    actions.append(state(next,remain,k,depth,score+z,score))

        return actions



    def heuristic(self,sta):
        Aiscore=0.0
        humanscore=0.0
        # check points for computer
        for i in range(7):
            temp=sta
            temp2=sta
            row=(temp>>(9*i)) & 7
            row=row>>(9*i)
            if (row)<7:
                next=temp2 |(1 << ( (9*i)+(3+row) ) )
                row+=1
                next=temp2 |( 7 <<  (9*i) )
                next=temp2 & ( row <<  (9*i) )
                z=self.points(next,row,i,1)
                Aiscore+=z
            
        # check points for player
        for i in range(7):
            temp=sta
            temp2=sta
            row=(temp>>(9*i)) & 7
            row=row>>(9*i)
            if (row)<7:
                next=temp2 |(0 << ( (9*i)+(3+row) ) )
                row+=1
                next=temp2 |( 7 <<  (9*i) )
                next=temp2 & ( row <<  (9*i) )
                z=self.points(next,row,i,0)
                humanscore+=z
        return Aiscore-humanscore        
        # check potential score for computer
        # check potential score for player
        