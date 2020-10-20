import matplotlib.pyplot as plt

def plotdgree_distribution(dgree_distribution_list):
    """
    度的分布图
    """
    plt.plot([i for i in range(len(dgree_distribution_list))],dgree_distribution_list,color='green')
    plt.title('dgree_distribution--Plot')
    plt.savefig('D:/Files/计算机程序设计/现代程序设计技术/作业/第四周作业/dgree_distribution--Plot.jpg')
    plt.show()