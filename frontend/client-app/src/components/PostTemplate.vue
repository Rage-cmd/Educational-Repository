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


    <v-card-title>Sample Post</v-card-title>
    
    
    <v-card-text secondary-title>
        <v-icon small>mdi-account</v-icon>
        sample_user
    </v-card-text>


    <iframe width="100%" height="400" src="https://www.youtube.com/embed/tgB1wUcmbbw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
    </iframe>


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
        <v-icon>mdi-thumb-up</v-icon>
      </v-btn>

      <v-btn
      class="ma-2"
      icon>
          <v-icon>mdi-comment-outline</v-icon>
      </v-btn>    

      <v-btn
      v-if="postModel.verifiedPost"
      class="ma-2"
      icon>
      <v-icon color="green">mdi-check-bold</v-icon>
      </v-btn>   

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
        v-model="selection"
        active-class="deep-purple accent-4 white--text"
        column
      >
        <v-chip>tag1</v-chip>

        <v-chip>tag2</v-chip>

        <v-chip>tag3</v-chip>

        <v-chip>tag4</v-chip>
      </v-chip-group>
    </v-card-text>

  </v-card>
</template>




<script>
export default {
  name: 'PostTemplate',
  data(){
      return{
        fullDescription:false,
        description:"",
      }
  },
  props:{
      postModel:Object,
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
  },

}
</script>
