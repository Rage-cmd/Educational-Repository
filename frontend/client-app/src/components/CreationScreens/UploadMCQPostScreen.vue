<template>
<v-container mt-6 class="d-flex justify-center">
        
    <v-card width="75%" mt-2 elevation="8">
        <v-card-text>
            <v-form width="50%">
                <v-text-field
                    width="20%"
                    label="Title"
                    required
                ></v-text-field>

                <v-file-input
                    accept="image/*"
                    label="Image File"
                    required
                ></v-file-input>

                <v-textarea
                    outlined
                    name="input-7-4"
                    label="Description"
                    required
                ></v-textarea>

                <v-autocomplete 
                        chips
                        small-chips
                        dense
                        multiple
                        :items="suggestionOptions"
                        label="Tags"
                        ></v-autocomplete>
            
            </v-form>
            <v-card-actions class="d-flex justify-center">
            <v-btn
                color="primary"
                @click="reveal = true"
            >
                Post
            </v-btn>
            </v-card-actions>
            
        </v-card-text>
    </v-card>
</v-container>
</template>