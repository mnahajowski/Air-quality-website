import App from './App.vue'
import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from "@/components/main/Main.vue";
import Charts from "@/components/charts/Charts.vue";
import AdminPage from "@/components/admin/AdminPage.vue";

Vue.use(VueRouter)

const routes = [
    { path: '/', component: Main },
    { path: '/charts', component: Charts },
    { path: '/token', component: AdminPage }
]

const router = new VueRouter({
    routes
})

new Vue({
    router,
    render: h => h(App)
}).$mount('#app')