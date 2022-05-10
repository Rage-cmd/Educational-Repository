<template>

    <v-app >
        <v-container>    
        </v-container>
        <v-container mt-6>
            <!-- <PostTemplate :postModel="sampleMCQPostData" :currentScreen="currentScreen"/> -->
            <!-- <PostTemplate :postModel="sampleVideoPostData" :currentScreen="currentScreen"/> -->
            <PostTemplate v-for="post in posts" :key="post.id" :postModel="post" :currentScreen="currentScreen"
            @approvepost="postapproveMethod"
            :user="user"/>
                        
        </v-container>        
        
    </v-app>
</template>

<script>
import PostTemplate from "../components/PostTemplate.vue" ;
import {yourUploads,approvepost, pendingApprovals, getSavedPosts} from '../api.js';

export default ({
    setup() {
        
    },
    components:{
        PostTemplate,
    },
    props:{
        currentScreen:String,
        user:Object,
    },
    data: ()=>({
    posts:[],
    selectedTab:null,
    }),
    async created(){
        if(this.currentScreen==="Your Uploads"){
            await yourUploads(this.user.id).then((response)=>{
                this.posts = response.data;
            });
        }
        else if(this.currentScreen==="Pending Approvals"){
            await pendingApprovals(this.user.id).then((response)=>{
                this.posts = response.data;
            });
        }
        else if(this.currentScreen === "Saved Posts"){
            await getSavedPosts(this.user.id).then((response)=>{
                this.posts = response.data;
            });
        }
    },
    methods:{
        async postapproveMethod(post_id){
            await approvepost(post_id).then((response)=>{
                alert(response.data);
                this.posts = this.posts.filter(post => post.id != post_id);
            }).catch((error)=>{
                alert(error);
            });
        },
        }
});
</script>
