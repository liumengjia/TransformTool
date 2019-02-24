# -*- coding: UTF-8 -*-
import wx
import BaseTools
import hashlib
import random
import requests


q = None
appid = "zzz"
SecretKey = "zzz"
salt = str(random.random())
q = None


class MianWindow(BaseTools.Frame):
    # 首先，咱们从刚刚源文件中将主窗体继承下来.就是修改过name属性的主窗体咯。
    def BtnTranWord(self, event):
        # 1.定义翻译单词函数
        def WordFanyi():
            def SignMake(q):
                # 创建index字符串
                index = appid + q + salt + SecretKey
                # 对index进行md5加密
                Md5 = hashlib.md5()
                Md5.update(index.encode("utf-8"))
                str = Md5.hexdigest()
                return str

            q = str(self.CommonInput.GetValue())
            if (q.strip() == ""):
                self.ResultInput.SetValue("请在第一个输入框输入您需要转化的字符.....")
            else:
                BaiDuFanYi = {'q': q, 'from': 'auto', 'to': 'auto', 'appid': appid, 'salt': salt, 'sign': SignMake(q)}
                try:
                    self.ResultInput.SetValue("")
                    BaiDuFanYi = requests.get("http://api.fanyi.baidu.com/api/trans/vip/translate", params=BaiDuFanYi)
                    try:
                        for i in range(0, len(BaiDuFanYi.json()["trans_result"])):  # 处理输入的翻译字符是多行的
                            # 追加到末尾 但是不换行ApppendText
                            self.ResultInput.AppendText(BaiDuFanYi.json()["trans_result"][i]["dst"] + "\n")
                        CommonInputline = str(self.ResultInput.GetNumberOfLines() - 1)  # 默认会有一个回车行，需要减掉
                        self.staticTexttitleView.SetLabel("翻译如下，合计:\"" + CommonInputline + "\"行，感谢您的使用...")

                    except Exception as xx:
                        self.ResultInput.SetValue(
                            BaiDuFanYi.json()["error_msg"] + "错误码：" + BaiDuFanYi.json()["error_code"])
                except Exception as EX:
                    self.ResultInput.SetValue("请求失败...检查电脑网络是否通畅")

        # 2.定义cookie格式转Dict
        def CookieTranDict():
            strcookie = str(self.CommonInput.GetValue())
            strlen = len(strcookie.split(";"))
            if (strlen == 1):
                self.ResultInput.SetValue("非Cookie格式，请重新输入....")
            else:
                DictNum1List = []
                DictNum2List = []
                DictBody = {}
                for i in range(0, strlen):
                    try:
                        DictNum1 = strcookie.split(";")[i].strip().split("=")[0]
                        DictNum2 = strcookie.split(";")[i].strip().split("=")[1]
                        DictNum1List.append(DictNum1)
                        DictNum2List.append(DictNum2)

                        for x in range(0, len(DictNum1List)):
                            DictBody[DictNum1List[x]] = DictNum2List[x]
                        DictStrRaw = ""
                        DictStr = ""
                        for key in DictBody.keys():
                            values = (key, DictBody[key])
                            DictStrRaw = DictStrRaw + "," + "'%s'" ':' "'%s'" % (values)
                        DictStr = "{" + DictStrRaw[1:] + "}"
                        self.staticTexttitleView.SetLabel("cookie格式转化Dict完成，请直接copy进行使用")
                        self.ResultInput.SetValue(DictStr)

                    except Exception as Ex:
                        self.ResultInput.SetValue("非Cookie格式，请重新输入....")

        # 3.定义url格式转换成dict
        def UrlTranDict():
            strcookie = str(self.CommonInput.GetValue())
            strlen = len(strcookie.split("&"))
            if (strlen == 1):
                self.ResultInput.SetValue("非Url参数格式，请重新输入....")
            else:
                DictNum1List = []
                DictNum2List = []
                DictBody = {}
                for i in range(0, strlen):
                    try:
                        DictNum1 = strcookie.split("&")[i].strip().split("=")[0]
                        DictNum2 = strcookie.split("&")[i].strip().split("=")[1]
                        DictNum1List.append(DictNum1)
                        DictNum2List.append(DictNum2)

                        for x in range(0, len(DictNum1List)):
                            DictBody[DictNum1List[x]] = DictNum2List[x]
                        DictStrRaw = ""
                        DictStr = ""
                        # 将字典拼接成Str
                        for key in DictBody.keys():
                            values = (key, DictBody[key])
                            DictStrRaw = DictStrRaw + "," + "'%s'" ':' "'%s'" % (values)
                        DictStr = "{" + DictStrRaw[1:] + "}"
                        self.ResultInput.SetValue(DictStr)
                        self.staticTexttitleView.SetLabel("URL格式转化Dict完成，请直接copy进行使用")

                    except Exception as Ex:
                        self.ResultInput.SetValue("非URl参数格式，请重新输入....")

        def generateheaderdict():
            headersstr = str(self.CommonInput.GetValue())
            headerdicts = {}
            try:
                headerslist = headersstr.split("\n")
                for i in range(len(headerslist)):
                    headers = headerslist[i].split(": ")
                    headerdicts[headers[0].replace(" ", "")] = headers[1].replace(" ", "")
                self.ResultInput.SetValue(format(headerdicts))
                self.staticTexttitleView.SetLabel("header格式转化Dict完成，请直接copy进行使用")
            except Exception as ex:
                self.ResultInput.SetValue("无法识别的格式....")

        # 根据输入的字符串格式来调用不同的方法
        strword = str(self.CommonInput.GetValue())
        douhao = ";"
        dengyu = "="
        yufuhao = "&"
        huanxingfu = "\n"
        maohao = ":"
        if douhao in strword and dengyu in strword and maohao not in strword:
            CookieTranDict()
        elif yufuhao in strword and dengyu in strword:
            UrlTranDict()
        elif huanxingfu in strword and maohao in strword:
            generateheaderdict()
        else:
            WordFanyi()


if __name__ == '__main__':
    app = wx.App()
    main_win = MianWindow(None)
    main_win.Show()
    app.MainLoop()
