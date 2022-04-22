# Sample Database Sketch

## Users

No. of users: 5

User IDs: [u1, u2, u3, u4, u5]


## Tags

No. of tags: 5

Tag names and IDs: 
```
[
    {
        "id": 1,
        "name": "tag1"
    },
    {
        "id": 2,
        "name": "tag2"
    },
    {
        "id": 3,
        "name": "tag3"
    },
    {
        "id": 4,
        "name": "tag4"
    },
    {
        "id": 5,
        "name": "tag5"
    }
]
```



### Adjacency list of tags

```
tag1 -> [tag2, tag3]
tag2 -> []
tag3 -> [tag4, tag5]
tag4 -> []
tag5 -> []
```



## Posts

No. of posts: 6

Post IDs: [p1, p2, p3, p4, p5, p6]

### Authors vs posts


| Author | Posts     |
| ------ | --------- |
| u1     | [p1, p2,] |
| u2     | [p3]      |
| u3     | [p4]      |
| u4     | [p5]      |
| u5     | [p6]      |


### Posts vs Parent Tags


| Post | Parent Tag  |
| -----| ----------- |
| p1   | [tag2]      |
| p2   | [tag2,]     |
| p3   | [tag4,]     |
| p4   | [tag5,]     |
| p5   | [tag5,]     |
| p6   | [tag5,]     |
