import pickle as pe

def init_graph(node_list,near_dict):
    """
    返回一个字典，分别存储节点信息和边信息
    """
    graph_dict={}
    for i in range(len(node_list)):
        graph_dict[i]=(node_list[i],near_dict[i])
    return graph_dict

def save_graph(graph_dict,save_location=r"D:/Files/计算机程序设计/现代程序设计技术/作业/第四周作业/graph_dict.txt"):
    """
    序列化图信息
    """
    with open(save_location,'wb') as w:
        pe.dump(graph_dict,w)

def load_graph(load_location=r"D:/Files/计算机程序设计/现代程序设计技术/作业/第四周作业/graph_dict.txt"):
    """
    反序列化图信息
    """
    with open(load_location,'rb') as r:
        graph_dict=pe.load(r)

    return graph_dict