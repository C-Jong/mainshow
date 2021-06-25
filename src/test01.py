from py2neo import Graph, Node, Relationship,NodeMatcher
import pandas as pd
import csv

# 连接neo4j数据库，输入地址、用户名、密码
graph = Graph("bolt://localhost:7687", username="neo4j", password='123456')
matcher = NodeMatcher(graph)

# 清除neo4j中原有的结点等所有信息
graph.delete_all()

with open('C:/neo4j/neo4j-community-3.2.3-windows/neo4j-community-3.2.3/import/names_message.csv', 'r') as f_node:
    reader_node = csv.reader(f_node)
    data_node = list(reader_node)

with open('C:/neo4j/neo4j-community-3.2.3-windows/neo4j-community-3.2.3/import/relation_message.csv', 'r') as f_rel:
    reader_rel = csv.reader(f_rel)
    data_rel = list(reader_rel)

# 添加节点
for i in range(1, len(data_node)):
    node = Node('names', name=data_node[i][0], id=data_node[i][1])
    graph.create(node)

for j in range(1, len(data_rel)):

    # 判断节点是否存在,不存在则创建该节点
    if matcher.match('names',name = data_rel[j][0]) == None:
        node_index = Node('names', name=data_rel[j][0])
        graph.create(node_index)

    if matcher.match('names', name=data_rel[j][1]) == None:
        node_index = Node('names', name=data_rel[j][1])
        graph.create(node_index)


    # 获取neo4j中节点的信息
    node_sub = graph.nodes.match('names', name=data_rel[j][0]).first()
    node_obj = graph.nodes.match('names', name=data_rel[j][1]).first()

    # 创建节点间关系
    rel = Relationship(node_sub, data_rel[j][2], node_obj)
    graph.create(rel)
