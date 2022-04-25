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

            

             <v-form>
                 <v-row>
                    <v-col :cols=4 >
                        <v-container mt-5>
                        <v-select
                        :items="items"
                        v-model="searchFilter"
                        ></v-select>   
                        </v-container>
                    </v-col>
                 <v-col :cols=8>
                     <v-container mt-6 height="10">
                         
                        <v-autocomplete 
                        chips
                        small-chips
                        dense
                        multiple
                        :items="suggestionOptions"
                        ></v-autocomplete>
                     </v-container>
                 </v-col>
                 </v-row>
             </v-form>
            
            <v-spacer></v-spacer>
            <!-- <v-btn icon>
                <v-icon>mdi-bell-outline</v-icon>
            </v-btn> -->
            <NotificationDialog/>
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

import NotificationDialog from "../../components/NavBar/NotificationDialog.vue"

export default {
    components:{
        NotificationDialog,
    },
    setup() {
        
    },
    data:()=>({
        userDetails:{
            "username":"Siddharth",
        },
        drawer: false,
        group: null,
        navBarOptions:["Home"],
        items:["Child Search","Tag","Post"],
        suggestionOptions:["CN","OS", "Lingo"],
        searchFilter:"",
    }),
    created: function(){
        this.searchFilter=this.items[0];
    }
}
</script>