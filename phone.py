
#判断
class Judge:
    '''判断电话和姓名的合法性'''

    zj_lst2 = []
    dic = {}
    new_dic = {}
    #判断姓名
    def jg_name(self):
        self.name = input('输入姓名')
        if len(self.name) < 12 and self.name != '':
            return
        else:
            print('姓名不能长于12位数，或不能为空')
            self.jg_name()
        return self.name            
    #判断电话    
    def jg_phone(self):
        while 1:
            b = 1
            self.phone = input('输入电话号码')

            if len(self.phone) != 11:
                print('电话位数不正确，请重新输入11位电话号码')
                b = 0
            elif self.phone[0] != '1':
                print('电话的第一位数字不对,请从新输入')
                b = 0
            if b:
                for i in self.phone: 
                    if not i.isdigit():
                        print('电话号格式不对，请输入正确电话号码')
                        b = 0
                        break
            if b:
                return self.phone
                

    #电话备注增加
    def book_add(self):
        nu = input('是否增加电话备注，是请按1加回车键，否请按回车键')
        if nu == '1':
            books = input('请输入备注')
            for k,y in self.dic.items():
                if self.phone in self.dic.keys():
                    self.new_dic.update({k:books})
            print('备注增加成功')



    #电话备注增加或修改           
    def book_can(self):
        self.jg_name()
        if self.name in self.dic.values():
            nun = list(self.dic.values()).count(self.name)
        else:
            print('没有要修改的号码')
            return
        
        if nun == 1:
            bz = input('请输入新的备注')
            for k,y in self.dic.items():
                if y == self.name:
                    self.new_dic[k] = bz
            print('修改成功')
        else:    
            lst = []
            lst2 = []
            nb = 1
            for k,y in self.dic.items():
                if y == self.name:
                    lst.append({nb:{y:k}})
                    lst2.append(k)
                    nb += 1
            print(lst)
            xh = input('选择要修改的序号进行修改')
            xh = int(xh)-1
            bz = input('请输入新的备注')
            self.new_dic[lst2[xh]] = bz
            print('修改成功')


       
            
#电话的查找
class Find(Judge):
    '''电话的查找'''
    ##电话查找
    def phone_find(self):
        phone = input('请输入手机号')
        for i in phone:
            if not i.isdigit():
                print('电话号格式不对，请重新输入正确电话号码')
                self.phone_find()
        nun = []
        for i in self.dic.keys():
            if i.find(phone) != -1:
                nun.append(i)
            else:
                print('没有找到匹配的手机号')
                return
            
        for k,y in self.dic.items():
            if k in nun:
                nun.insert(nun.index(k),y)
        if nun:
            print(nun)
        else:
            print('没有找到匹配的手机号')
                    
    #姓名查找
    def name_find(self):
        self.jg_name()
        nun = []
        for i in self.dic.values():
            if i.find(self.name) != -1:
                nun.append(i)
            else:
                print('没有找到匹配的姓名')
                
        for k,y in self.dic.items():
            if y in nun:
                nun.insert(nun.index(y)+1,k)
        if nun:
            print(nun)
        else:
            print('没有找到匹配的手机号')


            
    #电话本被反向打印
    def find(self):
        dic = self.dic.copy()
        for k,y in dic.items():
            if not self.new_dic.items():
                 print(y,':',k)
            else:
                for i,f in self.new_dic.items():
                    if i == k:
                        print(y,':',k,'备注',f)
                        break
                    else:
                        print(y,':',k)
                        break
                    
            

#分组实现
class Gp:
    gp = {'朋友':[]}
     #分组名的添加
    def fz_gpg(self):
        name = input('请添加分组名称')
        if name not in self.gp.keys():
            self.gp.setdefault(name,[])
            print(self.gp)
        else:
            print('分组名已存在，请从新命名')
            self.fz_gpg()

    #分组名的修改
    def fz_xg(self):
        zj_lst = []
        nun = 1
        for i in self.gp.keys():
            zj_lst.append(i)
            print(nun,i)
            nun += 1
        fz = int(input('选择你想更改的分组名'))
        val = self.gp[zj_lst[fz - 1]]
        self.gp.pop(zj_lst[fz - 1])
        while 1:            
            name = input('请输入新的分组名称')
            if name != ' ':
                if name not in self.gp.keys():
                    self.gp[name] = val
                    print('分组命名成功')
                    break
                else:
                    print('分组名已存在，请从新命名')
            else:
                print('分组名不能为空')

    #分组的添加电话
    def fz_zj(self):
        zj_lst = []
        nun = 1
        for i in self.gp.keys():
            zj_lst.append(i)
            print(nun,i)
            nun += 1
        
        fz = int(input('选择你想加入的分组'))
        self.gp[zj_lst[fz - 1]].append({self.phone:self.name})
        print('电话分组成功')

    #分组电话的显示
    def fz_dy(self):
        nae = 1    
        for i in self.gp.keys():
            print(nae,i)
            nae += 1
        nun = int(input('请输入分组的序号'))
        noe = list(self.gp.keys())[nun-1]
        for i in self.gp[noe]:
            for j,k in i.items():
                print(k,j)

                
    #分组的删除电话            
    def fz_sc(self):
        nae = 1
        lst = []
        we = 1
        for i in self.gp.keys():
        
            print(nae,i)
            nae += 1
        nun = int(input('请输入分组的序号'))
        noe = (list(self.gp.keys()))[nun-1]
        
        for i in self.gp[noe]:
            for j,k in i.items():
                lst.append(j)
                print(we,k,j)
                we += 1
        ue = int(input('请选择删除号码的序号'))
        self.gp[noe].pop(ue-1)
        print('电话删除成功')

        
        
    

    
