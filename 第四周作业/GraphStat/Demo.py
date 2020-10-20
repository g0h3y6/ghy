import NetworkBuilder.node as n
import NetworkBuilder.stat as s
import NetworkBuilder.graph as g
import Visualization.plotgraph as plg
import Visualization.plotnodes as pln
import random

def main():
    #NetworkBuilder.node模块测试
    node_list,near_dict=n.init_node()
    print(n.get_item(node_list,'type',random.randint(0,34282)))
    print(n.get_item(node_list,'weight',random.randint(0,34282)))
    n.print_node(node_list,random.randint(0,34282))
    #NetworkBuilder.Stat模块测试
    print('The average degree of the graph is {}'.format(s.cal_average_dgree(near_dict)))
    dgree_distribution_list=s.cal_dgree_distribution(near_dict)
    #NetworkBuilder.graph模块测试
    graph_dict=g.init_graph(node_list,near_dict)
    g.save_graph(graph_dict)
    a=g.load_graph()
    if a==graph_dict:
        print('Transformed successfully!')
    #Visualization.plotgraph模块测试
    plg.plot_nodes_attr(graph_dict,'weight')
    plg.plot_nodes_attr(graph_dict,'type')
    #Visualization.plotnodes模块测试
    pln.plotdgree_distribution(dgree_distribution_list)

if __name__=='__main__':main()