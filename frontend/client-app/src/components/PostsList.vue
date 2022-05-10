<template>

    <v-app >
        <v-container>    
        </v-container>
        <v-container mt-6>
            <!-- <PostTemplate :postModel="sampleMCQPostData" :currentScreen="currentScreen"/> -->
            <!-- <PostTemplate :postModel="sampleVideoPostData" :currentScreen="currentScreen"/> -->
            <div :key="reloadPosts">

            <PostTemplate v-for="post in getPosts" :key="post.id" :postModel="post" :currentScreen="currentScreen"
            @approvepost="postapproveMethod"
            :user="user"
            @removePost="removePost"
            @postLike="postLikeHandler"
            @verifyComment="verifyComment"/>
                        
            </div>
        </v-container>        
        
    </v-app>
</template>

<script>
import PostTemplate from "../components/PostTemplate.vue" ;
import {yourUploads,approvepost, pendingApprovals, getSavedPosts, likePost, getLatestPosts, getMostCommentedPosts} from '../api.js';

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
    postsKey:true,
    posts:[],
    selectedTab:null,
    reloadPosts:false,
    }),
    async created(){
        if(this.currentScreen==="Your Uploads"){
            await yourUploads(this.user.id).then((response)=>{
                this.$store.commit('setPosts', response.data);
            });
        }
        else if(this.currentScreen==="Pending Approvals"){
            await pendingApprovals(this.user.id).then((response)=>{
                this.$store.commit('setPosts', response.data);
            });
        }
        else if(this.currentScreen === "Saved Posts"){
            await getSavedPosts(this.user.id).then((response)=>{
                this.$store.commit('setPosts', response.data);
            });
        }
        else if(this.currentScreen === "Most Recent"){
            await getLatestPosts().then((response)=>{
                this.$store.commit('setPosts', response.data);
            });
        }else if(this.currentScreen === "Most Commented"){
            await getMostCommentedPosts().then((response)=>{
                this.$store.commit('setPosts', response.data);
            });
        }
    },
    computed:{
        getPosts(){
            return this.$store.state.posts;
        }
    },
    methods:{
        async fetchPostList(){
            if(this.currentScreen==="Your Uploads"){
            await yourUploads(this.user.id).then((response)=>{
                this.$store.commit('setPosts', response.data);
            });
            }
            else if(this.currentScreen==="Pending Approvals"){
                await pendingApprovals(this.user.id).then((response)=>{
                    this.$store.commit('setPosts', response.data);
                });
            }
            else if(this.currentScreen === "Saved Posts"){
                await getSavedPosts(this.user.id).then((response)=>{
                    this.$store.commit('setPosts', response.data);
                });
            }
        },
        async postapproveMethod(post_id){
            await approvepost(post_id).then((response)=>{
                alert(response.data);
                this.posts = this.posts.filter(post => post.id != post_id);
            }).catch((error)=>{
                alert(error);
            });
        },
        removePost(post_id){
            this.posts = this.posts.filter(post => post.id != post_id);
            this.postsKey = !this.postsKey;
        },
        postLikeHandler(post_id,user_id){
            console.log("Liking the post")
            likePost(user_id,post_id).then((response)=>{
                alert(response.data);
                var index = this.posts.findIndex((obj=>obj.id===post_id))
                this.posts[index].upvotes++;  
            }).catch((error)=>{
                alert(error);
            });
        },
        verifyComment(comment_id){
            console.log(comment_id)
            this.fetchPostList();
            // this.postsKey = !this.postsKey;
        }
    }

});
</script>
