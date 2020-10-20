import matplotlib.pyplot as plt

def plot_nodes_attr(graph_dict,key):
    """
    绘制图中节点属性的统计结果，其他和名称不便于统计，此处仅统计权重和类型
    """
    if key=='weight':
        
        plt.hist([int(graph_dict[i][0]['weight']) for i in range(len(graph_dict))],color='green')
        plt.title('weight distribution--Hist')
        plt.savefig('D:/Files/计算机程序设计/现代程序设计技术/作业/第四周作业/weight distribution--Hist.jpg')
        plt.show()
        
        """
        plt.plot([graph_dict[i][0]['weight'] for i in range(len(graph_dict))],[i for i in range(len(graph_dict))],color='green')
        plt.title('weight distribution--Bar')
        plt.show()
        """
    elif key=='type':
        a=set([graph_dict[i][0]['type'] for i in range(len(graph_dict))])
        plt.pie([[graph_dict[i][0]['type'] for i in range(len(graph_dict))].count(j) for j in a])
        plt.title('type distribution--Pie')
        plt.savefig('D:/Files/计算机程序设计/现代程序设计技术/作业/第四周作业/type distribution--Pie.jpg')
        plt.show()
    else:
        print('Can not give a plot for this item!')