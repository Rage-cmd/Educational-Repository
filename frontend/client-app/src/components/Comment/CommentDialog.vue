<template>
    <v-dialog
        v-model="dialog"
        scrollable
        :overlay="true"
        width="90%"
        transition="dialog-transition"
    >
        <template v-slot:activator="{ on, attrs }">
            <v-btn icon v-bind="attrs" v-on="on">
                    <v-icon>mdi-comment-outline</v-icon>
            </v-btn>
        </template>
        <v-card height="100%">
            <v-row class="mb-0">
                <v-col cols=6 mr-0>
                    <v-card>
                        
                    <PostView :postModel="postModel" :showActionTray="false"/>
                    </v-card>
                </v-col>
                <v-col cols=6 ml-0 scrollable>
                       <v-card flat>
                           <v-card-text>
                           <v-container >
                               
                           <v-row>
                               <v-col cols=10>
                                <v-textarea rows="1" v-model="commentInput">
                                </v-textarea>

                               </v-col>
                            <v-btn color="primary" @click="postComment">Post</v-btn>  
                           </v-row>
                           </v-container>

                           </v-card-text>
                       </v-card> 
                    <v-card scrollable flat>
                        <v-card-text>
                            
                            <v-list dense height="100%" three-line>
                            <v-list-title class="text-center">Comments</v-list-title>
                            <v-list-item-group
                                color="primary"
                            >
                                <v-list-item
                                v-for="(comment, i) in postModel.comments"
                                :key="i"
                                elevation="1"
                                width="100%"
                                >
                                <v-list-item-avatar>
                                    <v-img :src="comment.author.profile_picture"></v-img>
                                </v-list-item-avatar>
                                <v-list-item-content>
                                    <v-list-item-title v-html="comment.author.name"></v-list-item-title>
                                    <v-list-item-subtitle v-html="comment.text"></v-list-item-subtitle>
                                <!-- <v-spacer></v-spacer> -->
                                <!-- <v-btn icon>
                                    <v-icon>mdi-dots-vertical</v-icon>
                                </v-btn> -->

                                <!-- <v-list-item-content>
                                    <v-list-item-title v-text="item.text"></v-list-item-title>
                                </v-list-item-content> -->
                                </v-list-item-content>
                                <v-icon color="green" v-if="comment.is_verified">mdi-check-bold</v-icon>
                                <CommentMenu :user="user" :postModel="postModel" :comment="comment" @verifyComment="verifyComment"/>
                                </v-list-item>
                            </v-list-item-group>
                            </v-list>

                        </v-card-text>
                    </v-card>
                </v-col>
            </v-row>
      </v-card>
    </v-dialog>
</template>

<script>
import PostView from './PostView.vue';
import CommentMenu from './CommentMenu.vue'
import { uploadComment } from '../../api';
export default {
    name:'CommentDialog',
    components:{
        PostView,
        CommentMenu,
    },
    setup() {
        
    },
    created(){
        console.log(this.postModel);
    },
    props:{
        postModel:Object,
        user:Object,
    },
    data:()=>({
        items : [{"commentedby":"user1",
                    "comment":"a + b = c"},
                {"commentedby":"user2",
                    "comment":"Albert Einstein"}],
        dialog:false,
        commentInput:"",
    }),
    methods:{
        verifyComment(commentId){
            this.$emit('verifyComment',commentId);
        },
        postComment(){
            uploadComment(this.commentInput,this.user.id,this.postModel.id).then(
                (res)=>{
                    
                    var index = this.$store.state.posts.findIndex(post=>post.id==this.postModel.id);
                    this.$store.state.posts[index].comments.push(res.data);
                    console.log("comment: " + JSON.stringify(res.data));
                    this.commentInput="";
                }
            )
        },
    }
}
</script>