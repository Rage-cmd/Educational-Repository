<template>
    <UserList :currentuser="user"/>
</template>

<script>
import UserList from './User/UserList.vue';

export default {
    name:'UserListScreen',
    setup() {
        
    },
    props:{
        user:Object
    },
    components:{
        UserList
    }
}
</script>