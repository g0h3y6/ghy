def cal_average_dgree(near_dict):
    """
    计算网络中的平均度
    """
    sum_dgree=0
    for i in near_dict:
        sum_dgree+=len(near_dict[i])
    
    return sum_dgree/len(near_dict)


def _get_attr_distribution(near_dict,num=0):
    """
    获取某个节点的度分布
    """
    return len(near_dict[num])

def cal_dgree_distribution(near_dict):
    """
    计算网络的度分布，返回一个列表，依节点次排布度
    """
    dgree_distribution_list=[_get_attr_distribution(near_dict,i) for i in range(len(near_dict))]
    return dgree_distribution_list