#电话的增改删
class Phone(Judge,Gp):
    '''电话的增改删'''

    def wy(self):
        self.jg_name()
        self.jg_phone()
        self.fz_zj()
 
    #增加电话号码  
    def add(self):
        self.jg_name()
        self.jg_phone()
        if self.phone not in self.dic.keys():
            self.dic[self.phone] = self.name
            print('保存成功')
            self.book_add()
            da = input('是否增添到分组中，是请回车键，否则请按1和回车键')
            if not da:
                self.fz_zj()
            
        else:
            print('电话号码已经存过，请重新输入')
            self.add()


    #修改电话号码       
    def mod(self):
        self.jg_name()
        if self.name in self.dic.values():
            nun = list(self.dic.values()).count(self.name)
        else:
            print('没有要修改的号码')
            return
        
        if nun == 1:
            self.jg_phone()
            for k,y in self.dic.items():
                if y == self.name:
                    self.dic.pop(k)
                    break
            self.dic[self.phone] = self.name
            
            print('修改成功')
            return
                    
        else:
           
            lst = []
            lst2 = []
            nb = 1
            for k,y in self.dic.items():
                if y == self.name:
                    lst.append({nb:{y:k}})
                    lst2.append(k)
                    nb += 1
            print(lst)
            xh = input('选择要修改的序号进行修改')
            xh = int(xh)-1
            self.dic.pop(lst2[xh])
            self.jg_phone()
            self.dic[self.phone] = self.name
            print('修改成功')
            
        
            
    #移除电话号码   
    def remove(self):
        self.jg_name()
        if self.name in self.dic.values():
            nun = list(self.dic.values()).count(self.name)
        else:
            print('没有删除的号码')
            return
        if nun == 1:
            for k,y in self.dic.items():
                if y == self.name:
                    self.dic.pop(k)
                    print('删除成功')
                    break
        else:
            lst = []
            lst2 = []
            nb = 1
            for k,y in self.dic.items():
                if y == self.name:
                    lst.append({nb:{y:k}})
                    lst2.append(k)
                    nb += 1
            print(lst)
            xh = input('选择要删除的序号进行删除')
            xh = int(xh)-1
            self.dic.pop(lst2[xh])
            print('删除成功')
            
        
        
    #提示语句
    def jg(self):
        num = input('继续当前操作请安1和回车键，退出当前操作请按回车键')
        if num != '1':
            return 1
        
    
while 1:
    num = input('''输入数字 1：增加 2：修改 3：删除 4：查找 5：修改备注
                6：显示全部 7: 分组增改修查 8：结束''')
    if num == '1':
        while 1:
            print('增加')
            Phone().add()
            if Phone().jg():
                break
            
            da = input('是否增添到分组中，是请回车键，否则请按1和回车键')
            if not da:
                Phone().fz_zj()
            

            
    if num == '2':
        while 1:
            print('修改')
            Phone().mod()
            if Phone().jg():
                break
            
    if num == '3':
        while 1:
            print('删除')
            Phone().remove()
            if Phone().jg():
                break
            
    if num == '4':
        while 1:
            nas = input('电话查找请按1！姓名超找请安2！')
            if nas == '1':
                Find().phone_find()
                if Phone().jg():
                    break
            elif nas == '2':
                Find().name_find()
                if Phone().jg():
                    break

    if num == '5':
        while 1:
            print('修改备注')
            Judge().book_can()
            if Phone().jg():
                break
           
    if num == '6':
        Find().find()

    if num == '7':
        while 1:
            fs = input('''输入对应的序号，1：增加分组名  2：修改分组名
                     3：分组电话添加 4: 分组删除单词  5：显示分组信息
                     6：退出''')
            if fs == '1':
                while 1:
                    Phone().fz_gpg()
                    if Phone().jg():
                        break
                    
            if fs == '2':
                while 1:
                    Phone().fz_xg()
                    if Phone().jg():
                        break
                   
            if fs == '3':
                while 1:
                    Phone().wy()
                    
                    if Phone().jg():
                        break
                  
            if fs == '4':
                while 1:
                    Phone().fz_sc()
                    if Phone().jg():
                        break
            if fs == '5':
                while 1:
                    Phone().fz_dy()
                    if Phone().jg():
                        break
                    
            if fs == '6':
                break
             
    if num == '8':
        break







    






































































































































