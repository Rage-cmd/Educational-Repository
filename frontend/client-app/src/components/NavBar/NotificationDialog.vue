<template>
    <v-dialog
      max-width="800"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn icon v-bind="attrs" v-on="on">
                <v-icon>mdi-bell-outline</v-icon>
        </v-btn>
      </template>
      <v-card>
        <v-list dense disabled>
        <v-subheader>Notfications</v-subheader>
        <v-list-item-group
            color="primary"
        >
            <v-list-item
            v-for="(item, i) in items"
            :key="i"
            >
            <v-list-item-icon>
                <v-icon small> mdi-circle</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
                <v-list-item-title v-text="item.text"></v-list-item-title>
            </v-list-item-content>
            </v-list-item>
        </v-list-item-group>
        </v-list>
      </v-card>
    </v-dialog>
  <!-- </v-row> -->
</template>

<script>
export default {
    setup() {
        
    },
    data:()=>({
        items : [{"text":"Your last post was approved successfully"},
                {"text":"Your last post was disapproved."}]
    }),
}
</script>