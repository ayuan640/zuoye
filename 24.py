#24、字典根据键从小到大排序

dic={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
lis=sorted(dic.items(),key=lambda i:i[0],reverse=False)
print(lis)
print(dict(lis))