from state import state
class utilities:
    
    def action(sta,type):
        bit=1
        if type=="h":
            bit=0
        actions=[]
        remain=sta.remain-1
        k=sta.k
        depth=sta.dep+1
        for i in range(7):
            temp=sta.board
            temp2=sta.board
            pos=(temp>>(9*i)) & 7
            if (pos)<7:
                next=temp2 |(bit << ( (9*i)+(3+pos) ) )
                pos+=1
                next=temp2 |( 7 <<  (9*i) )
                next=temp2 & ( pos <<  (9*i) )
                actions.append(state(next,remain,k,depth))
        return actions
        