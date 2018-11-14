#coding:utf8

_read = "/Users/zhangyongsheng/Downloads/wdjanss.txt"
with open(_read,"r")as f:
    alist = f.readlines()

def menu():
    menunum = []
    menunames = []
    for i in range(len(alist)):
        if alist[i].startswith('第'):    #如果这行是以"第"开头的就为真
            menunum.append(i)           #把"第"字的行数存入列表
            menunames.append(alist[i])  #把内容存入列表
    return menunum,menunames

def contents(menunum):
    contentlist = []
    n = len(menunum)
    for i in range(n):
        try:
            content = ''.join(alist[menunum[i]:menunum[i+1]])   #把menunum[i]（包括这个元素）到menunum[i+1]（不包括这个元素）的行数存到字符串
        except IndexError:
            content = ''.join(alist[menunum[i]:])
        contentlist.append(content)

    return contentlist

if __name__ == '__main__':
    menunum,subjuct = menu()
    c = contents(menunum)
    for i in c:
        print i
    #subjuct是所有的标题，c就是所有的内容，自己插库就行了



