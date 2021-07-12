<template>
    <div class="home">
        <Header />
        <b-container fluid>
            <b-row>
                <b-col cols="6" style="height:800px">
                    <h4 class="title">电影列表</h4>
    
       
                                <b-col lg="6" class="my-1">
                                  <b-form-group
                                    label="搜索电影"
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
                                        v-model="movieStatus"
                                        :options="movieOptions"
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
                                <b-table
                                  :items="filterMovies(items,movieStatus)"
                                  :fields="fields"
                                  :current-page="currentPage"
                                  :per-page="perPage"
                                  :filter="filter"
                                  :filter-included-fields="filterOn"
                                  :sort-by.sync="sortBy"
                                  :sort-desc.sync="sortDesc"
                                  :sort-direction="sortDirection"
                                  stacked="md"
                                  show-empty
                                  small
                                  @filtered="onFiltered"
    
                                   >
                                    <!-- 自增的索引序列  https://bootstrap-vue.org/docs/components/table#jane-doe -->
                                    <template #cell(id)="data">
                                        {{ data.index + 1 }}
                                    </template>


                                  <template #cell(movie_info)="data">
                                    <!-- `构造链接 -->
                                    <a :href="`movie_srt/${data.value.id}`">{{ data.value.movie }}</a>
                                  </template>
                                    <!-- 调整完成情况开关 -->
                                    <template #cell(ifFinish)="row">
                                    <b-checkbox size="sm" class="switch" name="checkbox-1" v-model="row.item.ifFinish"  :value="true" switch>
                                     </b-checkbox>
    
    
                                  </template>
                                <!-- 触发展示模板 -->
                                 <template #cell(action)="row">
                                    <b-button size="sm" variant="outline-primary"  @click="changeRowValue(row)"  class="mr-1">
                                    <!-- row.toggleDetails -->
                                      发送
                                    </b-button>
    
                                  </template>
                                <!-- 展示的卡片模板 -->
                                <template #row-details="row">
                                  <b-card>
                                    <ul>
                                      <li v-for="(value, key) in row.item" :key="key">{{ key }}: {{ value }}</li>
                                    </ul>
                                  </b-card>
                                </template>

                                </b-table>

                                <b-modal :id="infoModal.id" :title="infoModal.title" ok-only @hide="resetInfoModal">
                                    <pre>{{ infoModal.content }}</pre>
                                </b-modal>


<!-- <b-row>
                        <b-col cols= 10>
                            <b-form-input class="input" v-model="filter" placeholder="输入电影名" @keyup.enter="add" ></b-form-input>
                        </b-col>
                            <b-col ols= 2>
                        <b-button class="movie_add" variant="outline-primary" size="sm">添加</b-button>
                            </b-col>
                    </b-row> -->

<!-- v-for  笨办法解决数据问题 -->
<!-- <div translate="translate" class="bd-example vue-example vue-example-b-table">
                        <div> -->
<!-- <table role="table" aria-busy="false" class="table  table-hover">
                                <thead role="rowgroup" class="">
                                    <tr role="row" class="">
                                        <th role="columnheader" aria-colindex="1" >
                                            <div>ID</div>
                                        </th>
                                        <th role="columnheader" aria-colindex="2" >
                                            <div>电影名</div>
                                        </th>
                                        <th role="columnheader" aria-colindex="3" >
                                            <div>评分</div>
                                        </th>                                    
                                        <th ria-colindex="4">
                                            <div>状态</div>
                                        </th>
                                        <th >
                                            <div>操作</div>
                                        </th>
                                    </tr>
                                </thead>
                                <tbody role="rowgroup">
                                    <tr role="row" v-for="(movie, index) in movies" :key="movie.id"  class="">
                                        <th>
                                        <td  class="text-center" role="cell">{{index+1}}</td>
                                        </th>
                                        <th>
                                        <td class="text-center" role="cell"><a :href="'/movie_srt/'+ movie.id" > {{movie.movie}} </a></td>
                                        </th>
                                        <th>
                                        <td class="text-center" role="cell">{{movie.score}}</td>
                                        </th>
                                        <th>
                                        <b-checkbox class="switch" name="checkbox-1" v-model="movie.ifFinish" :value="true" switch> </b-checkbox>
                                        </th>
                                        <th>
                                         <b-button class="movie_check" variant="outline-primary" size="sm">发送</b-button>
                                         </th>
                                    </tr>
                                  
                                </tbody>
                            </table> -->
<!-- </div> -->
<!-- </div> -->
</b-col>

<b-col cols="6" style="height:800px">
    <h4 class="title">预览框</h4>
    <!-- <h5>{{getMovieDetail.data}}</h5> -->
    <!-- <h5>{{"电影名:" + movie_name}}</h5> -->

    <!-- <span>{{getMovieDetail.data}}</span> -->

    <!-- <span>简介:</span>
    <span>{{movie_info}}</span> -->
  <b-container id="col_img" clsss="movie_detail">

    <b-row class="my-1">
        <b-col sm="2" class="my-2">
            电影名:
        </b-col>
        <b-col sm="5" class="my-3">
          {{movie_name}}
        </b-col>

        <b-col sm="5">
          <img :src="pic_url" alt="">
        </b-col>
    </b-row>

    <b-row class="my-1">
        <b-col sm="2" class="my-2">
            下载链接:
        </b-col>
        <b-col sm="10" class="my-3">
           <a :href="download_url">{{download_url}}</a>
          <!-- {{download_url}} -->
        </b-col>
    </b-row>

    <b-row  class="my-1">
      <b-col sm="2" class="my-2">
            评分:
      </b-col>
      <b-col sm="10">
          <b-row v-for="(info,index) in score_ls"  :key="index">
              <b-col sm="2" class="my-3">
                  {{info.type}}
               </b-col>
              <b-col sm="4" >
                  {{info.score}} 分
               </b-col>    
              <b-col sm="5">
                  <a :href="info.href">详情页面</a>
               </b-col>                         
            <!-- {{info}} -->
          </b-row >
      </b-col>
    </b-row>
      <hr>
    <b-row class="my-1">
        <b-col sm="2" class="my-2">
            简介:
        </b-col>
        <b-col sm="10" class="m_info">
          <b-row v-for="(info,index) in movie_info" :key= "index">
            <span>{{info}}</span>
          </b-row>
          <!-- {{movie_info}} -->
        </b-col>
    </b-row>

 
    </b-container>
<!-- // { "desc": "蓝色星球.第2季..央视国配字幕.2017", "lang": "简体 官方译本", "movie_actor": [ "大卫·爱登堡" ], 
// "movie_director": [ "詹姆斯·霍尼伯内" ], "movie_id": "388087",
//  "movie_info": "招募影视资料编辑，有意向的可发邮件 至此处 ，谢谢支持 豆瓣: 9.8 IMDb: 9.4 类型：英国 纪录片 导演：詹姆斯·霍尼伯内 演员：大卫·爱登堡 介绍：《蓝色星球II》将由大卫·爱登堡爵士主持。在长达4年的拍摄过程中, 制作团队共执行了125次的探险，水下拍摄时数长达到6000多个小时。与2001年首播的《藍色星球》相隔16年之后，制作团队透过新的科技技术突破以往限制，将许多过去未知的地带、惊人的生物及其令人瞠目结舌的举动呈现在观众眼前 .. 全部介绍 自从《蓝色星球》2001年开播以来，我们对大海之下生命的理解被彻底颠覆了。从北极熊出没的北冰洋到焕发着勃勃生机的蓝色珊瑚环礁，本系列纪录片同大家分享一些令人吃惊的新发现；邂逅在南冰洋深处神出鬼没的奇怪章鱼，观赏巨大的鲹鱼跳出水面，飞跃到半空中捕鱼；骑在虎鲸的背上，同它一起冲向鱼群。《蓝色星球2》带领我们体验让人敬畏称奇的新地方，见识魅力四射的新物种，了解非同寻常的新行为。 暂无 蓝色星球2 的更多字幕",
//   "movie_name": "蓝色星球2", "movie_page_url": "https://subdh.com/d/26979545", "movie_type": [ "英国 纪录片" ], "movie_url": "/a/388087", 
//   "n": 1, "nModified": 0, "ok": 1, 
//   "pic_url": "https://img.subhd.la/poster/l/p2544388666.jpg", 
//   "score_ls": [ { "href": "https://movie.douban.com/subject/26979545", "score": "9.8", "type": "豆瓣" },
//  { "href": "https://www.imdb.com/title/tt6769208", "score": "9.4", "type": "IMDb" } ], "updatedExisting": true }
 -->

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

import {
    GetMovies,
    GetInfoPost
} from "../apis/read.js";
import {
    ref,
    reactive,
    onMounted,
    toRefs,
    mounted,
    computed,
        
} from "@vue/composition-api"; // ref,

export default {
    name: "Home",
    components: {
        Header,
        Footer},

    setup(props, context) {

        const now_url = ref(context.root.$route.path)
        const movieList = reactive({
            movies: [],
        });

        // 初始请求电影数据
        GetMovies().then(response => {
            // console.log("data is:",response.data);
            movieList.movies = response.data.data;
            // console.log("movie list: ",movieList.movies);
            tableData.items = response.data.data.map(function(item) {

              return {"movie_info":{'movie':item.movie_name,'id':item.movie_id}, 'ifFinish':item.ifFinish,'score':item.score }
            });
            pageParams.totalRows = tableData.items.length
            // console.log("movie list: ",tableData.fields);
            // console.log("movie list: ",tableData.items); 
        })

        // 转化为表格数据
        const tableData = reactive({
          fields :[{ key: 'id', label: 'ID', sortable: true },
                   { key: 'movie_info', label: '电影名', sortable: true, sortDirection: 'desc', class: 'text-center' },
                        {
                          key: 'score',
                          label: '评分',
                          // formatter: (value, key, item) => {
                          //   return value ? 'Yes' : 'No'
                          // },
                          sortable: true,
                          sortByFormatted: true,
                          filterByFormatted: true
                        },
                        { key: 'ifFinish', label: '状态' },
                        { key: 'action', label: '操作' },
                      ],
          items:[],
        })
        // 页面布局数据
        const pageParams = reactive({
                totalRows: 1,
                currentPage: 1,
                perPage: 15,
                pageOptions: [15, 30, 50, { value: 100, text: "Show a lot" }],
                movieOptions:['all','finish','unfinish'],
                movieStatus:'all',
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


      const  getMovieDetail = reactive({
        data:"",
        movie_id:"",
        movie_name:"",
        movie_actor:"",
        desc:"",
        movie_info:"",
        score_ls:"",
        download_url:"",
        pic_url:"",
        movie_url:"",
        movie_type:"",
        // data:""
      })
      const changeRowValue = (row)=>{
        // return
        console.log(row)
        console.log("now_url",now_url)
        //发送到服务器,修改电影状态
        const  movieParams = reactive({
            url: now_url.value+"change_movie", //now_url.value, 对应 flsak 的路由链接
            key: row.item.movie_info.id,
            data: row,
            params: ""
        });

        GetInfoPost(movieParams).then(resp => {
                            console.log("In change movie status = ", resp.data.data);
                            // if (resp.data.data.length > 0) {
                            //     getimgs = resp.data.data[0];
                            // } else {
                            //     getimgs = ['./data/cover/cover.png'];
                            // };
                            // 返回的结果进行赋值保存 放在详细页面展示
                            getMovieDetail.data = resp.data.data;
                            getMovieDetail.movie_id = resp.data.data.movie_id;
                            getMovieDetail.movie_name = resp.data.data.movie_name;
                            getMovieDetail.movie_actor = resp.data.data.movie_actor;
                            getMovieDetail.desc = resp.data.data.desc;
                            getMovieDetail.movie_info = resp.data.data.movie_info.split(" ").filter(item =>(item.length>6)&&(!item.startsWith("招募")));
                            //  {
                            //           if ((item.length>6)&&(~item.startsWith("招募")){
                            //             return item;
                            //           }
                            //         });
                            getMovieDetail.score_ls = resp.data.data.score_ls;

                            getMovieDetail.download_url = resp.data.data.movie_page_url;
                            getMovieDetail.pic_url = resp.data.data.pic_url;
                            getMovieDetail.movie_url = "https://subdh.com/" + resp.data.data.movie_url;
                            getMovieDetail.movie_type = resp.data.data.movie_type;
                     });
                     console.log(getMovieDetail)
      };
      
      const filterMovies = (items,movieStatus)=>{
            if (movieStatus =='finish') {
              return items.filter(item =>item.ifFinish=== true);
            } else if (movieStatus === 'unfinish') {
              return items.filter(item =>item.ifFinish=== false);
            } else {
              return items;
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
        }

        const movieName = ref("")


        // const getMovieDetail = 

        // // 回车的事件回调函数，用来添加数据
        // const add = () => {
        //     const text = movieName.value;

        //     // if (text.trim()) return 
        //     const movie = {
        //         id:Date.now(),
        //         movie:text,
        //         isFinshed:false,
        //     };
        //     movieName.value = "";
        //     // console.log(movie);
        //         // 调用addMovie 方法
        //         movieList.movies.unshift(movie);
        //     }

        return {
            info,
            // add,
            changeRowValue,
            filterMovies,
            // addMoive,
            movieName,
            resetInfoModal,
            onFiltered,
            getMovieDetail,
            ...toRefs(getMovieDetail),
            ...toRefs(pageParams),  // 拆解对象
            ...toRefs(tableData),
            ...toRefs(movieList),  // 拆解对象
        }
    },
        //~~ TODO 添加 电影，并写入数据库，自增id /
        // TODO  flask 创建 目录
        // TODO 添加 电影， 点击 下载字幕


};
</script>



<style lang="scss" scoped>
.toggle {
    color: #fff;
    background-color: #007bff;
    border-color: #007bff;
}
// .text-center {
//     text-align:center;
//     // width: 70%;
//     // margin-left:100px;
// }
.movie_check {
    // 固定 图片边栏  https://c.runoob.com/codedemo/5664
    margin-top: 10px;
    // margin-left: 1%;
    // top: 10px;
    // font-weight: bold;
}
.switch {
    // 固定 图片边栏  https://c.runoob.com/codedemo/5664
    margin-top: 10px;
    // margin-left: 1%;
    // top: 10px;
    // font-weight: bold;
}
.title {
    // 固定 图片边栏  https://c.runoob.com/codedemo/5664
    margin-top: 20px;
    margin-bottom: 20px;
    // top: 10px;
    font-weight: bold;
}
.m_info {
  // 文本左对齐
  text-align: left;
   vertical-align: bottom;
}
.my-2 {
  // 文本左对齐
  text-align: right;
}
.my-3 {
  // 文本左对齐
  text-align: left;
  vertical-align: top;
}
</style>
