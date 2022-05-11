<template>
<v-container mt-6 class="d-flex justify-center">
        
    <v-card width="70%" mt-2 elevation="8">
        <v-card-text>
            <v-form width="50%">
                <v-text-field
                    width="20%"
                    label="Tag Name"
                    v-model="tagModel.name"
                ></v-text-field>

                <v-autocomplete 
                        chips
                        small-chips
                        dense
                        v-model="tagModel.parentTag"
                        :items.sync="suggestions"
                        @update:search-input="debounceInput($event)"
                        label="Tag Heirarchy"
                        no-filter
                >
                <template v-slot:selection="data">
                    <v-chip v-bind="data.attrs" small>{{data.item.name}}</v-chip>
                </template>
                <template v-slot:item="data" >
                            <v-list-item-content>
                                <v-list-item-title v-html="data.item.name"></v-list-item-title>
                                <v-list-item-subtitle v-html="listToStr(data.item.path_to_tag)"></v-list-item-subtitle>
                            </v-list-item-content>
                </template>
                
                </v-autocomplete>
            
            </v-form>
            <v-card-actions class="d-flex justify-center">
            <v-btn
                color="primary"
                @click="createTag"
            >
                Create
            </v-btn>
            </v-card-actions>
            
        </v-card-text>
    </v-card>
</v-container>
</template>

<script>
import _ from 'lodash';
import { createTag, getPostSuggestions } from '../../api';
export default {
    name: 'TagCreationScreen',
    setup() {
        
    },
    data:() => ({
        suggestions:[],
        tagModel:{},
    }),
    methods:{
        listToStr(list){

            return (list.map(tag=>tag.name)).join(' -> ');
        },
        createTag(){
            createTag(this.tagModel.name,this.tagModel.parentTag.id).then(() => {
                alert('Tag created successfully');
                this.$emit('close');
            }).catch(err => {
                alert('Tag creation failed');
                console.log(err);
            }
            );
            console.log(this.tagModel);

        },
        debounceInput: _.debounce(function (search) {
            getPostSuggestions(search,'tag').then(res=>{
                this.suggestions = res.data;
            })
        }, 1000),
    }
}
</script>