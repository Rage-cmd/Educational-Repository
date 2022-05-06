from datetime import datetime
from backend.educationalRepository.databaseInterfaces.mongoDB_interface import *
from backend.educationalRepository.databaseInterfaces.drive_api import *
from backend.educationalRepository.repositoryAPI.Caching.cache_impl import *
import numpy as np
import random
import time
import collections
import matplotlib.pyplot as plt

def insert_tag(tag_name, parents, id=None):
    """
    Inserts a tag in the tag_tree collection. It also adds the tag ID in the main_tree collection.

    Parameters:
        tag_name (str) : The name of the tag.
        parents (list) : The list of parent tag IDs.

    Returns:
        tag_id (str) : The id of the tag.

    """

    # try :
    if id is None:
        tag_id = 't' + str(getNextSequenceValue("test_db","tagtree_collection"))
    else:
        tag_id = id
    tag_doc = {
        "id": tag_id,
        "name": tag_name,
        "path_to_tag": parents,
    }

    saveSingleDocument("test_db","tagtree_collection",tag_doc)
    updateDocument("test_db","maintree_collection",{"id":parents[-1]},{"$push": {"children_tags":tag_id}})

    # parent_folder_id = findSingleDocument("test_db","maintree_collection",{"id":parents[-1]})["drive_id"]

    # file = create_folder(tag_name,[parent_folder_id])

    main_tree_node_doc = {
        "id": tag_id,
        "name": tag_name,
        "type" : "tag",
        "children_tags": [],
        "children_posts": [],
        'drive_id': 'dfga' #file['id'],
    }

    saveSingleDocument("test_db","maintree_collection",main_tree_node_doc)
    return tag_id
    # except:
        # print("Could not insert tag. Check if the parents are valid.")
        # return None


def delete_random_elements(input_list, n):
    to_delete = set(random.sample(input_list, n))
    return to_delete


