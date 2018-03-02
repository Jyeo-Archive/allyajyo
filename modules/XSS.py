import sys
'''
XSS Gadget maker
입력받은 파일의 스크립트를 우회해 XSS 공격을 할 수 있도록 가젯을 따주는(?) 모듈
현재 개발중인데 현타옴...
'''
def GadgetMaker():
    filename=input("script filename : ")
    f=open(filename, 'r')
    newscript=""
    '''
    input : (PresentationConnectionAvailableEvent+[])
    output : "function PresentationConnectionAvailableEvent() { [native code] }"

    '''
    dictionary=dict()
    dictionary['a']='(!1+[])[1]' #(!1+[]) -> "false"
    dictionary['b']='(typeof(1))[3]' #(typeof(1)) -> "number"
    dictionary['c']='(alert+[])[3]' #(alert+[]) -> "function alert() { [native code] }"
    dictionary['d']='([][0]+[])[2]' #([][0]+[]) -> "undefined"
    dictionary['e']='(!!1+[])[3]' #(!!1+[]) -> "true"
    dictionary['f']='(alert+[])[0]'
    dictionary['g']='(Range+[])[12]' #(Range+[]) -> "function Range() { [native code] }"
    dictionary['h']='(fetch+[])[13]' #(fetch+[]) -> "function fetch() { [native code] }"
    dictionary['i']='([][0]+[])[5]'
    dictionary['j']='(Object+[])[11]' #(Object+[]) -> "function Object() { [native code] }"
    dictionary['k']='(keys+[])[9]' #(keys+[]) -> "function keys(object) { [Command Line API] }"
    dictionary['l']='(!1+[])[2]'
    dictionary['o']=''
    for i in f.readlines():
        for j in i:
            newscript+=dictionary[]
