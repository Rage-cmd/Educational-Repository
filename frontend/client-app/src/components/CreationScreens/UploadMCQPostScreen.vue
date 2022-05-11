<template>
<v-container mt-6 class="d-flex justify-center">
        
    <v-card width="75%" mt-2 elevation="8">
        <v-card-text>
            <!-- <v-form width="50%"> -->
                <v-text-field
                    width="20%"
                    label="Caption"
                    name="caption"
                    v-model="postModel.caption"
                    required
                ></v-text-field>

                <!-- <v-file-input
                    accept="image/*"
                    label="Image File"
                    ref="fileInput"
                    @change="onFileChange"
                    required
                ></v-file-input> -->

                <div class="container mb-2">
                    <label>Image File
                        <input type="file" @change="handleFileUpload( $event )"/>
                    </label>
                    <br>
                </div>

                <v-textarea
                    outlined
                    name="input-7-4"
                    label="Description"
                    required
                    v-model="postModel.description"
                ></v-textarea>

                <v-autocomplete 
                        label="Tags"
                        chips
                        small-chips
                        dense
                        :items="suggestions"
                        v-model="postModel.tags"
                        @update:search-input="debounceInput($event)"
                        no-filter 
                        >
                        
                         <template v-slot:selection="data">
                            <v-chip v-bind="data.attrs" small>{{data.item.name}}</v-chip>
                        </template>

                        <template v-slot:item="data" >
                            <v-list-item-content @click="optionSelected(data.item)">
                                <v-list-item-title v-html="data.item.name"></v-list-item-title>
                            </v-list-item-content>
                        </template>

                </v-autocomplete>
            <v-container class="d-flex justify-center">
                <v-btn
                    color="primary"
                    @click="postUpload"
                >
                    Post
                </v-btn>
            </v-container> 
            <!-- </v-form> -->
            
        </v-card-text>
    </v-card>
</v-container>
</template>

<script>

import _ from 'lodash';
import { getPostSuggestions, uploadPost } from '../../api';

export default {
    name:'UploadMCQPostScreen',
    setup() {
    },
    props:{
        user:Object,
    },
    data: ()=>({
        postModel:{
            caption:'',
            image:'',
            description:'',
            tags:[]
        },
        suggestions:[],
        file:''
    }),
    methods:{
        postUpload(){
            let formdata  = new FormData();
            formdata.append('caption',this.postModel.caption);
            formdata.append('description',this.postModel.description);
            formdata.append('tags',JSON.stringify(this.postModel.tags));
            formdata.append('image',this.file);
            formdata.append('user_id',this.user.id);
                
                uploadPost(formdata).then(res=>{
                    console.log(res);
                }).catch(err=>{
                    console.log(err);
                });
        },
        debounceInput: _.debounce(function (search) {
            getPostSuggestions(search,'tag').then(res=>{
                this.suggestions = res.data;
            })
        }, 1000),
        handleFileUpload( event ){
            this.file = event.target.files[0];
            if(this.file)
                console.log("File taken");
        },
    }
}
</script>