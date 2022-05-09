<template>
  <v-card
    :loading="loading"
    elevation = "1"
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
        <v-icon small>mdi-account</v-icon>
        {{postModel.author.name}}
    </v-card-text>


    <iframe v-if="postModel.type === 'video'" width="100%" height="400" :src="postModel.video_url" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
    </iframe>

    <v-img v-if="postModel.image_url != null && postModel.image_url!=''" :src="postModel.image_url" width="100%"></v-img>


    <v-card-text>

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
  },

  methods:{
      getDescription(postModel){
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
  },
  created: function(){
      this.description = this.getDescription(this.postModel);
  },

}
</script>
