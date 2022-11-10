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


        #check horizontal bounderis
        start=col+3
        end=col-3
        while start>6:
            start-=1
        while end<0:
            end+=1
         

        #check horizontal
        while end<=start-3:
            equal=0
            exist=1
            for i in range(4):
                temp=board
                temp2=board
                if (temp>>(9*(end+i)) & 7) <= row:
                    exist=0
                    break
                bit=temp2 & (1<<((9*(end+i))+3+row))
                bit=bit>>((9*(end+i))+3+row)
                equal+=(bit^B)
            if exist==1 and equal==0:
                score+=1
            end+=1


        # left diagonal boundires
        uperleft=[row,col]
        lowerright=[row,col]
        uper=0
        lower=0
        while uperleft[0]<5 and uperleft[1]<6 and uper<3:
            uperleft[0]=uperleft[0]+1
            uperleft[1]=uperleft[1]+1
            uper+=1
        while lowerright[0]>0 and lowerright[1]>0 and lower<3:
            lowerright[0]=lowerright[0]-1
            lowerright[1]=lowerright[1]-1
            lower+=1   

        # check left diagonal
        while lowerright[1]<=uperleft[1]-3 and lowerright[0]<=uperleft[0]-3:
            equal=0
            exist=1
            for i in range(4):
                temp=board
                temp2=board
                if (temp>>(9*(lowerright[1]+i)) & 7) <= lowerright[0]+i:
                    exist=0
                    break
                bit=temp2 & (1<<((9*(lowerright[1]+i))+3+lowerright[0]+i))
                bit=bit>>((9*(lowerright[1]+i))+3+lowerright[0]+i)
                equal+=(bit^B)
            if exist==1 and equal==0:
                score+=1
            lowerright[1]+=1
            lowerright[0]+=1

        # left diagonal boundires
        uperright=[row,col]
        lowerleft=[row,col]
        uper=0
        lower=0
        while uperright[0]<5 and uperright[1]>0 and uper<3:
            uperright[0]=uperright[0]+1
            uperright[1]=uperright[1]-1
            uper+=1
        while lowerleft[0]>0 and lowerleft[1]<6 and lower<3:
            lowerleft[0]=lowerleft[0]-1
            lowerleft[1]=lowerleft[1]+1
            lower+=1   

        # check right diagonal 
        while  lowerleft[1]>=uperright[1]+3 and lowerleft[0]<=uperright[0]-3:
            equal=0
            exist=1
    
            for i in range(4):
                temp=board
                temp2=board
                if (temp>>(9*(lowerleft[1]-i)) & 7) <= lowerleft[0]+i:
                    exist=0
                    break
                bit=temp2 & (1<<((9*(lowerleft[1]-i))+3+lowerleft[0]+i))
                bit=bit>>( (9*(lowerleft[1]-i)+3+lowerleft[0]+i) )
                equal+=(bit^B)
            if exist==1 and equal==0:
                score+=1
            lowerleft[1]-=1
            uperright[0]+=1
        return score


    def action(self,sta,type):
        bit=1
        if type=="h":
            bit=0
          
        actions=[]
        scoreh=sta.humanscore
        score=sta.Aiscore
        for i in range(7):
            temp=sta.board
            temp2=sta.board
            row=(temp>>(9*i)) & 7
            if (row)<6:
                temp2=temp2 + ( 1 <<  (9*i) )
                next=temp2 |(bit << ( (9*i)+(3+row) ) )
                z=self.points(next,row,i,bit)
                if type=="h":
                    actions.append(state(next,i,score,scoreh+z,sta))
                else:
                    actions.append(state(next,i,score+z,scoreh,sta))

        return actions



    def heuristic(self,sta):
        Aiscore=0.0
        humanscore=0.0

        # check points for computer
        for i in range(7):
            temp=sta.board
            temp2=sta.board
            row=(temp>>(9*i)) & 7
            if (row)<6:
                next=temp2 |(1 << ( (9*i)+(3+row) ) )
                next=next + ( 1 <<  (9*i) )
                z=self.points(next,row,i,1)
                Aiscore+=z
        
            
        # check points for player
        for i in range(7):
            temp=sta.board
            temp2=sta.board
            row=(temp>>(9*i)) & 7
            if (row)<6:
                next=temp2 |(0 << ( (9*i)+(3+row) ) )
                next=next + ( 7 <<  (9*i) )
                z=self.points(next,row,i,0)
                humanscore+=z
        return (Aiscore+sta.Aiscore)-(humanscore+sta.humanscore)

        # check potential score for computer
        # check potential score for player

    #update gui state
    def update(self,board,col):
        temp=board + (1<<(9*col) )
        return temp
