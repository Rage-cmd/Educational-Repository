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
import {verifyComment} from '../../api.js';

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
          response=>{
            alert(response.data);
            this.$emit('verifyComment',this.comment.id);
          }
        ).catch(error=>{
          alert("Some error occured during comment verification");
          console.log(error);
        });
      }
    },
    created(){
      console.log("commentMenu" + this.postModel);
    }
}
</script>