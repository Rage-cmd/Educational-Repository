<template>

    <v-app >
        <NavBar/>        
        <PostTemplate :postModel="sampleVideoPostData"/>
        <PostTemplate :postModel="sampleMCQPostData"/>
    </v-app>
</template>

<script>
import PostTemplate from "../components/PostTemplate.vue";
import NavBar from "../components/NavBar/NavBar.vue";

export default ({
    setup() {
        
    },
    components:{
        PostTemplate,
        NavBar,
    },
    data: ()=>({
        sampleVideoPostData:{
      "title":"Thor Trailer",
      "verifiedPost":true,
      "description":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Quos recusandae nesciunt ad voluptate aperiam exercitationem veritatis laudantium totam a, natus inventore, sunt unde laborum nam obcaecati neque. Velit, obcaecati quas. Lorem ipsum dolor, sit amet consectetur adipisicing elit. Aperiam temporibus optio deserunt, at odit dolorem nostrum magnam dolores sequi delectus, corporis reiciendis. Provident tempora minus maiores iure, cum fugit quasi.",
      "videoURL":"https://www.youtube.com/embed/tgB1wUcmbbw",
      "postType":"video",
    },
    sampleMCQPostData:{
      "verifiedPost":false,
      "title":"Find the value of x",
      "description":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Quos recusandae nesciunt ad voluptate aperiam exercitationem veritatis laudantium totam a, natus inventore, sunt unde laborum nam obcaecati neque. Velit, obcaecati quas. Lorem ipsum dolor, sit amet consectetur adipisicing elit. Aperiam temporibus optio deserunt, at odit dolorem nostrum magnam dolores sequi delectus, corporis reiciendis. Provident tempora minus maiores iure, cum fugit quasi.",
      "imgURL":"https://hi-static.z-dn.net/files/d62/0c3678b43230a26c13d6f16947d28a03.jpg",
      "postType":"MCQ",
      "Options":""
    },
    })
})
</script>
