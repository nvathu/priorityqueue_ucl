import heapq
class PriorityQueue:
   
    def  __init__(self):
        self.queue=[]
        

    def push(self, item, priority):
        heapq.heappush(self.queue,(priority,item))
        

    def pop(self):
        (priority,item) = heapq.heappop(self.queue)
        return priority,item

    def isEmpty(self):
        return len(self.queue) == 0

    def update(self, item, priority):
        # If item already in priority queue with higher priority, update its priority and rebuild the heap.
        # If item already in priority queue with equal or lower priority, do nothing.
        # If item not in priority queue, do the same thing as self.push.
        
        for n, (p,i) in enumerate(self.queue):
            if(i==item):
                if (p > priority):
                    self.queue[n]=(p,i)
                    heapq.heapify(self.queue)
                return
        self.push(item,priority)        
                
      