<template>
<div class="home">
    <Header />

    <b-container id="movie" class="flex" fluid>

        <b-row>
            <b-col cols="5">

                <b-container id="col_img" clsss="img_contral">
                    <b-row >
                        <h6 class="movie_name">电影名：{{movie_name}}</h6>
                    </b-row>
                    <b-row>
                        <img class="img_window" :src="img_ls[index]" />
                    </b-row>
                    <!-- <p>{{imglist.img_ls}}</p> -->
                    <p>{{index + 1 }}/{{img_ls.length}}</p>
                    <b-row class="my-3">
                        <b-col sm="4">
                            <b-button variant="outline-primary" @click="prev" size="sm" :disabled="index==0">上 一 张</b-button>
                        </b-col>
                        <b-col sm="2">
                            <b-button variant="outline-primary" @click="next" size="sm" :disabled="index>=(img_ls.length-1)">下 一 张</b-button>
                        </b-col>
                        <b-col sm="5">
                            <b-button variant="outline-primary" size="sm">过 滤</b-button>
                        </b-col>
                    </b-row>

                    <b-row class="my-3">
                        <b-col sm="4">
                            <b-form-checkbox v-model=ifContent >使用文本</b-form-checkbox>
                            <!-- <b-button :pressed.sync="ifContent" variant="primary" size="sm">原图字幕</b-button> -->
                        </b-col>
                        <b-col sm="2">
                            <b-button variant="info" size="sm" type="submit" @click="toCreate">一键生成</b-button>
                        </b-col>
                        <b-col sm="5">
                            <b-button variant="info" size="sm" @click="clearAllSelect(false)">清空选项</b-button>
                        </b-col>

                    </b-row>

                    <b-row class="my-3">
                        <!-- <b-col sm="2">
                            <b-button variant="info" size="sm">原图字幕</b-button>
                        </b-col> -->
                        <b-col sm="4">
                            封面区域:
                        </b-col>
                        <b-col sm="2">
                            <b-form-input placeholder="宽左" id="img_w1"></b-form-input>
                        </b-col>
                        <b-col sm="2">
                            <b-form-input placeholder="高上" id="img_h1"></b-form-input>
                        </b-col>
                        <b-col sm="2">
                            <b-form-input placeholder="宽右" id="img_w2"></b-form-input>
                        </b-col>
                        <b-col sm="2">
                            <b-form-input placeholder="高下" id="img_h2"></b-form-input>
                        </b-col>
                    </b-row>

                    <b-row class="my-3">

                        <b-col sm="4">
                            字幕区域:
                        </b-col>
                        <b-col sm="2">
                            <b-form-input placeholder="宽左" id="srt_w1"></b-form-input>
                        </b-col>
                        <b-col sm="2">
                            <b-form-input placeholder="高上" id="srt_h1"></b-form-input>
                        </b-col>
                        <b-col sm="2">
                            <b-form-input placeholder="宽右" id="srt_w2"></b-form-input>
                        </b-col>
                        <b-col sm="2">
                            <b-form-input placeholder="高下" id="srt_h2"></b-form-input>
                        </b-col>

                    </b-row>

                    <b-row class="my-3">

                        <b-col sm="4">
                            字体大小:
                        </b-col>
                        <b-col sm="2">
                            <b-form-input placeholder="字体" v-model="fontSize" id="font_w1"></b-form-input>
                        </b-col>
                        <b-col sm="4">
                            时间偏移[回车]:
                        </b-col>
                        <b-col sm="2">
                            <b-form-input placeholder="字体" v-model="timeShift" @keyup.enter="clearImgs"  id="time_w1"></b-form-input>
                        </b-col>
                    </b-row>
                    <b-row class="my-3">

                    </b-row>
                    <b-row>
                        <b-col sm="1">
                        </b-col>

                        <!-- <h4>结果图片</h4> -->
                        <b-col sm="11">
                        <ol>
                            <li v-for="(i_url,index) in resultData.result_img" :key="index">
                                <a :href="i_url">{{i_url}}</a>
                            </li>

                        </ol>
                        </b-col>
                    </b-row>

                </b-container>

            </b-col>

            <b-col style="background-color:white;" cols="7">

                <b-container fluid>
                                <b-col lg="6" class="my-1">
                                  <b-form-group
                                    label="搜索台词"
                                    label-for="filter-input"
                                    label-cols-sm="3"
                                    label-align-sm="right"
                                    label-size="sm"
                                    class="mb-0"
                                  >
                                    <b-input-group size="sm">
                                      <b-form-input
                                        id="filter-input"
                                        v-model="filter"
                                        type="search"
                                        placeholder=""
                                      ></b-form-input>
    
                                      <b-input-group-append>
                                        <b-button :disabled="!filter" @click="filter = ''">取消筛选</b-button>
                                      </b-input-group-append>
                                    </b-input-group>
                                  </b-form-group>
                                </b-col>
    
                                    <!-- 分页量选择框 -->
                                  <b-col sm="5" md="6"  class="my-1">
                                    <b-form-group
                                      label="完成状态"
                                      label-for="per-page-select"
                                      label-cols-sm="6"
                                      label-cols-md="4"
                                      label-cols-lg="3"
                                      label-align-sm="right"
                                      label-size="sm"
                                      class="mb-0"
                                    >
                                      <b-form-select
                                        id="per-page-select"
                                        v-model="srtStatus"
                                        :options="srtOptions"
                                        size="sm"
                                      ></b-form-select>
                                    </b-form-group>
                                  </b-col>

                                <!-- 分页量选择框 -->
                                  <b-col sm="5" md="6"  class="my-1">
                                    <b-form-group
                                      label="分页大小"
                                      label-for="per-page-select"
                                      label-cols-sm="6"
                                      label-cols-md="4"
                                      label-cols-lg="3"
                                      label-align-sm="right"
                                      label-size="sm"
                                      class="mb-0"
                                    >
                                      <b-form-select
                                        id="per-page-select"
                                        v-model="perPage"
                                        :options="pageOptions"
                                        size="sm"
                                      ></b-form-select>
                                    </b-form-group>
                                  </b-col>
    
                                  <!-- 分页数据显示 -->
                                  <b-col sm="7" md="6" class="my-1">
                                    <b-pagination
                                      v-model="currentPage"
                                      :total-rows="totalRows"
                                      :per-page="perPage"
                                      align="fill"
                                      size="sm"
                                      class="my-0"
                                    ></b-pagination>
                                  </b-col>
                                <!-- 表格数据 -->


                                  <!-- 高亮显示修改行:tbody-tr-class="highlightModifyRowSrt"  -->
                                  <!-- :row-hovered="rowButtonShow"  -->
                                <b-table
                                  :items="filterSrts(items,srtStatus)"
                                  :fields="fields"
                                  :tbody-tr-class="highlightModifyRowSrt"     
                                  :current-page="currentPage"
                                  :per-page="perPage"
                                  :filter="filter"
                                  :filter-included-fields="filterOn"
                                  :sort-by.sync="sortBy"
                                  :sort-desc.sync="sortDesc"
                                  :sort-direction="sortDirection"
                                  stacked="md"
                                  show-empty
                                  hover 
                                  small
                                  @filtered="onFiltered"
                                   >
                                     <template #cell(select1)="row">
                                    <b-form-checkbox size="sm" class="switch" name="checkbox-1" v-model="row.item.select1"  :value="true" >
                                     </b-form-checkbox>
                                    </template>

                                    <template #cell(select2)="row">
                                    <b-form-checkbox size="sm" class="switch" name="checkbox-1" v-model="row.item.select2"  :value="true" >
                                     </b-form-checkbox>
                                     </template>   
                                    


                                    <!-- 自增的索引序列  https://bootstrap-vue.org/docs/components/table#jane-doe -->
                                    <!-- <template #cell(id)="data"> -->
                                        <!-- {{ data.index + 1 }} -->
                                    <!-- </template> -->

                                <!-- 触发展示模板 -->
                                 <!-- <template #cell(insert)="row">
                                    <b-button size="sm" variant="outline-primary" v-show="showButton"  @click="row.toggleDetails"  class="mr-1">
                                      插入
                                    </b-button>
                                  </template> -->

                                <!-- 触发展示模板 -->
                                 <template #cell(modify_srt)="row">
                                    <b-button size="sm" variant="outline-primary" v-show="showButton"  @click="row.toggleDetails"  class="mr-1">
                                    <!-- row.toggleDetails -->
                                      修改
                                    </b-button>
                                  </template>

                                <!-- 触发展示模板 -->
                                 <template #cell(action)="row">
                                    <b-button size="sm" variant="outline-primary" v-show="showButton"   @click="getRowFrameValue(row)"  class="mr-1">
                                    <!-- row.toggleDetails -->
                                      截图
                                    </b-button>
                                  </template>
                                <!-- 展示的卡片模板 -->
                                <template #row-details="row">
                                  <b-card>
                                      <b-row>
                                        <b-form-input class="sub_input" v-model="row.item.modify" ></b-form-input>
                                      <hr>  
                                      <b-col>
                                        开始时间:
                                      </b-col>
                                        <b-col>
                                        <b-form-input  v-model="row.item.start" ></b-form-input>
                                      </b-col>
                                      <b-col>
                                        结束时间:
                                      </b-col>
                                        <b-col>
                                        <b-form-input  v-model="row.item.end" ></b-form-input>
                                      </b-col>


                                        <!-- <b-form-input  v-model="row.item.end" ></b-form-input> -->
                                      <!-- <b-row> -->
                                        <b-button size="sm" variant="outline-primary"   @click="insertRowValue(row)" > 向上插入</b-button>
                                      </b-row>
                                  </b-card>

                                </template>

                                </b-table>

                                <b-modal :id="infoModal.id" :title="infoModal.title" ok-only @hide="resetInfoModal">
                                    <pre>{{ infoModal.content }}</pre>
                                </b-modal>

                </b-container>
            </b-col>

        </b-row>

    </b-container>
    <Footer />

