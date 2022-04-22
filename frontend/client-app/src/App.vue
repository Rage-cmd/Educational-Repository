<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />

        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"
          width="100"
        />
      </div>

      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
        text
      >
        <span class="mr-2">Latest Release</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <userData/>
      <postData/>
      <PostTemplate :verifiedPost="true" :postModel="samplePostData"/>
    </v-main>
  </v-app>
</template>

<script>
// import HelloWorld from './components/HelloWorld';
import userData from './components/userData.vue';
import postData from './components/postData.vue';
import PostTemplate from './components/PostTemplate.vue';

export default {
  name: 'App',

  components: {
    userData,
    postData,
    PostTemplate
},

  data: () => ({
    samplePostData:{
      "verifiedPost":true,
      "description":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Quos recusandae nesciunt ad voluptate aperiam exercitationem veritatis laudantium totam a, natus inventore, sunt unde laborum nam obcaecati neque. Velit, obcaecati quas. Lorem ipsum dolor, sit amet consectetur adipisicing elit. Aperiam temporibus optio deserunt, at odit dolorem nostrum magnam dolores sequi delectus, corporis reiciendis. Provident tempora minus maiores iure, cum fugit quasi.",
      "videoURL":"https://www.youtube.com/embed/tgB1wUcmbbw",
      "postType":"video",
    }
  }),
};
</script>
