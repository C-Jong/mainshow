from py2neo import Graph, Node, Relationship,NodeMatcher
import pandas as pd
import csv
# 连接neo4j数据库，输入地址、用户名、密码
graph = Graph("bolt://localhost:7687", username="neo4j", password='123456')
#graph.delete_all() # 清除neo4j中原有的结点等所有信息

with open('C:/neo4j/neo4j-community-3.2.3-windows/neo4j-community-3.2.3/import/names_message.csv', 'r') as f_node:
    reader_node = csv.reader(f_node)
    data_node = list(reader_node)

with open('C:/neo4j/neo4j-community-3.2.3-windows/neo4j-community-3.2.3/import/relation_message.csv', 'r') as f_rel:
    reader_rel = csv.reader(f_rel)
    data_rel = list(reader_rel)

matcher = NodeMatcher(graph)
node = matcher.match('names',name = 'tonys').first()
node1 = Node("names",name = "jong")
print(node)
print(node1)