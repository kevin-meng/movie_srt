import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import MovieSrt from "../views/MovieSrt.vue";
import CreateSrt from "../views/CreateSrt.vue";


// 台词处理页

// import HomeCate from "../views/HomeCate.vue";
// import BookIndex from "../views/BookIndex.vue";
// import BookDetail from "../views/BookDetail.vue";
// import BookSearch from "../views/BookSearch.vue"

Vue.use(VueRouter);

const routes = [{ // 网站首页
        path: "/",
        name: "Home",
        component: Home
    },

    // // 网站分类页面 search
    {
        path: "/movie_srt/:movie_id",
        name: "MovieSrt",
        component: MovieSrt
    },

    // 生成结果图片
    {
        path: "/create",
        name: "ToCreate",
        component: CreateSrt
    }
    // // 图书首页
    // {
    //     path: "/book/:book_id",
    //     name: "BookIndex",
    //     component: BookIndex,
    // },

    // // 图书详情页
    // {
    //     path: "/book/:book_id/:sort_id",
    //     name: "BookDetail",
    //     component: BookDetail
    // },

];

const router = new VueRouter({
    mode: "history",
    base: process.env.BASE_URL,
    routes
});

export default router;