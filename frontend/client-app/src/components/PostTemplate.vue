<template>
  <v-card
    :loading="loading"
    class="mx-auto my-12"
    max-width="700"
  >
    <template slot="progress">
      <v-progress-linear
        color="deep-purple"
        height="10"
        indeterminate
      ></v-progress-linear>
    </template>


    <v-card-title>{{postModel.caption}}</v-card-title>
    
    
    <v-card-text secondary-title>
       <v-row>
        <!-- <v-col cols="10"> -->
         <v-list width="100%">
            <v-list-item height="80%" width="100%">
                <v-list-item-avatar size="25">
                    <v-img src="https://cdn.vuetifyjs.com/images/lists/1.jpg"></v-img>
                </v-list-item-avatar>
                <v-list-item-content>
                    <v-list-item-title>{{postModel.author.name}}</v-list-item-title>
                    
                </v-list-item-content>
                <v-spacer></v-spacer>
              {{getDate(postModel)}}
            </v-list-item>
         </v-list>
       </v-row>
    </v-card-text>


    <!-- <iframe v-if="postModel.postType === 'video'" width="100%" height="400" :src="postModel.videoURL" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
    </iframe> -->

    <iframe v-if="postModel.type === 'video'" width="100%" height="400" :src="postModel.video_url" allow="autoplay"
    allowfullscreen>
    </iframe>

    <v-img v-if="postModel.image_url != null && postModel.image_url!=''" :src="postModel.image_url" width="100%"></v-img>


    <v-card-text>
      <v-row
        align="center"
        class="mx-0"
      >
        <v-btn
        class="ma-2"
        icon
        color="blue lighten-2"
        @click="thumbsupBtnHandler()"
      >
        <v-icon v-if="!thumbsupFilled">mdi-thumb-up-outline</v-icon>
        <v-icon v-else>mdi-thumb-up</v-icon>
      </v-btn>

      <!-- <v-btn
      class="ma-2"
      icon>
          <v-icon>mdi-comment-outline</v-icon>
      </v-btn>     -->
      <CommentDialog :postModel="postModel" :user="user" @verifyComment="verifyComment"
      />
   
      <v-btn
      class="ma-2"
      icon
      @click="bookmarkHandler()"
      :loading="bookmarkLoading"
      >
          <v-icon v-if="currentScreen!=='Saved Posts' && !bookmarkFilled">mdi-bookmark-outline</v-icon>
          <v-icon v-else>mdi-bookmark</v-icon>
      </v-btn>     

      <v-btn
      class="ma-2"
      icon
      @click="reportPostHandler"
      >
          <v-icon>mdi-alert-circle-outline</v-icon>
      </v-btn>
   
    <v-spacer></v-spacer>
    <span v-if="this.currentScreen === 'Reported Posts'">Reports: {{postModel.reports}}</span>
    <v-icon color="green" v-if="postModel.is_answered">mdi-check-bold</v-icon>
      </v-row>

      <div class="my-4 text-subtitle-1 font-weight-bold">
        Description
      </div>

      <div>
          {{description}}
          <!-- <v-btn text @click="fullDescription=true">read more..</v-btn> -->
          <a href="javascript:void(0)" @click="toggleDescription(postModel)" v-if="!fullDescription"> read more...</a>
          <!-- <a href="javascript:void(0)" @click="toggleDescription(postModel)"> </a> -->
      </div>
    </v-card-text>

    <v-divider class="mx-4"></v-divider>

    <v-card-text>
      <v-chip-group
        active-class="deep-purple accent-4 white--text"
        column
      >
        <v-chip v-for="tag in postModel.tags" :key="tag">{{tag}}</v-chip>
      </v-chip-group>
    </v-card-text>

    <v-card-actions v-if="currentScreen=='Pending Approvals'">
      <v-btn rounded color="success" width="48%" @click="$emit('approvepost',postModel.id)">
        <v-icon>mdi-check-bold</v-icon>
        Accept
      </v-btn>
      
      <v-btn rounded color="error" width="48%">
        <v-icon>mdi-alpha-x</v-icon>
        Reject
      </v-btn>
    </v-card-actions>

  </v-card>
</template>




<script>

import CommentDialog from './Comment/CommentDialog.vue';
import { savePost,likePost, reportPost} from '../api.js'

export default {
  name: 'PostTemplate',
  components:{
    CommentDialog
  },
  data(){
      return{
        fullDescription:false,
        description:"",
        loading:false,
        thumbsupFilled:false,
        bookmarkFilled:false,
        bookmarkLoading:false,
      }
  },
  props:{
      postModel:Object,
      currentScreen:String,
      user:Object,
  },

  methods:{
      getDescription(postModel){
        // console.log(postModel.video_url)
        if(postModel.text.length <= 250){
          this.fullDescription = true;
        }
          if(this.fullDescription == true){
              return postModel.text;
          }
          else{
              return postModel.text.substring(0,250)
          }
      },

      toggleDescription(postModel){
            this.fullDescription = !this.fullDescription;
            this.description = this.getDescription(postModel);
      },
      thumbsupBtnHandler(){
        // this.$emit('postLike',this.postModel.id,this.user.id);
        console.log("Liking the post")
            likePost(this.user.id,this.postModel.id).then(()=>{
                var index = this.$store.state.posts.findIndex((obj=>obj.id===this.postModel.id))
                this.$state.state.posts[index].upvotes++;  
            }).catch((error)=>{
                alert(error);
            });
        this.thumbsupFilled = !this.thumbsupFilled;
      },
      async bookmarkHandler(){
        this.bookmarkLoading=true;
        await savePost(this.user.id,this.postModel.id).then(()=>{
          this.bookmarkFilled = !this.bookmarkFilled;
          if(this.currentScreen === "Saved Posts"){
            this.$store.commit('setPosts',this.$store.state.posts.filter(post=>post.id!==this.postModel.id));
          }
          this.bookmarkLoading = false;
        });
      },
      getDate(postModel){
       return postModel.time.split('T')[0].split("-").reverse().join("-"); 
      },
      verifyComment(commentid){
        this.$emit('verifyComment',commentid);
      },
      reportPostHandler(){
        reportPost(this.user.id,this.postModel.id).then(()=>{
          this.$store.state.snackbarMessage = "Post Reported Successfully";
          this.$store.state.snackbar = true;
        }).catch((error)=>{
          alert(error);
        });
      },
  },
  created: function(){
      this.description = this.getDescription(this.postModel);
      // console.log(this.currentScreen);
  },
  computed:{
    
  }

}
</script>
