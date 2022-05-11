import Vuex from 'vuex';
import Vue from 'vue';

Vue.use(Vuex);

// Create a new store instance.
export const store = new Vuex.Store({
  state () {
    return {
      posts: [],
      user:{},
      currentScreen:'',
      suggestions:[],
      snackbar:false,
      snackbarMessage:'',
    }
  },
  mutations: {
    setPosts (state, posts) {
        console.log("setPosts: " + JSON.stringify(posts));
        state.posts = posts
    },
    setUser (state, user) {
        state.user = user
    },
    setSuggestions(state, suggestions){
        state.suggestions = suggestions
    }
  }
});
