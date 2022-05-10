<template>
    <UserList :currentuser="user" :users="users"
    @banuser="banuser"/>
</template>

<script>
import UserList from './User/UserList.vue';
import {banuser,getAllUsers} from '../api.js';

export default {
    name:'UserListScreen',
    setup() {
        
    },
    props:{
        user:Object
    },
    components:{
        UserList
    },
    data:()=>({
        users:[],
    }),
    created(){
        getAllUsers().then(response=>{
            this.users = response.data.filter(user=>{
                if(this.user.access_level == 'moderator')
                    return user.access_level=='user';
                else
                    return true;
            });
            console.log(this.users);
        });
    },
    methods:{
        async banuser(user,index){
            await banuser(this.user.id,user.id).then(
                response=>{
                    console.log(response);
                    this.users[index].is_banned = true;
                }
            ).catch(error=>{
                alert("Some error occured during user ban");
                console.log(error);
            });
        },
    }
}
</script>