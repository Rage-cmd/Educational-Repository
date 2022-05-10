from queue import PriorityQueue
# from datetime import datetime

class CacheImpl:
    
    
    def __init__(self, maxSize=1):
        self.most_recent_cache = PriorityQueue()
        self.most_upvoted_cache = PriorityQueue()
        self.maxItems = maxSize
    
    def addItem_recent_cache(self,doc, datetime):
        insertItem = (datetime,doc)
        if len(self.most_recent_cache.queue) >= self.maxItems:
            removedItem = (self.most_recent_cache).get()
            insertItem = max(removedItem,insertItem)
        (self.most_recent_cache).put(insertItem)

    
    def getAllItems_recent_cache(self):
        posts = []
        for i in range(len(self.most_recent_cache.queue)):
            posts.append(self.most_recent_cache.queue[i][1])
        return posts

    def addItem_upvote_cache(self,id, upvotes):
        insertItem = (-upvotes,id)
        if len(self.most_upvoted_cache.queue) >= self.maxItems:
            removedItem = (self.most_upvoted_cache).get()
            insertItem = min(removedItem, insertItem)
        (self.most_upvoted_cache).put(insertItem)

    def getAllItems_upvote_cache(self):
        postIds=[]
        for i in range(len(self.most_upvoted_cache.queue)):
            postIds.append(self.most_upvoted_cache.queue[i][1])
        return postIds

    def addItem_comment_cache(self,post, upvotes):
        insertItem = (-upvotes,post)
        if len(self.most_upvoted_cache.queue) >= self.maxItems:
            removedItem = (self.most_upvoted_cache).get()
            insertItem = min(removedItem, insertItem)
        (self.most_upvoted_cache).put(insertItem)

    def getAllItems_comment_cache(self):
        posts=[]
        for i in range(len(self.most_upvoted_cache.queue)):
            posts.append(self.most_upvoted_cache.queue[i][1])
        return posts


    def clear_cache(self):
        self.most_recent_cache = PriorityQueue()
        self.most_upvoted_cache = PriorityQueue()
        return True
        
# cache = CacheImpl(2)

# cache.addItem_recent_cache(1,datetime.now())
# cache.addItem_recent_cache(2,datetime(2019,1,1,0,0,0))
# cache.addItem_recent_cache(3,datetime(2020,1,1,0,0,0))

# cache.addItem_upvote_cache(1,4)
# cache.addItem_upvote_cache(3,10)
# cache.addItem_upvote_cache(2,11)

# print(cache.getAllItems_recent_cache())
# print(cache.getAllItems_upvote_cache())

