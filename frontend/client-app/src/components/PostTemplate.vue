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


    <v-card-title>{{postModel.title}}</v-card-title>
    
    
    <v-card-text secondary-title>
        <v-icon small>mdi-account</v-icon>
        {{postModel.username}}
    </v-card-text>


    <iframe v-if="postModel.postType === 'video'" width="100%" height="400" :src="postModel.videoURL" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
    </iframe>

    <v-img v-if="postModel.postType === 'MCQ'" :src="postModel.imgURL" width="100%"></v-img>


    <v-card-text>
      <v-row
        align="center"
        class="mx-0"
      >
        <v-btn
        class="ma-2"
        text
        icon
        color="blue lighten-2"
      >
        <v-icon>mdi-thumb-up-outline</v-icon>
      </v-btn>

      <v-btn
      class="ma-2"
      icon>
          <v-icon>mdi-comment-outline</v-icon>
      </v-btn>    

      <v-icon color="green" v-if="postModel.verifiedPost">mdi-check-bold</v-icon>   

      <v-btn
      class="ma-2"
      icon>
          <v-icon>mdi-bookmark-outline</v-icon>
      </v-btn>     
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
        <v-chip>tag1</v-chip>

        <v-chip>tag2</v-chip>

        <v-chip>tag3</v-chip>

        <v-chip>tag4</v-chip>
      </v-chip-group>
    </v-card-text>

    <v-card-actions v-if="currentScreen=='Pending Approvals'">
      <v-btn rounded color="success" width="48%">
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
export default {
  name: 'PostTemplate',
  data(){
      return{
        fullDescription:false,
        description:"",
        loading:false,
      }
  },
  props:{
      postModel:Object,
      currentScreen:String,
  },

  methods:{
      getDescription(postModel){
          if(this.fullDescription == true){
              return postModel.description;
          }
          else{
              return postModel.description.substring(0,250)
          }
      },

      toggleDescription(postModel){
            this.fullDescription = !this.fullDescription;
            this.description = this.getDescription(postModel);
      }
  },
  created: function(){
      this.description = this.getDescription(this.postModel);
      console.log(this.currentScreen);
  },

}
</script>
