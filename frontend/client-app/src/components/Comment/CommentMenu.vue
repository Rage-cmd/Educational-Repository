<template>
    <v-menu
            bottom
            left
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                icon
                v-bind="attrs"
                v-on="on"
              >
                <v-icon>mdi-dots-vertical</v-icon>
              </v-btn>
            </template>

            <v-list>
              <v-list-item
              >
              <v-list-item-icon>
                <v-icon>mdi-alert-circle-outline</v-icon>
              </v-list-item-icon>
                <v-list-item-title>Report</v-list-item-title>
              </v-list-item>

              <v-list-item
              >
              <v-list-item-icon>
                <v-icon color="green">mdi-check-decagram</v-icon>
              </v-list-item-icon>
                <v-list-item-title>Verify</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
</template>

<script>
export default {
    name:'CommentMenu',
    setup() {
        
    },
    data: ()=>({
        menuopts:["report"],
    }),
    methods:{
    }
}
</script>