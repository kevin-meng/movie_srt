import service from "../utils/request.js";
// import { rsaEncrypt } from "../utils/rsa.js";



export function GetMovies() {
    return service.request({
        method: 'get',
        url: "/movies",
    })
}


// export function GetMovieSrt() {
//     return service.request({
//         method: 'get',
//         url: postParams.url,
//         data: {
//             key: postParams.url,
//             secretKey: "",
//         },
//     })
// }



// export function GetCates() {
//     return service.request({
//         method: "get",
//         url: "/"
//     });
// };

export function GetInfoPost(postParams) {
    return service.request({
        method: 'post',
        url: postParams.url,
        data: {
            key: postParams.key, // newest 
            secretKey: "",
            data: postParams.data,
            params: postParams.params
                // secretKey: rsaEncrypt(new Date().getTime() + ':' + 'www.baidu.com' + ':' + 'otherinfos') // 预留字段给加密用
        }
    })
}


export function GetImgs(movieSrt, index) {
    return movieSrt[index].img_ls;
}