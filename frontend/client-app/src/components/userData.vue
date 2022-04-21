
<template>
    <div class="user_container">
        <div class="user_content">
            <h1>Users</h1>
            <ul>
                <li v-for="user in users" :key="user.user_id">
                    <h2>{{ user.user_name }}</h2>
                    <p>{{ user.user_email }}</p>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: 'UserData',
    data() {
            return {
                users: ['']
            }
    },
    methods: {
        async getData(){
            try{
                const response = await axios.get('http://127.0.0.1:8000/api/user');
                // log response data
                console.log('get data method was called \n\n');
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
