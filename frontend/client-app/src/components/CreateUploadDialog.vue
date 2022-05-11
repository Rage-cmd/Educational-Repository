<template>
    <v-dialog
        v-model="dialog"
        scrollable
        :overlay="false"
        width="1000"
        transition="dialog-transition"
    >
        <template v-slot:activator="{ on, attrs }">
        <v-btn
                color="pink"
                v-bind="attrs"
                v-on="on"
                dark
                fixed
                bottom
                right
                fab
              >
                <v-icon>mdi-plus</v-icon>
      </v-btn>
      </template>
      <v-tabs
          v-model="value"
          color="primary"
          slider-color="primary"
          fixed-tabs
      >
        <v-tab>
            Video Post 
        </v-tab>
          <v-tab-item>
              <UploadVideoPostScreen/>
          </v-tab-item>
        <v-tab>
            Text Post
        </v-tab>
          <v-tab-item>
              <UploadMCQPostScreen :user="user"/>
          </v-tab-item>
          <v-tab>
            Create Tag 
        </v-tab>
          <v-tab-item>
              <TagCreationScreen/>
          </v-tab-item>
      </v-tabs>
    </v-dialog>
</template>

<script>
import UploadVideoPostScreen from './CreationScreens/UploadVideoPostScreen.vue';
import UploadMCQPostScreen from './CreationScreens/UploadMCQPostScreen.vue';
import TagCreationScreen from './CreationScreens/TagCreationScreen.vue';

export default {
    name : 'CreateUploadDialog',
    setup() {
        
    },
    components:{
        UploadVideoPostScreen,
        UploadMCQPostScreen,
        TagCreationScreen,
    },
    props:{
        user:Object
    },
    data: ()=>({
            dialog:false,
            value:0,
    }),
}
</script>