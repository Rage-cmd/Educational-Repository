<template>
    <v-app>
        <v-app-bar app dense dark color="blue">
            <v-spacer></v-spacer>
            New here? <v-btn class="pa-2" rounded href="/login" text> Sign Up</v-btn>            
        </v-app-bar>
        <v-content class="pt-0">
            <v-container fluid class="pa-0" fill-height>
                <v-row class="fill-height" style="flex-flow: row nowrap;">
                <v-col cols="2" class="pa-0">
                    <v-img height="100%" width="100%" src="../assets/login_wallpaper.jpg" style="background-size: cover">
                    </v-img>
                </v-col>
                <v-col class="pa-0">
                    <div height="100vh">
                        <v-card class="ml-15 mt-15" width="500">
                        <v-card-title>Login</v-card-title>
                        <v-card-text>
                            <v-text-field v-model="username" prepend-icon="mdi-account-circle" label="Username" clearable></v-text-field>
                            <v-text-field v-model="password" prepend-icon="mdi-lock" label="Password" type="password"></v-text-field>
                        </v-card-text>
                        <v-divider></v-divider>
                        <v-card-actions>
                            <v-btn @click="submitForm" color="success">Login</v-btn>
                            <v-btn color="info">Sign Up</v-btn>
                        </v-card-actions>
                    </v-card>
                    </div>
                </v-col>
            </v-row>
            </v-container>
            
            
        </v-content>
    </v-app>
</template>

<script>

export default ({
    setup() {
        
    },
    data: ()=>({
        username: "",
        password: "",
    }),
    methods: {
        async submitForm(){
            const response = await this.$http.post('http://127.0.0.1:8000/api/login', {
                username: this.username,
                password: this.password,
            });

            console.log(response.body);

            this.username= "";
            this.password= "";
            
            if(response.status == 200){
                this.$store.commit('setUser', response.body);
                this.$store.commit('setCurrentScreen', 'Home');
            }

        
        }
    }

})
</script>

