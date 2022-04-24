<template>
    
    <v-container >
            <v-app-bar
            color="primary"
            dark
            elevate-on-scroll
            absolute
            >
                <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>


            <!-- <v-row ml-4> -->
                   <v-btn      
                   v-for="opt in navBarOptions" :key="opt"
                   color="primary"
                   elevation="0"
                    >
                        {{opt}}
                    </v-btn>
            <!-- </v-row> -->
                
            <v-spacer></v-spacer>

                <v-btn icon>
                    <v-icon>mdi-magnify</v-icon>
                </v-btn>

                <v-btn icon>
                    <v-icon>mdi-logout</v-icon>
                </v-btn>
            </v-app-bar>

            <v-navigation-drawer
            v-model="drawer"
            absolute
            temporary
            >
                <v-list
                    nav
                >
                    <v-list-item-group
                    v-model="group"
                    active-class="deep-purple--text text--accent-4"
                    >
                    <v-list-item>
                        <v-list-item-icon>
                        <v-icon>mdi-home</v-icon>
                        </v-list-item-icon>
                        <v-list-item-title>Home</v-list-item-title>
                    </v-list-item>

                    <v-list-item>
                        <v-list-item-icon>
                        <v-icon>mdi-account</v-icon>
                        </v-list-item-icon>
                        <v-list-item-title>Account</v-list-item-title>
                    </v-list-item>
                    </v-list-item-group>
                </v-list>
            </v-navigation-drawer>
    </v-container>
</template>

<script>
export default {
    setup() {
        
    },
    data:()=>({
        userDetails:{
            "username":"Siddharth",
        },
        drawer: false,
        group: null,
        navBarOptions:["Home","Notifications","Your Uploads","Watchlist"]
    })
}
</script>