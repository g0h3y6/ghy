def init_node(node_file_location=r"D:/Files/计算机程序设计/现代程序设计技术/作业数据/newmovies.txt"):
    """
    输入节点文档所在位置，返回包含节点属性字典的列表，key为节点的属性，值为对应的属性值
    """
    node=['id','name','weight','type','others']
    node_list=[]#存储节点信息字典的列表
    near_dict={}#存储节点邻接表的字典
    with open(node_file_location,'r',encoding='UTF-8') as f:
        lines=f.readlines()
        t_t=0#用于记录*出现的次数，读取到第二个*立刻断开，也能避开对第一个*后内容的读取
        for line in lines:
            if line[0]=='*':
                t_t+=1
                if t_t==1:#根据节点数
                    num=int(line.split(' ')[1].strip())
                    for i in range(num+1):
                        near_dict[i]=[]
                continue
            if t_t==1:
                temp=line.split('\t')
                s_dict={}
                for i in range(5):
                    s_dict[node[i]]=temp[i].strip()
                node_list.append(s_dict)
            if t_t==2:
                temp=line.split('\t')
                near_dict[int(temp[0])].append(temp[1])

    return node_list,near_dict

def _get_attr(node,key):
    """
    获取节点的属性，其中node为字典形式的节点信息
    """
    return node[key]

def get_item(node_list,key,num=0):
    """
    获取对应的节点属性，其中num是节点的序号
    """
    node=node_list[num]
    return _get_attr(node,key)

def print_node(node_list,num=0):
    """
    利用format函数，将节点属性输出至屏幕上，其中num是节点的序号
    """
    print("Node\nid:{},name:{},weight:{},type:{},others:{}".format(*[node_list[num][i] for i in node_list[num]]))

#print(init_node()[1][0])
#print(get_item(init_node()[0],'name',0))