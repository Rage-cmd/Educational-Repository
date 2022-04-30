<template>

    <v-app >
        <v-container>    
        </v-container>
        <v-container mt-6>
            <PostTemplate :postModel="sampleMCQPostData" :currentScreen="currentScreen"/>
            <PostTemplate :postModel="sampleVideoPostData" :currentScreen="currentScreen"/>
                        
        </v-container>        
        
    </v-app>
</template>

<script>
import PostTemplate from "../components/PostTemplate.vue" ;

export default ({
    setup() {
        
    },
    components:{
        PostTemplate,
    },
    props:{
        currentScreen:String,
    },
    data: ()=>({
        sampleVideoPostData:{
      "title":"Thor Trailer",
      "verifiedPost":true,
      "description":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Quos recusandae nesciunt ad voluptate aperiam exercitationem veritatis laudantium totam a, natus inventore, sunt unde laborum nam obcaecati neque. Velit, obcaecati quas. Lorem ipsum dolor, sit amet consectetur adipisicing elit. Aperiam temporibus optio deserunt, at odit dolorem nostrum magnam dolores sequi delectus, corporis reiciendis. Provident tempora minus maiores iure, cum fugit quasi.",
      "videoURL":"https://www.youtube.com/embed/tgB1wUcmbbw",
      "postType":"video",
      "username":"user1",
    },
    sampleMCQPostData:{
      "verifiedPost":false,
      "title":"Find the value of x",
      "description":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Quos recusandae nesciunt ad voluptate aperiam exercitationem veritatis laudantium totam a, natus inventore, sunt unde laborum nam obcaecati neque. Velit, obcaecati quas. Lorem ipsum dolor, sit amet consectetur adipisicing elit. Aperiam temporibus optio deserunt, at odit dolorem nostrum magnam dolores sequi delectus, corporis reiciendis. Provident tempora minus maiores iure, cum fugit quasi.",
      "imgURL":"https://hi-static.z-dn.net/files/d62/0c3678b43230a26c13d6f16947d28a03.jpg",
      "postType":"MCQ",
      "options":["option1", "option2", "option3"],
      "username":"user2",
    },
    selectedTab:null,
    })
})
</script>
