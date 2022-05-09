<template>
<v-container class="d-flex justify-center mt-4">
    
<v-card width="70%">
    <v-card-title class="text-center">
        USERS
    </v-card-title>
    <v-list>
        <v-list-item
        v-for="user in users.filter(user=>{
                return user.access_level=='user';
            })"
        :key="user.id"
        >
        <v-list-item-avatar>
            <v-img :src="user.profile_picture"></v-img>
        </v-list-item-avatar>

        <v-list-item-content>
            <v-list-item-title v-html="user.name"></v-list-item-title>
        </v-list-item-content>

        <v-spacer></v-spacer>
        <v-tooltip top>
            <template v-if="!user.is_banned" v-slot:activator="{ on, attrs }">
                <v-btn 
                color="error"
                 class="ma-3"
                v-bind="attrs"
                v-on="on"
                @click="banuser(user)">
                    <v-icon small>mdi-account-remove</v-icon>
                </v-btn>
            </template>
            <span>Ban User</span>

        </v-tooltip>

        <v-tooltip top>
            <template v-if="currentuser.access_level=='admin'" v-slot:activator="{ on, attrs }">
                
                 <v-btn 
                 color="primary" 
                 class="ma-3"
                 v-bind="attrs"
                 v-on="on">
                    <v-icon small>mdi-account-arrow-up</v-icon>
                </v-btn>
            </template>
            <span>Upgrade User Level</span>

        </v-tooltip>

        <v-tooltip top>
            <template v-if="user.is_banned===true" v-slot:activator="{ on, attrs }">
                
                 <v-btn 
                 color="success" 
                 class="ma-3"
                 v-bind="attrs"
                 v-on="on"
                 @click="unbanuser(user)">
                    <v-icon small>mdi-account-lock-open</v-icon>
                </v-btn>
            </template>
            <span>Remove Ban</span>

        </v-tooltip>

        </v-list-item>
    </v-list>
</v-card>
    
</v-container>
        
</template>

<script>
import {getAllUsers,banuser,unbanuser} from '../../api.js';

export default {
    name:'UserList',
    setup() {
        
    },
    computed:{
        filterUsers(users){
            console.log(users);
            return users.filter(user=>{
                return user.access_level=='user';
            })
        }
    },
    props:{
        currentuser:{
            type:Object,
            default:()=>({"id":2,
            "username":"user2",
            "user_level":"moderator",
            })
        },
    },
    data: ()=>({
        users:[
            {"id":1,
            "username":"user1",
            "user_level":"user",
            },
            {"id":2,
            "username":"user2",
            "user_level":"moderator",
            },
        ]
    }),
    created(){
        getAllUsers().then(response=>{
            this.users = response.data;
            console.log(this.users);
        });
    },
    methods:{
        async banuser(user){
            await banuser(this.currentuser.id,user.id).then(
                response=>{
                    console.log(response);
                    user.is_banned = true;
                }
            ).catch(error=>{
                alert("Some error occured during user ban");
                console.log(error);
            });
        },
        async unbanuser(user){
            await unbanuser(this.currentuser.id,user.id).then(
                response=>{
                    console.log(response);
                    user.is_banned = false;
                }
            ).catch(error=>{
                alert("Some error occured during user ban");
                console.log(error);
            });
        }
  }
}
</script>