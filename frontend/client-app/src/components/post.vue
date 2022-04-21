<template>
    <div class="post_container">
        <div class="post_content">
            <h1>Posts</h1>
            <ul>
                <li v-for="post in posts" :key="post.id">
                    <h2>{{ post.caption }}</h2>
                    <p>{{ post.text }}</p>
                    <image src = {{post.image_url}}></image>
                </li>
            </ul>
        </div>
    </div>
</template>