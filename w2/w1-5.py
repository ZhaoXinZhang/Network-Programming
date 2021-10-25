import xml.etree.ElementTree as et
tree = et.ElementTree(file='menu.xml') # 讀取'menu.xml'，獲取tree物件
root = tree.getroot() # 獲取root物件
#遍歷root物件child子節點列印tag與attrib屬性
for child in root: 
    print(child.tag)
    print('hours:', child.attrib['hours'])
    for grandchild in child: 
        print(grandchild.text,'price:', grandchild.attrib['price'])
    

