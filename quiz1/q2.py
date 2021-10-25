import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml') # 解析xml檔，回傳ElementTree物件。
root = tree.getroot() #獲得根節點
a=0
b=0
c=0
for child in root:
    print(child.tag,":", child.attrib['name'])

    
    print("rank:"+root[a][0].text)
    print("year:"+root[a][1].text)
    print("gdppc:"+root[a][2].text,)
    a=a+1  
        # print(child.iter('neighbor'))
    for neighbor in child.iter('neighbor'):
        print('neighbor name:',neighbor.attrib['name'],)
    print('\n')


# import xml.etree.ElementTree as et
# tree = et.ElementTree(file='country_data.xml') # 讀取'menu.xml'，獲取tree物件
# root = tree.getroot() # 獲取root物件
# #遍歷root物件child子節點列印tag與attrib屬性
# for child in root: 
#     # print(child.tag)
#     print('country name::', child.attrib['name'])
#     for grandchild in child: 
#         print('rank:', grandchild.text)
#         # print('rank:', grandchild.text[])

# import xml.etree.ElementTree as ET
# tree = ET.parse('country_data.xml') # 解析xml檔，回傳ElementTree物件。
# root = tree.getroot() #獲得根節點
# i=0
# for child in root:
#     print(child.tag,":", child.attrib['name'])
# for grandchild in child: 
#         print('rank:', grandchild.text)
#     for j in range(3):
#         print("rank:"+root[j][0].text)
#         print("year:"+root[j][1].text)
#         print("gdppc:"+root[j][2].text,)
        
#         # print(child.iter('neighbor'))
#         for neighbor in child.iter('neighbor'):
#             print('neighbor name:',neighbor.attrib['name'],)
#         print('\n')