<template>
<v-container mt-6 class="d-flex justify-center">
        
    <v-card width="70%" mt-2 elevation="8">
        <v-card-text>
            <v-form width="50%">
                <v-text-field
                    width="20%"
                    label="Tag Name"
                ></v-text-field>

                <v-autocomplete 
                        chips
                        small-chips
                        dense
                        multiple
                        :items="suggestionOptions"
                        label="Tag Heirarchy"
                ></v-autocomplete>
            
            </v-form>
            <v-card-actions class="d-flex justify-center">
            <v-btn
                color="primary"
                @click="reveal = true"
            >
                Create
            </v-btn>
            </v-card-actions>
            
        </v-card-text>
    </v-card>
</v-container>
</template>