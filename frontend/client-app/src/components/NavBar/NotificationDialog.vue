<template>
    <v-dialog
      max-width="800"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn icon v-bind="attrs" v-on="on" @click="getNotifications">
                <v-icon>mdi-bell-outline</v-icon>
        </v-btn>
      </template>
      <v-card>
        <v-list dense disabled>
        <v-subheader>Notfications</v-subheader>
        <v-list-item-group
            color="primary"
            v-model="items"
        >
            <v-list-item
            v-for="(item, i) in items"
            :key="i"
            >
            <v-list-item-icon>
                <v-icon small> mdi-circle</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
                <v-list-item-title v-text="item"></v-list-item-title>
            </v-list-item-content>
            </v-list-item>
        </v-list-item-group>
        </v-list>
      </v-card>
    </v-dialog>
  <!-- </v-row> -->
</template>

<script>
import { getUserDetails } from '../../api';
export default {
    setup() {
        
    },
    data:()=>({
        items : [{"text":"Your last post was approved successfully"},
                {"text":"Your last post was disapproved."}]
    }),
    props:{
      user:Object,
    },
    async created(){
      this.items = this.user.notifications;

    },
    methods:{
        async getNotifications(){
          getUserDetails(this.user.id).then(response => {
            this.items = response.data.notifications;
          }).catch(error => {
            console.log(error);
          });

        }
    }
}
</script>