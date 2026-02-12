from queue import PriorityQueue
def topKFrequent(words, k):
        q=PriorityQueue()
        word_dict={}
        for item in words:
            if item in word_dict:
                word_dict[item]+=1
            else:
                word_dict[item]=1
        for item in word_dict.items():
            q.put((-item[1],item[0]))
        res=[]
        for i in range(k):
            res.append(q.get()[1])
        return res

