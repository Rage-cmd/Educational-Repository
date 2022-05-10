<template>

  <v-app>

    <v-main>
      <LoginVue v-if="!loggedin && currentScreen == 'loginScreen'" 
      @successfulLogin="loginuser"
      @signup="changeTosignup"/>
      <SignupVue v-else-if="!loggedin && currentScreen == 'signupScreen'" 
      @successfullLogin="loginuser"
      @changelogin="changelogin"/>
      <div v-else>
      <NavBar :sideMenu="sideMenuMap[user.access_level]" 
      @sideMenuSelect="sideMenuSelectHandler"
      @logout = "logout"
      :user="user"/>
      <v-container >
        
      </v-container>


      <HomeScreen v-if="currentScreen=='Home' " :currentScreen="currentScreen"/>
      <!-- <PendingApprovalsScreen v-if="currentScreen == 'Pending Approvals'" :currentScreen="currentScreen"/>
       -->

      <UserListScreen v-else-if="currentScreen=='Users List'" :user="user"/>

      <MyProfile v-else-if="currentScreen=='My Profile' " :user="user"/>

      <PostsList v-else :currentScreen="currentScreen" :user="user"/>

      <CreateUploadDialog/>

      <!-- <UploadVideoPostScreen />
      <TagCreationScreen />
       -->

      </div>
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
import {yourUploads} from './api.js';
import LoginVue from './components/LoginVue.vue';
import SignupVue from './components/RegisterVue.vue';

export default {
  name: 'App',

  components: {
    HomeScreen,
    CreateUploadDialog,
    NavBar,
    PostsList,
    UserListScreen,
    MyProfile,
    LoginVue,
    SignupVue,
},

  data: () => ({
    loggedin : false,
    user:{
      "username":"sample_user",
      "access_level":"moderator",
    },
    currentScreen:"loginScreen",
    sideMenuMap:{
      "moderator":["Your Uploads","My Profile", "Saved Posts","Pending Approvals","Users List"],
      "user":["Your Uploads","My Profile", "Saved Posts"],
      "admin":["Your Uploads","My Profile", "Saved Posts","Pending Approvals","Users List"],
    },
    hideall: true,
  }),
  methods:{
    async sideMenuSelectHandler(opt){
      this.currentScreen = opt;
      yourUploads().then(function(response){
        console.log(response);
        }
      );
    },
    loginuser(user){
      console.log(user);
      this.user = user;
      this.loggedin=true;
      this.currentScreen="Home";
    },
    logout(){
      this.loggedin=false;
      this.user = null;
      this.currentScreen="loginScreen";
    },
    changeTosignup(){
      this.currentScreen="signupScreen";
    },
    changelogin(){
      this.currentScreen = "loginScreen";
    }
  },
  created(){
    // getUserDetails('u5').then(response => {
    //     this.user = response.data;
    //   });
  }
};
</script>
