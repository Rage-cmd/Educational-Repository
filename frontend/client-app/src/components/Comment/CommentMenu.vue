<template>
    <v-menu
            bottom
            left
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                icon
                v-bind="attrs"
                v-on="on"
              >
                <v-icon>mdi-dots-vertical</v-icon>
              </v-btn>
            </template>

            <v-list>
              <v-list-item
                @click="reportComment"
              >
              <v-list-item-icon>
                <v-icon>mdi-alert-circle-outline</v-icon>
              </v-list-item-icon>
                <v-list-item-title>Report</v-list-item-title>
              </v-list-item>

              <v-list-item v-if=" postModel.author.id === user.id " @click="verifyCommentHandler">
              <v-list-item-icon>
                <v-icon color="green">mdi-check-decagram</v-icon>
              </v-list-item-icon>
                <v-list-item-title>Verify</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
</template>

<script>
import {reportComment, verifyComment} from '../../api.js';

export default {
    name:'CommentMenu',
    setup() {
        
    },
    props:{
        user:Object,
        postModel:Object,
        comment:Object,
    },
    data: ()=>({
        menuopts:["report"],
    }),
    methods:{
      async verifyCommentHandler(){
        await verifyComment(this.comment.id,this.user.id).then(
          ()=>{
            this.$store.state.snackbarMessage = "Comment verified successfully";
            this.$store.state.snackbar = true;
            this.$emit('verifyComment',this.comment.id);
          }
        ).catch(error=>{
          alert("Some error occured during comment verification");
          console.log(error);
        });
      },
      async reportComment(){
        reportComment(this.comment.id,this.user.id).then(
          ()=>{
            this.$store.state.snackbarMessage = "Comment reported successfully";
            this.$store.state.snackbar = true;
          }
        ).catch(error=>{
          alert("Some error occured during comment reporting");
          console.log(error);
        });
      },
    },
    created(){
      console.log("commentMenu" + JSON.stringify(this.postModel));
    }
}
</script>