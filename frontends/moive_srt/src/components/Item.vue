<template>
<b-row :class="{highlight: srt.id%2!=0}" :key="srt.id">
    <b-col cols="0.5">
        <b-checkbox name="checkbox-1" v-model="selectLevel1" :value="true"> </b-checkbox>
    </b-col>
    <b-col cols="0.5">
        <b-form-checkbox name="checkbox-2" v-model="selectLevel2" :value="true"> </b-form-checkbox>
    </b-col>


    <b-col cols="1" style="text-align:left;">
        <p>{{numPadding(srt.id,4) }}</p>
    </b-col>

    <b-col cols="9" style="text-align:left;">
        <p>{{content}}</p>
        <b-form-input type="text" v-show="myToggle" @keyup.enter="modifySrt" v-model="content"></b-form-input>

    </b-col>
    <b-col cols="0.5">
        <b-button :pressed.sync="myToggle" size="sm" variant="outline-primary">{{changeStates()}}</b-button>

    </b-col>
    <b-col cols="0.5">
        <b-button variant="outline-primary" @click="updateImgs" size="sm">截图</b-button>
        <!-- :class="{showimg: highLight1.id===srt.id}" 高粱显示非常耗性能 -->
    </b-col>
</b-row>
</template>

<script>
import {
    GetCates,
    GetImgs,
    GetInfoPost
} from "../apis/read.js";

import {
    ref,
    reactive,
    onMounted,
    computed,
} from "@vue/composition-api";

export default {
    name: "Item",
    props: ['srt', 'imglist', 'isSrtTag', 'isImgTag', 'setImgList', 'ifModified',"timeShift", "movie_name","index", "selectImg", "showImgTag","updateItemImgs" ,"highLightChange", "highLight1"],
    setup(props, context) {

        const now_url = ref(context.root.$route.path)

        // console.log("Item data is:",context.root.$route.path)


        var myToggle = ref(false);

        const changeStates = () => {
            const stat = false
            if (stat != myToggle.value) {
                // console.log("myToggle", myToggle.value)

                return "重置";
            } else {
                // console.log("myToggle", myToggle.value)
                return "编辑";
            }
        };
        // 是否点击查看图片
        var showImg = ref(false)

        // const hightLightIndex = props.highLight1

        // 格式化数字
        const numPadding = (num,len) =>{
            const numStr = num.toString()
            return "0".repeat(len-numStr.length) + numStr
        }
        // 计算属性方式更改数据
        const selectLevel1 = computed({
            get() {
                return props.srt.select1
            },
            set(s1) {
                //更改 数据状态
                props.isImgTag(props.srt, s1)
                if (props.srt.select1 == true) {
                    props.selectImg(props.srt, props.index)
                };
                // console.log(props.srt);
            }
        });
        const selectLevel2 = computed({
            get() {
                return props.srt.select2
            },
            set(s2) {
                //更改 数据状态
                props.isSrtTag(props.srt, s2);
                // console.log(props.srt);
            }
        });

        // 截图 请求
        const picParams = reactive({
            url: now_url.value+"/frame", //now_url.value, 对应 flsak 的路由链接
            key: props.movie_name,
            data: "",
            params: ""
        });

        const updateImgs = () => {

            picParams.data = props.srt;
            picParams.params = {"timeshift":props.timeShift}

            // console.log("in Header send data", picParams);
            context.root.$router.push({
                path: now_url.value,   //对应 vue (浏览器)显示 路由链接 eg： http://localhost:8080/create?q=%E6%9C%80%E5%88%9D%E7%9A%84%E6%A2%A6%E6%83%B3&id=4
                query: {
                    // q: picParams.key,
                    id: props.srt.id
                }
            });

            var getimgs = []
            if (props.srt.img_ls.length === 0) {
                console.log("In Pic data = ", picParams);
                GetInfoPost(picParams).then(resp => {
                    console.log("In Pic title = ", resp.data.data);
                    if (resp.data.data.length > 0) {
                        getimgs = resp.data.data[0];
                    } else {
                        getimgs = ['./data/cover/cover.png'];
                    };
                    // 更新显示图片的图片序列
                    props.setImgList(getimgs);

                    // 更新原始数据中的图片列表
                    props.updateItemImgs(props.srt.id-1, getimgs)

                    // console.log("In after data = ", props.srt.img_ls );
                });

            } else {
                props.setImgList(props.srt.img_ls);
            };

            showImg.value = true;
            // console.log("showImg",showImg);

            //高亮显示某一行
            // 返回索引
            props.highLightChange(props.highLight1, props.srt.id)


        };

        const content = ref(props.srt.content)

        const modifySrt = () => {
            // 更改内容的毁掉函数
            props.ifModified(props.srt, content.value);
            myToggle.value = false;
        }

        return {
            myToggle,
            changeStates,
            selectLevel1,
            selectLevel2,
            updateImgs,
            modifySrt,
            content,
            showImg,
            numPadding,
            // hightLightIndex,
        }
    },
}
</script>

<style>
.highlight {
    background: rgb(245, 242, 239)
}

.level1 {
    background: rgb(247, 225, 198)
}

.level2 {
    background: rgb(247, 225, 198)
}

.showimg {
    background: rgb(114, 224, 243)
}
</style>
