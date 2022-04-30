<template>

  <v-app>
    <!-- <v-app-bar
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
    </v-app-bar> -->

    <v-main>
      <NavBar :sideMenu="sideMenuMap[user.user_level]" @sideMenuSelect="sideMenuSelectHandler"/>

      <HomeScreen v-if="currentScreen=='Home'" :currentScreen="currentScreen" />
      <PendingApprovalsScreen v-if="currentScreen == 'Pending Approvals'" :currentScreen="currentScreen"/>
      

    </v-main>
  </v-app>
</template>

<script>
// import HelloWorld from './components/HelloWorld';
import HomeScreen from './components/HomeScreen.vue';
import PendingApprovalsScreen from './components/Moderator/PendingApprovalsScreen.vue'
import NavBar from './components/NavBar/NavBar.vue'


export default {
  name: 'App',

  components: {
    HomeScreen,
    PendingApprovalsScreen,
    NavBar,
},

  data: () => ({
    user:{
      "username":"sample_user",
      "user_level":"user",
    },
    currentScreen:"Home",
    sideMenuMap:{
      "Moderator":["Your Uploads","My Profile", "Watchlist","Pending Approvals","Reported Users","Banned Users"],
      "user":["Your Uploads","My Profile", "Watchlist"],
    }
  }),
  methods:{
    sideMenuSelectHandler(opt){
      // console.log("selected opt:" + opt);
      this.currentScreen = opt;

    }
  }
};
</script>
