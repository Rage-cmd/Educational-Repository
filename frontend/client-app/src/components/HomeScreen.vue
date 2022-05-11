<template>

    <v-app >
        <!-- <NavBar/> -->
        <v-container mt-6>
            <v-tabs
                v-model="selectedTab"
                color="primary"
                slider-color="primary"
                fixed-tabs
            >
                <v-tab>
                    Most Recent 
                </v-tab>
               

                <v-tab>
                    Most Commented
                </v-tab>
                    
                    <v-tab-item>
                        <!-- <PostTemplate :postModel="sampleVideoPostData"/>
                        <PostTemplate :postModel="sampleMCQPostData"/> -->
                        <PostsList :currentScreen="currentScreen" :user="user"/>
                    </v-tab-item>
                    
                    <v-tab-item>
                        <PostTemplate :postModel="sampleMCQPostData"/>
                        <PostTemplate :postModel="sampleVideoPostData"/>
                        
                    </v-tab-item>
            </v-tabs>
        </v-container>        
        
    </v-app>
</template>

<script>
import PostTemplate from "../components/PostTemplate.vue";
// import NavBar from "../components/NavBar/NavBar.vue";
import PostsList from "./PostsList.vue"

export default ({
    setup() {
        
    },
    components:{
        PostTemplate,
        PostsList,
        // NavBar,
    },
    props:{
        user:Object,
    },
    data: ()=>({
    sampleVideoPostData:{
    "caption":"Hospital Data Management Project",
    "is_answered":true,
    "text":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Quos recusandae nesciunt ad voluptate aperiam exercitationem veritatis laudantium totam a, natus inventore, sunt unde laborum nam obcaecati neque. Velit, obcaecati quas. Lorem ipsum dolor, sit amet consectetur adipisicing elit. Aperiam temporibus optio deserunt, at odit dolorem nostrum magnam dolores sequi delectus, corporis reiciendis. Provident tempora minus maiores iure, cum fugit quasi.",
    "video_url":"https://drive.google.com/file/d/13zHw-vwAWZCUhjFo4QVs7OcHqRqMj7ed/preview",
    "type":"video",
    "user":"user1",
    "time":"2020-06-01T00:00:00.000Z",
    "tags": ["t4","t5"],
    "author":{
    "_id": "6277a3ab8fb52aafb4294872",
    "id": "u2",
    "name": "John Doe",
    "email": "user@example.com",
    "password": "password",
    "access_level": "user",
    "status": "active",
    "posts": [
        "p1"
    ],
    "comments": [
        "c13",
        "c66"
    ],
    "saved_posts": [
        "p2"
    ],
    "liked_posts": [
        "p32",
        "p62"
    ],
    "points": 100,
    "profile_picture": "https://cdn.vuetifyjs.com/images/lists/1.jpg",
    "no_of_bans": 0,
    "is_banned": false
},
"upvotess":10,
"is_approved":true,
"comments":[
    "c13",
    "c66"
],
"reports":2,

    },
    currentScreen:"Most Recent",
    sampleMCQPostData:{
      "is_answered":false,
      "caption":"Find the value of x",
      "time":"2020-06-01T00:00:00.000Z",
      "text":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Quos recusandae nesciunt ad voluptate aperiam exercitationem veritatis laudantium totam a, natus inventore, sunt unde laborum nam obcaecati neque. Velit, obcaecati quas. Lorem ipsum dolor, sit amet consectetur adipisicing elit. Aperiam temporibus optio deserunt, at odit dolorem nostrum magnam dolores sequi delectus, corporis reiciendis. Provident tempora minus maiores iure, cum fugit quasi.",
      "image_url":"https://hi-static.z-dn.net/files/d62/0c3678b43230a26c13d6f16947d28a03.jpg",
      "type":"Text",
      "tags": ["t4","t5"],
      "options":["option1", "option2", "option3"],
      "author": {
        "_id": "6277a3ab8fb52aafb4294872",
        "id": "u2",
        "name": "John Doe",
        "email": "user@example.com",
        "password": "password",
        "access_level": "user",
        "status": "active",
        "posts": [
            "p1"
        ],
        "comments": [
            "c13",
            "c66"
        ],
        "saved_posts": [
            "p2"
        ],
        "liked_posts": [
            "p32",
            "p62"
        ],
        "points": 100,
        "profile_picture": "https://example.com/profile.png",
        "no_of_bans": 0,
        "is_banned": false
    },
    "upvotess":10,
    "is_approved":true,
    "comments":[
        "c13",
        "c66"
    ],
    "reports":2,
    },
    selectedTab:null,
    }),

    watcher:{
        selectedTab(newValue){
            if(newValue === 0){
                this.currentScreen = "Most Recent";
            }else{

                this.currentScreen = "Most Commented";
            }
        }
    },

})
</script>
