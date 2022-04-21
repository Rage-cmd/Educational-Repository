<template>
    <div class="post_container">
        <div class="post_content">
            <h1>Posts</h1>
            <ul>
                <li v-for="post in posts" :key="post.id">
                    <h2>{{ post.caption }}</h2>
                    <p>{{ post.text }}</p>
                    <img v-bind:src="post.image_url"/>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>

import axios from 'axios';

export default ({
    name: 'postData',
    data() {
        return {
            posts: []
        }
    },
    created() {
        this.fetchPosts()
    },
    methods: {
        fetchPosts() {
            axios.get('http://127.0.0.1:8000/api/post')
                .then(response => {
                    this.posts = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
})
</script>