def generate_random_tag_tree(n):
    queue = [0]
    nodes = range(1,n+1)
    
    file = create_folder('tag0',None)
    main_tree_node_doc = {
        "id": 't0',
        "name": 'tag0',
        "type": 'tag',
        'children_tags':[],
        'children_posts':[],
        'drive_id': file['id'],
        }

    global root_id_drive
    root_id_drive = file['id']

    saveSingleDocument("test_db","maintree_collection",main_tree_node_doc)

    while nodes and queue:
        r = random.randint(1,len(nodes))
        div_facts = [1,2,3,4]
        div_fact = random.choice(div_facts)
        children = delete_random_elements(nodes, r//div_fact)
        nodes = [i for i in nodes if i not in children]
        # print(children,nodes)
        q_front = queue.pop(0)
        queue.extend(children)

        for i in children:
            path = [j for j in path_dict[q_front]]
            path_dict[i] = path
            path_dict[i].append(i)
            ids = ['t'+str(i) for i in path_dict[i][:-1]]
            # print(ids)
            insert_tag('tag'+str(i), ids, id='t'+str(i))


def print_tag():
    tag_tree = findAllDocument("test_db","tagtree_collection",{})
    for node in tag_tree:
        print(node['id'], "--->", node["path_to_tag"])


def create_posts(n):
    posts = []
    for i in range(n):
        tags = random.choice(list(path_dict.values()))
        tags = tags[:-1]
        posts.append({
        'id': 'p' + str(i),
        'type': 'text',
        'time': '2020-01-01T00:00:00Z',
        'tags': tags,
        'caption': 'P' + str(i) + 'Caption',
        'text': 'This is a test post',
        'author': 'u' + str(random.randint(1,n//2)),
        'upvotes': random.randint(1,100),
        'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKboCkjXUKztIj7P8a5UjeFn0lAMQSp_TqhQ&usqp=CAU',
        'is_answered': bool(random.getrandbits(1)),
        'is_approved': bool(random.getrandbits(1)),
        'comments': ['c13', 'c66'],
        'reports': 2
    },)
        cache.addItem_recent_cache(posts[-1]['id'], datetime.now())
        cache.addItem_upvote_cache(posts[-1]['id'], posts[-1]['upvotes'])
    
    
    
    saveMultipleDocuments('test_db',"posts_collection",posts)


def post_ID_search(post_id):
    post = findSingleDocument("test_db","posts_collection",{"id":post_id})
    return post

def post_name_search(post_name):
    posts = findAllDocument("test_db","posts_collection",{"caption": {"$regex": post_name}})
    result = []
    for post in posts:
        result.append(post)
    return result

def tag_ID_search(tag_id):
    main_tree_node = findSingleDocument("test_db","maintree_collection",{"id":tag_id})
    post_nodes = []
    queue = [main_tree_node]
    while queue:
        node = queue.pop(0)
        if node['type'] == 'post':
            post_nodes.append(node)
        for child in node['children_tags']:
            queue.append(findSingleDocument("test_db","maintree_collection",{"id":child}))
        for child in node['children_posts']:
            queue.append(findSingleDocument("test_db","maintree_collection",{"id":child}))
    
    result = []
    for post in post_nodes:
        result.append(findSingleDocument("test_db","posts_collection",{"id":post['id']}))
    return result

path_dict = collections.defaultdict(list)
path_dict[0] = [0]

def fetch_most_liked_posts(n):
    posts = findAllDocument("test_db","posts_collection",{})
    posts = sorted(posts, key=lambda x: x['upvotes'], reverse=True)
    return posts[:n]

def fetch_latest_posts(n):
    posts = findAllDocument("test_db","posts_collection",{})
    posts = sorted(posts, key=lambda x: x['time'], reverse=True)
    return posts[:n]

def delete_db():
    # delete database

    deleteDatabase("test_db")

    global root_id_drive
    if root_id_drive:
        remove_folder(root_id_drive)
        root_id_drive = None

    cache.clear_cache()

def simulate_search_ID_algorithms(n):

    # generate_random_tag_tree(n//5)
    # create_posts(n)
    times = []
    no_of_ids =[]
    posts = ['p' + str(i) for i in range(1,n+1)]

    for i in range(2,n):
        delete_db()
        test_db = createDatabase("test_db")

        if i < 50:
            generate_random_tag_tree(i)
        else:
            generate_random_tag_tree(i//5)

        create_posts(i)
        avg = []
        for j in range(4):
            start = time.time()
            search_id = random.sample(posts,1)
            post_ID_search(search_id[0])
            end = time.time()
            avg.append(end-start)
        
        times.append(sum(avg)/len(avg))
        no_of_ids.append(i)

    plt.plot(no_of_ids,times)
    plt.grid(True)
    plt.xlabel('No of Posts')
    plt.ylabel('Time')
    plt.title("Time taken to search for a post ID")
    plt.legend(['ID Search'])
    plt.show()


def simulate_search_name_algorithms(n):
    
    times = []
    no_of_posts =[]
    post_captions = ['P' + str(i) + 'Caption' for i in range(0,n)]
    
    for i in range(n):
        delete_db()
        test_db = createDatabase("test_db")

        if i < 50:
            generate_random_tag_tree(i)
        else:
            generate_random_tag_tree(i//5)

        avg = []
        for j in range(4):
            start = time.time()
            post_name = random.sample(post_captions,1)
            post_name_search(post_name[0])
            end = time.time()
            avg.append(end-start)
        
        times.append(sum(avg)/len(avg))
        no_of_posts.append(i)

    plt.plot(no_of_posts,times)
    plt.grid(True)
    plt.xlabel('No of posts')
    plt.ylabel('Time taken')
    plt.title('Time taken to search for posts by name')
    plt.legend(['Search by name'])
    plt.show()


def simulate_cache_latest(n):
    time_cache = []
    time_no_cache = []
    no_of_posts =[]
    
    for i in range(20,n):
        delete_db()
        test_db = createDatabase("test_db")
        generate_random_tag_tree(i)
        create_posts(i)

        avg_no_cache = []
        for j in range(4):
            start = time.time()
            fetch_latest_posts(10)
            end = time.time()
            avg_no_cache.append(end-start)
        
        avg_cache = []
        for j in range(4):
            start = time.time()
            post_ids = cache.getAllItems_recent_cache()
            # for post_id in post_ids:
            #     findSingleDocument("test_db","posts_collection",{"id":post_id})
            end = time.time()
            avg_cache.append(end-start)
        

        time_cache.append(sum(avg_cache)/len(avg_cache))
        time_no_cache.append(sum(avg_no_cache)/len(avg_no_cache))
        no_of_posts.append(i)

    plt.plot(no_of_posts,time_cache,'r',label='Cache')
    plt.plot(no_of_posts,time_no_cache,'b',label='No-Cache')
    plt.grid(True)
    plt.xlabel('No of posts')
    plt.ylabel('Time taken')
    plt.title('Time taken to search for the top 10 latest posts\n Cache vs No Cache')
    plt.legend(loc='best')
    plt.show()


def simulate_cache_most_liked(n):
    time_cache = []
    time_no_cache = []
    no_of_posts =[]
    
    for i in range(20,n):
        delete_db()
        test_db = createDatabase("test_db")
        generate_random_tag_tree(i)
        create_posts(i)

        avg_no_cache = []
        for j in range(4):
            start = time.time()
            fetch_most_liked_posts(10)
            end = time.time()
            avg_no_cache.append(end-start)
        
        avg_cache = []
        for j in range(4):
            start = time.time()
            post_ids = cache.getAllItems_upvote_cache()
            # for post_id in post_ids:
            #     findSingleDocument("test_db","posts_collection",{"id":post_id})
            end = time.time()
            avg_cache.append(end-start)
        

        time_cache.append(sum(avg_cache)/len(avg_cache))
        time_no_cache.append(sum(avg_no_cache)/len(avg_no_cache))
        no_of_posts.append(i)

    plt.plot(no_of_posts,time_cache,'r',label='Cache')
    plt.plot(no_of_posts,time_no_cache,'b',label='No-Cache')
    plt.grid(True)
    plt.xlabel('No of posts')
    plt.ylabel('Time taken')
    plt.title('Time taken to search for the top 10 liked posts\n Cache vs No Cache')
    plt.legend(loc='best')
    plt.show()

root_id_drive = None
cache = CacheImpl(10)


delete_db()

# create new
test_db = createDatabase("test_db")

simulate_search_ID_algorithms(200)

# simulate_search_name_algorithms(200)

# simulate_cache_latest(200)
# simulate_cache_most_liked(200)

# generate_random_tag_tree(100)