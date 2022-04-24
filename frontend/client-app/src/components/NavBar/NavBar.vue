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

             <v-form pt-1>
                 <v-row mt-3>
                    <v-col :cols=3 >
                        <v-container mt-5>
                            
                        <v-select
                        :items="items"
                        ></v-select>   
                        </v-container>
                    </v-col>
                 <v-col :cols=9>
                     <v-container mt-6>
                         
                        <v-autocomplete 
                        mr-2
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
        navBarOptions:["Home","Notifications"],
        items:["Child Search","Tag","Post"],
        suggestionOptions:["CN","OS", "Lingo"],
    })
}
</script>