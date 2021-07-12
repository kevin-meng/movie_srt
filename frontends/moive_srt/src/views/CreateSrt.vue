<template>
<div class="home">
    <Header />

    <b-container id="result" class="flex" fluid>
        生成的结果图片
    </b-container>
    <Footer />

</div>
</template>

<script>
// @ is an alias to /src
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";

import {
    GetCates,
    GetImgs,
    GetInfoPost
} from "../apis/read.js";
import {
    ref,
    reactive,
    onMounted,
    computed
} from "@vue/composition-api"; // ref,

export default {
    name: "CreateSrt",
    components: {
        Header,
        Footer
    },
    setup(props, context) {

          const srtParams = reactive({
            url: "/create", //now_url.value,
            key: '123',
            imgType:1,
            data:"124",
            srtSize:""
        });
        // 创建处理后的结果数据
        const resultData = reactive({
            result:[]
        });

        GetInfoPost(srtParams).then(resp => {
        //   console.log("In Home title = ", resp);
          console.log("In Home title = ", resp.data.data);
          resultData.result = resp.data.data;
        //   console.log("In Home title = ", resp.data.data);
        //   document.title = resp.data.data[0];
        //   document.querySelector('meta[name="keywords"]').setAttribute("content", resp.data.data[1]);
        //   document.querySelector('meta[name="description"]').setAttribute("content", resp.data.data[2]);
        });

        return {
            movieSrtData,
            srtParams,
            resultData,
            
        }
    },
};
</script>

<style lang="scss" scoped>
.toggle {
    color: #fff;
    background-color: #007bff;
    border-color: #007bff;
}

</style>