</div>
</template>

<script>
// @ is an alias to /src
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
import Item from "../components/Item.vue";
// 引入数据接口  报错
// import {Srt} from "../types/srt.ts";

import {
    GetMovies,
    GetImgs,
    GetInfoPost
} from "../apis/read.js";
import {
    ref,
    reactive,
    onMounted,
    computed,
    toRefs,
} from "@vue/composition-api"; 

export default {
    name: "MovieSrt",
    components: {
        Header,
        Footer,
        Item,
    },

    setup(props, context) {

        const now_url = ref(context.root.$route.path)


        // 页面布局数据
        const pageParams = reactive({
                movie_name:"",
                index:0,  //显示图片的索引
                totalRows: 1,
                currentSrtIndex:0,  // 当前字幕的索引
                img_ls: ["http://127.0.0.1:3306/static/data/cover/cover.png"],  //初始显示封面图
                ifContent:false,        // 用字幕or原图 
                fontSize:60,         // 字体大小
                timeShift:0,         // 校准字幕的时间偏移量
                showButton:true,
                currentPage: 1,
                getFrameTime:0,   // 仅仅抽取时间
                perPage: 15,    
                pageOptions: [150, 300, 500, { value: 1000, text: "Show a lot" }],
                srtOptions:['all','select'],
                srtStatus:'all',
                sortBy: '',
                sortDesc: false,
                sortDirection: 'asc',
                filter: null,
                filterOn: [],
                infoModal: {
                    id: 'info-modal',
                    title: '',
                    content: ''}

        });        


        // 转化为表格数据
        const tableData = reactive({
            fields :[{ key: 'select1', label: '图' },
                    { key: 'select2', label: '文' },
                    { key: 'id', label: 'ID'},
                    { key: 'modify', label: '台词', sortable: true, sortDirection: 'desc'},  // class: 'text-center' 
                    { key: 'insert', label: '' },
                    { key: 'modify_srt', label: '' },
                    { key: 'action', label: '' },
                        ],
            items:[],
        })


        const getSrtParams = reactive({
            url: now_url.value, //now_url.value,
            key: 1,   // 改用最初的梦想  -->  id 
            data: "",
            params: ""
        });


        // 改用 Post 方法
        // GetCates().then(response => {
        //     console.log("data is:",response.data)
        //     movieSrtData.movie_srt_ls = response.data.data;
        // });

        // post 获取电影字幕
        GetInfoPost(getSrtParams).then(resp => {
            console.log("In Home Data = ", resp.data.data);
            // movieSrtData.movie_srt_ls = resp.data.data.data ;
            pageParams.movie_name = resp.data.data.name ;

            // 表格数据
            tableData.items = resp.data.data.data;
            console.log("数据",resp.data.data.data)
            pageParams.totalRows = tableData.items.length;
        });


        // const rowButtonShow = (item, index,event)=>{
        //     pageParams.rowButtonShow = true;
        // }
        // const getFrameTime = ref

        const insertRowValue = (row)=>{
            if  (String(row.item.id).endsWith(".5")=== false) {

                const inserData = reactive({
                    content:"",
                    start: row.item.start,
                    end: row.item.end,
                    id: row.item.id-0.5,
                    img_ls: [],
                    img_select: 0,
                    img_start: "00000",
                    modify: "    ",
                    select1: true,
                    select2: false
                });
                // 插入数据
                tableData.items.splice(row.item.id-1,0,inserData);
            };
        };




        const next = () => {
            if (pageParams.index < (pageParams.img_ls.length - 1)) {
                pageParams.index++;

                // 修改 字幕选择的 图片序号.
                tableData.items[pageParams.currentSrtIndex -1 ]['img_select'] = pageParams.index;

            }
        };
        const prev = () => {
            if (pageParams.index >= 1) {
                pageParams.index--;

                // 修改 字幕选择的 图片序号.
                tableData.items[pageParams.currentSrtIndex -1 ]['img_select'] = pageParams.index;
            }
        };


        // 修改 时间偏移后 ,清空 图片列表 重新获取
        const clearImgs = ()=>{
            tableData.items.forEach((srt) => {
                srt.img_ls = [];
            })
            // console.log("result2 :", tableData.items)
            };

        // 清空勾选
        const clearAllSelect = (ifSelect) => {
            tableData.items.forEach((srt) => {
                srt.select1 = ifSelect;
                srt.select2 = ifSelect;
            })
        };



        // 创建拼接处理后的结果数据
        const resultData = reactive({
                result_img: []
        });


        // 获取台词的截图
        const getRowFrameValue = (row)=>{
            console.log("ROW data:",row)
            // console.log("now_url",now_url)

            // 更新图片时需要的回调函数
            const setImgList = (imgs) => {
                // 将索引变为零
                pageParams.index = 0;
                // console.log("更新前的数据：", imgs);
                // console.log("更新后的数据：",imgs);                                       
                pageParams.img_ls = imgs.map(function (img) {
                    // 通过静态资源托管
                    return "http://127.0.0.1:3306/static/" + img.substr(2) // "data/1/imgs/9.72_12.6_0.png"
                });
                // console.log("更新后的数据：", movieSrtData.movie_srt_ls);
            };

            // 修改当前的字幕索引
            pageParams.currentSrtIndex = row.item.id;
            console.log("pageParams.currentSrtIndex: ",pageParams.currentSrtIndex )


            //发送到服务器,修改电影状态
            const  picParams = reactive({
                url: now_url.value+"/frame", //now_url.value, 对应 flsak 的路由链接
                key: pageParams.movie_name,
                data: row.item,
                params: ""
            });

            picParams.params = {"timeshift":pageParams.timeShift}

            // console.log("in Header send data", picParams);
            context.root.$router.push({
                path: now_url.value,   //对应 vue (浏览器)显示 路由链接 eg： http://localhost:8080/create?q=%E6%9C%80%E5%88%9D%E7%9A%84%E6%A2%A6%E6%83%B3&id=4
                query: {
                    // q: picParams.key,
                    id: row.item.id
                }
            });


            var getimgs = []

            // console.log("In before data = ", tableData.items);
            if (row.item.img_ls.length === 0) {
                // console.log("In Pic data = ", picParams);
                GetInfoPost(picParams).then(resp => {
                    // console.log("In Pic title = ", resp.data.data);
                    if (resp.data.data.length > 0) {
                        getimgs = resp.data.data[0];
                    } else {
                        getimgs = ['./data/cover/cover.png'];
                    };
                    // 更新显示图片的图片序列
                    setImgList(getimgs);
                    // 更新原始数据中的图片列表
                    tableData.items[row.index]['img_ls'] = getimgs

                    console.log("In after data = ", tableData.items);
                });
                } else {
                    setImgList(row.item.img_ls);
                };
            };

        // 生成台词截图
        const toCreate = () => {

            const srtParams = reactive({
                url: now_url.value + "/create",  //now_url.value, 对应 flsak 的路由链接
                key: "",   // 改用 返回的电影名  -->  id 
                data: "",
                params: ""
            });

            // console.log(movieSrtData.movie_srt_ls)
            srtParams.data = tableData.items.filter(srt => ((srt.select1) || (srt.select2)))
            srtParams.key = pageParams.movie_name
            srtParams.params = {
                ifContent: pageParams.ifContent,
                fontSize: pageParams.fontSize,
            }
            // console.log(srtParams)

            console.log("in Header send data", srtParams);
            context.root.$router.push({
                path: now_url.value,    //对应 vue (浏览器)显示 路由链接  不跳转
                query: {
                    q: srtParams.key
                }
            });

            GetInfoPost(srtParams).then(resp => {
                const img_url = "http://127.0.0.1:3306/static/" + resp.data.data[0].substr(3)
                resultData.result_img.push(img_url);
                console.log("In Home title = ", resultData.result_img);

            });
        };

        // 修改字幕数据 则高亮显示
        const highlightModifyRowSrt = (item,type)=>{
            if (!item || type !== 'row') return 
            if (item.modify !== item.content) return 'table-success'
            };


        const filterSrts = (srts,srtStatus)=>{
            if (srtStatus =='select') {
                return srts.filter(srt => ((srt.select1) || (srt.select2)));
            }  else {
                return srts;
            }
        };

        const info = (item, index, button) => {
            pageParams.infoModal.title = `Row index: ${index}`
            pageParams.infoModal.content = JSON.stringify(item, null, 2)
            pageParams.$root.$emit('bv::show::modal', pageParams.infoModal.id, button)
        };
        const resetInfoModal = () =>  {
            pageParams.infoModal.title = ''
            pageParams.infoModal.content = ''
        };
        const onFiltered = (filteredItems) => {
            // Trigger pagination to update the number of buttons/pages due to filtering
            pageParams.totalRows = filteredItems.length
            pageParams.currentPage = 1
        };


        return {
            info,
            prev,
            next,
            getRowFrameValue,
            highlightModifyRowSrt,
            filterSrts,
            // rowButtonShow,
            resetInfoModal,
            onFiltered,
            insertRowValue,
            toCreate,
            resultData,
            clearImgs,
            clearAllSelect,
            ...toRefs(pageParams),  // 拆解对象
            ...toRefs(tableData),

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

.movie_name {
    // 固定 图片边栏  https://c.runoob.com/codedemo/5664
    margin-top: 20px;
    margin-left: 1%;
    top: 20px;
    font-weight: bold;
}



#col_img {
    // 固定 图片边栏  https://c.runoob.com/codedemo/5664
    margin-top: 0px;
    background: rgb(240, 241, 239);
    // color: rgb(143, 173, 173);
    height: 900px; //100%
    // width: 555px;
    // box-shadow:4px 4px 4px #3C3F35;
    border-radius: 0px;
    margin-left: 1%;

    position: sticky;
    position: -webkit-sticky;
    top: 20px;
}

.sub_input {
    margin-bottom: 10px;
}    



#col_img img {
    // 图片窗口
    margin-top: 30px;
    margin-left: 100px;
    margin-bottom: 10px;

    width: 500px;
}

.srt_header {
    margin-top: 20px;
    border-bottom: 1px dashed rgb(129, 128, 128);
}
</style>
