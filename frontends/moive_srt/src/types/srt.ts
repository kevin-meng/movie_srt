// 暴露数据接口， 限制接口形式
export interface Srt{
    id: number,
    content: string,
    start: number,
    end: number,
    img_ls: Array<string>,
    img_start: string,
    modify: boolean,
    select1: boolean,
    select2: boolean,
}