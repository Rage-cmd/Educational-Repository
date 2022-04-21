
<template>
    <div class="user_container">
        <div v-show="users != ['']" class="user_content">
            <h1>Users</h1>
            <ul>
                <li v-for="user in users" :key="user.user_id">
                    <h2>{{ user.name }}</h2>
                    <p>{{ user.email }}</p>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
// import axios from "axios";

export default {
    name: 'userData',
    data() {
            return {
                users: ['']
            }
    },
    methods: {
        async getData(){
            try{
                const response = await this.$http.get('http://127.0.0.1:8000/api/user');
                this.users = response.data;
            } catch(error){
                console.log(error);
            }

        }
    },
    created() {
        this.getData();
    },
}
</script>
