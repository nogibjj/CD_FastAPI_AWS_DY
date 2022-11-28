import requests
from bs4 import BeautifulSoup
import json


topic = {
    "全部" : "https://v1.jinrishici.com/all",
    "抒情" : "https://v1.jinrishici.com/shuqing",
    "四季" : "https://v1.jinrishici.com/siji",
    "山水" : "https://v1.jinrishici.com/shanshui",
    "天气" : "https://v1.jinrishici.com/tianqi",
    "人物" : "https://v1.jinrishici.com/renwu",
    "人生" : "https://v1.jinrishici.com/rensheng",
    "生活" : "https://v1.jinrishici.com/shenghuo",
    "节日" : "https://v1.jinrishici.com/jieri",
    "动物" : "https://v1.jinrishici.com/dongwu",
    "植物" : "https://v1.jinrishici.com/zhiwu",
    "食物" : "https://v1.jinrishici.com/shiwu",
    "抒情-爱情" : "https://v1.jinrishici.com/shuqing/aiqing",
    "抒情-友情" : "https://v1.jinrishici.com/shuqing/youqing",
    "抒情-离别" : "https://v1.jinrishici.com/shuqing/libie",
    "抒情-思念" : "https://v1.jinrishici.com/shuqing/sinian",
    "抒情-思乡" : "https://v1.jinrishici.com/shuqing/sixiang",
    "抒情-伤感" : "https://v1.jinrishici.com/shuqing/shanggan",
    "抒情-孤独" : "https://v1.jinrishici.com/shuqing/gudu",
    "抒情-闺怨" : "https://v1.jinrishici.com/shuqing/guiyuan",
    "抒情-悼亡" : "https://v1.jinrishici.com/shuqing/daowang",
    "抒情-怀古" : "https://v1.jinrishici.com/shuqing/huaigu",
    "抒情-爱国" : "https://v1.jinrishici.com/shuqing/aiguo",
    "抒情-感恩" : "https://v1.jinrishici.com/shuqing/ganen",
    "四季-春天" : "https://v1.jinrishici.com/siji/chuntian",
    "四季-夏天" : "https://v1.jinrishici.com/siji/xiatian",
    "四季-秋天" : "https://v1.jinrishici.com/siji/qiutian",
    "四季-冬天" : "https://v1.jinrishici.com/siji/dongtian",
    "山水-庐山" : "https://v1.jinrishici.com/shanshui/lushan",
    "山水-泰山" : "https://v1.jinrishici.com/shanshui/taishan",
    "山水-江河" : "https://v1.jinrishici.com/shanshui/jianghe",
    "山水-长江" : "https://v1.jinrishici.com/shanshui/changjiang",
    "山水-黄河" : "https://v1.jinrishici.com/shanshui/huanghe",
    "山水-西湖" : "https://v1.jinrishici.com/shanshui/xihu",
    "山水-瀑布" : "https://v1.jinrishici.com/shanshui/pubu",
    "天气-写风" : "https://v1.jinrishici.com/tianqi/xiefeng",
    "天气-写云" : "https://v1.jinrishici.com/tianqi/xieyun",
    "天气-写雨" : "https://v1.jinrishici.com/tianqi/xieyu",
    "天气-写雪" : "https://v1.jinrishici.com/tianqi/xiexue",
    "天气-彩虹" : "https://v1.jinrishici.com/tianqi/caihong",
    "天气-太阳" : "https://v1.jinrishici.com/tianqi/taiyang",
    "天气-月亮" : "https://v1.jinrishici.com/tianqi/yueliang",
    "天气-星星" : "https://v1.jinrishici.com/tianqi/xingxing",
    "人物-女子" : "https://v1.jinrishici.com/renwu/nvzi",
    "人物-父亲" : "https://v1.jinrishici.com/renwu/fuqin",
    "人物-母亲" : "https://v1.jinrishici.com/renwu/muqin",
    "人物-老师" : "https://v1.jinrishici.com/renwu/laoshi",
    "人物-儿童" : "https://v1.jinrishici.com/renwu/ertong",
    "人生-励志" : "https://v1.jinrishici.com/rensheng/lizhi",
    "人生-哲理" : "https://v1.jinrishici.com/rensheng/zheli",
    "人生-青春" : "https://v1.jinrishici.com/rensheng/qingchun",
    "人生-时光" : "https://v1.jinrishici.com/rensheng/shiguang",
    "人生-梦想" : "https://v1.jinrishici.com/rensheng/mengxiang",
    "人生-读书" : "https://v1.jinrishici.com/rensheng/dushu",
    "人生-战争" : "https://v1.jinrishici.com/rensheng/zhanzheng",
    "生活-乡村" : "https://v1.jinrishici.com/shenghuo/xiangcun",
    "生活-田园" : "https://v1.jinrishici.com/shenghuo/tianyuan",
    "生活-边塞" : "https://v1.jinrishici.com/shenghuo/biansai",
    "生活-写桥" : "https://v1.jinrishici.com/shenghuo/xieqiao",
    "节日-春节" : "https://v1.jinrishici.com/jieri/chunjie",
    "节日-元宵节" : "https://v1.jinrishici.com/jieri/yuanxiaojie",
    "节日-寒食节" : "https://v1.jinrishici.com/jieri/hanshijie",
    "节日-清明节" : "https://v1.jinrishici.com/jieri/qingmingjie",
    "节日-端午节" : "https://v1.jinrishici.com/jieri/duanwujie",
    "节日-七夕节" : "https://v1.jinrishici.com/jieri/qixijie",
    "节日-中秋节" : "https://v1.jinrishici.com/jieri/zhongqiujie",
    "节日-重阳节" : "https://v1.jinrishici.com/jieri/chongyangjie",
    "动物-写鸟" : "https://v1.jinrishici.com/dongwu/xieniao",
    "动物-写马" : "https://v1.jinrishici.com/dongwu/xiema",
    "动物-写猫" : "https://v1.jinrishici.com/dongwu/xiemao",
    "植物-梅花" : "https://v1.jinrishici.com/zhiwu/meihua",
    "植物-梨花" : "https://v1.jinrishici.com/zhiwu/lihua",
    "植物-桃花" : "https://v1.jinrishici.com/zhiwu/taohua",
    "植物-荷花" : "https://v1.jinrishici.com/zhiwu/hehua",
    "植物-菊花" : "https://v1.jinrishici.com/zhiwu/juhua",
    "植物-柳树" : "https://v1.jinrishici.com/zhiwu/liushu",
    "植物-叶子" : "https://v1.jinrishici.com/zhiwu/yezi",
    "植物-竹子" : "https://v1.jinrishici.com/zhiwu/zhuzi",
    "食物-写酒" : "https://v1.jinrishici.com/shiwu/xiejiu",
    "食物-写茶" : "https://v1.jinrishici.com/shiwu/xiecha",
    "食物-荔枝" : "https://v1.jinrishici.com/shiwu/lizhi"
}

def poemgen(category="全部"):
# Fetch the web page
    # set the url as topic's value
    if category in topic:
        url = topic[category]
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        data = json.loads(soup.text)
        return data
    else:
        return "Sorry, the category you entered is not available. Try {topic.keys()}"

if __name__ == "__main__":
    poem = poemgen()
    print(poem)
