<template>
    <UserList :currentuser="user" :users="users"
    @banuser="banuser"
    @updateRole="upgradeRole"
    :key="userListKey"/>
</template>

<script>
import UserList from './User/UserList.vue';
import {banuser,getAllUsers,updateRole} from '../api.js';

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
        userListKey:true,
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
        async upgradeRole(user_id,role){
            console.log("upgrading user" + role);
            await updateRole(user_id,role).then(
                ()=>{
                    this.$store.state.snackbarMessage = "Role updated Successfully";
                    this.$store.state.snackbar = true;
                    getAllUsers().then(response=>{
                        this.users = response.data;
                        this.userListKey = !this.userListKey;
                    });
                }
            ).catch(error=>{
                alert("Some error occured during user ban");
                console.log(error);
            });
        }
    }
}
</script>