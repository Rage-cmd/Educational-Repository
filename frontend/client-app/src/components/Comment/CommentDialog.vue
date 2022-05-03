<template>
    <v-dialog
        v-model="dialog"
        scrollable
        :overlay="true"
        width="90%"
        transition="dialog-transition"
    >
        <template v-slot:activator="{ on, attrs }">
            <v-btn icon v-bind="attrs" v-on="on">
                    <v-icon>mdi-comment-outline</v-icon>
            </v-btn>
        </template>
        <v-card height="100%">
            <v-row class="mb-0">
                <v-col cols=6 mr-0>
                    <PostView :postModel="postModel" :showActionTray="false"/>
                </v-col>
                <v-col cols=6 ml-0>
                
                    <v-list dense disabled height="100%">
                    <v-subheader>Comments</v-subheader>
                    <v-list-item-group
                        color="primary"
                    >
                        <v-list-item
                        v-for="(item, i) in items"
                        :key="i"
                        elevation="1"
                        >
                        <v-list-item-avatar>
                            <v-img src="https://cdn.vuetifyjs.com/images/lists/1.jpg"></v-img>
                        </v-list-item-avatar>
                        <v-list-item-content>
                            <v-list-item-title v-html="item.commentedby"></v-list-item-title>
                            <v-list-item-subtitle v-html="item.comment"></v-list-item-subtitle>
                        </v-list-item-content>
                        <!-- <v-list-item-content>
                            <v-list-item-title v-text="item.text"></v-list-item-title>
                        </v-list-item-content> -->
                        </v-list-item>
                    </v-list-item-group>
                    </v-list>

                </v-col>
            </v-row>
      </v-card>
    </v-dialog>
</template>

<script>
import PostView from './PostView.vue';
export default {
    name:'CommentDialog',
    components:{
        PostView,
    },
    setup() {
        
    },
    props:{
        postModel:Object,
    },
    data:()=>({
        items : [{"commentedby":"user1",
                    "comment":"a + b = c"},
                {"commentedby":"user2",
                    "comment":"Albert Einstein"}]
    }),
}
</script>