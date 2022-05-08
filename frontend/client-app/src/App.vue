<template>

  <v-app>

    <v-main>
      <NavBar :sideMenu="sideMenuMap[user.user_level]" @sideMenuSelect="sideMenuSelectHandler"/>
      <v-container >
        
      </v-container>
      <HomeScreen v-if="currentScreen=='Home'" :currentScreen="currentScreen" />
      <!-- <PendingApprovalsScreen v-if="currentScreen == 'Pending Approvals'" :currentScreen="currentScreen"/>
       -->

      <UserListScreen v-else-if="currentScreen=='Users List'"/>

      <MyProfile v-else-if="currentScreen=='My Profile'" />

      <PostsList v-else :currentScreen="currentScreen"/>

      <CreateUploadDialog/>

      <!-- <UploadVideoPostScreen />
      <TagCreationScreen />
       -->

    </v-main>
  </v-app>
</template>

<script>
// import HelloWorld from './components/HelloWorld';
import HomeScreen from './components/HomeScreen.vue';
// import PendingApprovalsScreen from './components/Moderator/PendingApprovalsScreen.vue'
import NavBar from './components/NavBar/NavBar.vue';
import PostsList from './components/PostsList.vue';
import CreateUploadDialog from './components/CreateUploadDialog.vue';
// import UploadVideoPostScreen from './components/CreationScreens/UploadVideoPostScreen.vue';
// import TagCreationScreen from './components/CreationScreens/TagCreationScreen.vue';
import UserListScreen from './components/UserListScreen.vue';
import MyProfile from './components/MyProfile.vue';
import axios from 'axios';

export default {
  name: 'App',

  components: {
    HomeScreen,
    // UploadVideoPostScreen,
    // PendingApprovalsScreen,
    CreateUploadDialog,
    NavBar,
    PostsList,
    // TagCreationScreen,
    UserListScreen,
    MyProfile,
},

  data: () => ({
    user:{
      "username":"sample_user",
      "user_level":"Moderator",
    },
    currentScreen:"Home",
    sideMenuMap:{
      "Moderator":["Your Uploads","My Profile", "Watchlist","Pending Approvals","Users List"],
      "user":["Your Uploads","My Profile", "Watchlist"],
    },
    hideall: true,
  }),
  methods:{
    async sideMenuSelectHandler(opt){
      this.currentScreen = opt;
      const response = await axios.get('http://127.0.0.1:8000/api/post');
      console.log("This response:" + JSON.stringify(response.data));
    }
  }
};
</script>
