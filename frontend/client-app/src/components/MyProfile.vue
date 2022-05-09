 <template>
    <v-app>
      <v-card class="mx-auto mt-15" width="50%" elevation="5">
          <v-row class="pt-8  justify-center" >
            <v-avatar color="primary" size="150">A</v-avatar>
          </v-row>
          <v-list >
               <v-card-title class="pb-0 pt-5 justify-center" >{{user.name}}</v-card-title>
              <v-card-subtitle class="pt-3 text-center">
                  {{user.email}}
              </v-card-subtitle>
              <!-- <v-list-item-subtitle class="text-center">
                    Email
              </v-list-item-subtitle> -->
          </v-list>

            <v-divider></v-divider>
            <v-card-text>
                <v-row width="100%" justify="space-around">
                <v-list class="text-center">
                    <v-list-item-title>
                        Posts
                    </v-list-item-title>
                    <v-list-item-subtitle>
                        {{user.posts.length}}
                    </v-list-item-subtitle>
                </v-list>
                
                <v-list class="text-center">
                    <v-list-item-title>
                        Comments
                    </v-list-item-title>
                    <v-list-item-subtitle>
                        {{user.comments.length}}
                    </v-list-item-subtitle>
                </v-list>

                <v-list class="text-center">
                    <v-list-item-title>
                        Points
                    </v-list-item-title>
                    <v-list-item-subtitle>
                        {{user.points}}
                    </v-list-item-subtitle>
                </v-list>
                </v-row>
            </v-card-text>
         
      </v-card>
    </v-app>
</template>

<script>


export default ({
    components:{

    },
    setup() {
        
    },
    created() {
    },
    props:{
        user:{
            type:Object,
            default:()=>({
                "username":"sample_user",
                "access_level":"Moderator",
            }),
        },
    },
    data:()=>({
    }),
    methods:{
    }
})
</script>
