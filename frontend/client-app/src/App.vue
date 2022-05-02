<template>

  <v-app>

    <v-main>
      <NavBar :sideMenu="sideMenuMap[user.user_level]" @sideMenuSelect="sideMenuSelectHandler"/>
      <v-container >
        
      </v-container>
      <HomeScreen v-if="currentScreen=='Home' && !hideall" :currentScreen="currentScreen" />
      <!-- <PendingApprovalsScreen v-if="currentScreen == 'Pending Approvals'" :currentScreen="currentScreen"/>
       -->

      <PostsList v-if="currentScreen=='Watchlist' && !hideall" :currentScreen="currentScreen"/>

      <v-btn
                v-show="!hidden && !hideall"
                color="pink"
                dark
                fixed
                bottom
                right
                fab
              >
                <v-icon>mdi-plus</v-icon>
      </v-btn>

      <UploadScreen />
      

    </v-main>
  </v-app>
</template>

<script>
// import HelloWorld from './components/HelloWorld';
import HomeScreen from './components/HomeScreen.vue';
// import PendingApprovalsScreen from './components/Moderator/PendingApprovalsScreen.vue'
import NavBar from './components/NavBar/NavBar.vue';
import PostsList from './components/PostsList.vue';
import UploadScreen from './components/CreationScreens/UploadScreen.vue';

export default {
  name: 'App',

  components: {
    HomeScreen,
    UploadScreen,
    // PendingApprovalsScreen,
    NavBar,
    PostsList,
},

  data: () => ({
    user:{
      "username":"sample_user",
      "user_level":"Moderator",
    },
    currentScreen:"Home",
    sideMenuMap:{
      "Moderator":["Your Uploads","My Profile", "Watchlist","Pending Approvals","Reported Users","Banned Users"],
      "user":["Your Uploads","My Profile", "Watchlist"],
    },
    hideall: true,
  }),
  methods:{
    sideMenuSelectHandler(opt){
      // console.log("selected opt:" + opt);
      this.currentScreen = opt;

    }
  }
};
</script>
