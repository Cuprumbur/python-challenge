def Translate(myStrParam):
        destStr =""
        for symbol in myStrParam:
                if (symbol != " "):
                        index = ord(symbol)+ 2
                        if (index < 97):
                                destStr += chr(index-2)
                        elif (index > 122):
                                destStr += chr(97 + index - 123)
                        else:
                                destStr += chr(index)
                        
                else:
                        destStr += symbol
        return destStr

myStr = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print(Translate("map"))
print(Translate(myStr))
#next level
#http://www.pythonchallenge.com/pcc/def/ocr.html.

