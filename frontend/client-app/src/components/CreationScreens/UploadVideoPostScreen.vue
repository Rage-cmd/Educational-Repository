<template>
<v-container mt-6 class="d-flex justify-center">
        
    <v-card width="70%" mt-2 elevation="8">
        <v-card-text>
            <v-form width="50%">
                <v-text-field
                    width="20%"
                    label="Title"
                    required
                ></v-text-field>

                <v-file-input
                    accept="video/*"
                    label="Video File"
                    required
                ></v-file-input>

                <v-textarea
                    outlined
                    required
                    name="input-7-4"
                    label="Description"
                ></v-textarea>

                <v-autocomplete 
                        chips
                        small-chips
                        dense
                        multiple
                        :items="suggestionOptions"
                        label="Tags"
                        ></v-autocomplete>
            
            
            <v-card-actions class="d-flex justify-center">
            <v-btn
                color="primary"
                @click="reveal = true"
            >
                Post
            </v-btn>
            </v-card-actions>
            </v-form>
            
        </v-card-text>
    </v-card>
</v-container>
</template>