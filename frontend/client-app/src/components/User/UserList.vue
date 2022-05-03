<template>
<v-container class="d-flex justify-center mt-4">
    
<v-card width="70%">
    <v-card-title class="text-center">
        USERS
    </v-card-title>
    <v-list>
        <v-list-item
        v-for="user in users"
        :key="user.id"
        >
        <v-list-item-avatar>
            <v-img src="https://cdn.vuetifyjs.com/images/lists/1.jpg"></v-img>
        </v-list-item-avatar>

        <v-list-item-content>
            <v-list-item-title v-html="user.username"></v-list-item-title>
        </v-list-item-content>

        <v-spacer></v-spacer>
        <v-tooltip top>
            <template v-slot:activator="{ on, attrs }">
                <v-btn 
                color="error"
                v-bind="attrs"
                v-on="on">
                    <v-icon small>mdi-account-remove</v-icon>
                </v-btn>
            </template>
            <span>Ban User</span>

        </v-tooltip>

        <v-tooltip top>
            <template v-slot:activator="{ on, attrs }">
                
                 <v-btn 
                 color="primary" 
                 class="ma-3"
                 v-bind="attrs"
                 v-on="on">
                    <v-icon small>mdi-account-arrow-up</v-icon>
                </v-btn>
            </template>
            <span>Upgrade User Level</span>

        </v-tooltip>

        </v-list-item>
    </v-list>
</v-card>
    
</v-container>
        
</template>

<script>
export default {
    name:'UserList',
    setup() {
        
    },
    data: ()=>({
        users:[
            {"id":1,
            "username":"user1",
            "user_level":"user",
            },
            {"id":2,
            "username":"user2",
            "user_level":"moderator",
            },
        ]
    }),
}
</script>