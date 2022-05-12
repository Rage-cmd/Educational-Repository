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
                   @click="$emit('navBarOption',opt)"
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
                        @input="refreshSuggestions"
                        ></v-select>   
                        </v-container>
                    </v-col>
                 <v-col :cols=8>
                     <v-container mt-6 height="10">
                         
                        <v-autocomplete 
                        chips
                        small-chips
                        dense
                        :items="getSuggestions"
                        @update:search-input="debounceInput($event)"
                        @input="searchHandler"
                        no-filter 
                        >
                        
                         <template v-slot:selection="data">
                            <v-chip v-bind="data.attrs" small>{{getOption(data.item)}}</v-chip>
                        </template>

                        <template v-slot:item="data" >
                            <v-list-item-content @click="optionSelected(data.item)">
                                <v-list-item-title v-html="getOption(data.item)"></v-list-item-title>
                            </v-list-item-content>
                        </template>

                        </v-autocomplete>
                     </v-container>
                 </v-col>
                 </v-row>
             </v-form>
            
            <v-spacer></v-spacer>
            <!-- <v-btn icon>
                <v-icon>mdi-bell-outline</v-icon>
            </v-btn> -->
            <NotificationDialog :user="user"/>
            <v-tooltip bottom>
                 <template v-slot:activator="{ on, attrs }">
                    <v-btn 
                    v-bind="attrs"
                    v-on="on" 
                    icon 
                    @click="$emit('logout')">
                        <v-icon>mdi-logout</v-icon>
                    </v-btn>
                </template>
                <span>logout</span>
                
            </v-tooltip>
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
                    v-model="sideMenuSelection"
                    active-class="deep-purple--text text--accent-4"
                    >
                    <v-list-item v-for="opt in sideMenu" :key="opt" @click="$emit('sideMenuSelect',opt)">
                        <v-list-item-title>{{opt}}</v-list-item-title>
                    </v-list-item>
                    </v-list-item-group>
                </v-list>
            </v-navigation-drawer>
    </v-container>
</template>

<script>

import NotificationDialog from "../../components/NavBar/NotificationDialog.vue"
import {getPostSuggestions} from "../../api.js";
import _ from 'lodash';

export default {
    components:{
        NotificationDialog,
    },
    setup() {
        
    },
    props:{
        sideMenu:Array,
        user:Object,
        currentScreen:String,
    },
    data:()=>({
        userDetails:{
            "username":"Siddharth",
        },
        drawer: false,
        sideMenuSelection: null,
        navBarOptions:["Home"],
        items:["Post","Tag","Child Search"],
        suggestionOptions:[],
        // suggestionOptions:["CN","OS", "Lingo"],
        searchFilter:"",
        search:null,
        selectedOption:null,
    }),
    created: function(){
        this.searchFilter=this.items[0];
    },
    computed:{
        getSuggestions(){
            return this.$store.state.suggestions;
        },
    },
    watch:{
        user(){
            console.log(this.user);
        },
        currentScreen(val){
            if(val!=="Search Result"){
                this.searchFilter=this.items[0];
            }
        }
    },
    methods:{
        refreshSuggestions(){
            if(this.searchFilter === this.items[2]){
                getPostSuggestions("",'child_search').then(
                    (response)=>{
                        console.log("suggestions: " + JSON.stringify(response.data));
                        this.$store.commit('setSuggestions',response.data.tags);
                    }
                )
            }else{
                console.log("check");
                this.$store.commit('setSuggestions',[]);
            }
        },
        debounceInput: _.debounce(function (search) {
            getPostSuggestions(search,this.searchFilter.toLowerCase()).then(res=>{
                this.$store.commit('setSuggestions',res.data);
            })
        }, 1000),
        loginput(val){
            console.log(val);
        },
        getOption(item){
            
            if(item.caption){
                return item.caption;
            }else{
                return item.name;
            }
        },
        getItem(text){
            return this.$store.state.suggestions.find(item=>item.name===text[0]);
        },
        optionSelected(item){
            this.selectedOption=item;
        },
        searchHandler(){
            this.$emit('searchInput',this.selectedOption,this.searchFilter);
        }
    }
}
</script>