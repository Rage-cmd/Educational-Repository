<template>
    <v-app>
        <v-app-bar app dense dark color="blue">
            <v-spacer></v-spacer>
            Already regiserted? <v-btn class="pa-2" rounded @click="$emit('changelogin')" text> Login</v-btn>            
        </v-app-bar>
        <v-content class="pt-0">
            <v-container fluid class="pa-0" fill-height>
                <v-row class="fill-height" style="flex-flow: row nowrap;">
                <v-col cols="2" class="pa-0">
                    <v-img height="100%" width="100%" src="https://m.media-amazon.com/images/I/91LUaElO4aL._AC_SS450_.jpg" style="background-size: cover">
                    </v-img>
                </v-col>
                <v-col class="pa-0">
                    <div height="100vh">
                        <v-card class="ml-15 mt-15" width="500">
                        <v-card-title>Sign up</v-card-title>
                        <v-card-text>
                            <v-text-field prepend-icon="mdi-account-circle" v-model="username" label="Username" clearable></v-text-field>
                            <v-text-field prepend-icon="mdi-email" label="Email" v-model="email" clearable></v-text-field>
                            <v-text-field prepend-icon="mdi-lock" label="Password" v-model="password" type="password"></v-text-field>
                            <v-text-field prepend-icon="mdi-lock" label="Confirm Password" type="password"></v-text-field>
                        </v-card-text>
                        <v-divider></v-divider>
                        <v-card-actions>
                            <v-btn color="success" @click="signupuser">Register</v-btn>
                            <v-btn color="info" @click="$emit('changelogin')">Login</v-btn>
                        </v-card-actions>
                    </v-card>
                    </div>
                </v-col>
            </v-row>
            </v-container>
            
            
        </v-content>
    </v-app>
</template>

<script>

import {signup} from '../api.js';

export default ({
    setup() {
        
    },
    data: ()=>({
        email:"",
        username:"",
        password:"",
    }),
    methods: {
      async signupuser(){
          console.log("check");
          await signup(this.username,this.email,this.password).then((response)=>{
              if(response.status == 200){
                  this.$emit('successfullLogin',response.data)
              }else{
                  alert("Some error, please try again!");
              }
          }
          );
      }  
    },

})
</script>

