from search import *
from extract import *

if __name__ == '__main__':
    infoRetrie = InfoRetrie()
    infoExtract = infoExtract(infoRetrie.data_dict)
    while True:
        print("请选择模式：信息检索（IR） 或者 信息抽取（IE）:")
        mode_input = input()

        while mode_input == "IE":
            print("请从以下选择信息抽取类型：")
            print("1. 胜利信息，关键字：Win")
            print("2. 失败信息，关键字：Defeat")
            print("3. 主席/总统信息，关键字：President")
            print("4. 加入信息，关键字：Join")
            print("5. 部分人与部分组织信息，关键字：Of")
            print("输入其他返回上一级")
            type_input = input()
            if type_input == '1':
                infoExtract.findWin()
            elif type_input == '2':
                infoExtract.findDefeat()
            elif type_input == '3':
                infoExtract.findPresident()
            elif type_input == '4':
                infoExtract.findJoin()
            elif type_input == '5':
                infoExtract.findOF()
            else:
                mode_input = ''
                break
            print("**********\n对结果是否满意?\n是的话请输入评分（0-10）")
            print(
                "**********\n输入 n 继续\n输入 q 退出\n**********")
            usr_input = input()
            rating = int(usr_input) if usr_input.isdigit() else 10
            if usr_input == 'q':
                mode_input = ''
                break
            else:
                print("本次检索准确度评价：", rating, "/10")
                continue

        while mode_input == 'IR':
            print("搜索 (输入 q 返回上一级): ", end="")
            search_str = input()
            if search_str == 'q':
                mode_input = ''
                break
            count = 0
            rating = 0
            result = infoRetrie.do_search(search_str)
            if len(result) == 0:
                print("没有符合内容！\n")
                continue
            for i in result:
                i.output()
                count += 1
                print("**********\n对结果是否满意?\n是的话请输入Y，否则输入N")
                print(
                    "**********\n输入 n 继续\n输入 d 重新搜索\n输入 q 退出\n**********")
                usr_input = input()
                rating = rating if usr_input == 'N' else rating + 1
                if usr_input == 'd':
                    break
                elif usr_input == 'q':
                    rating = rating * 100.0 / count
                    print("本次检索准确度评价：", rating)
                    mode_input = ''
                    break
                else:
                    continue
            rating = rating * 100.0 / count
            print("本次检索准确度评价：", rating)
        if mode_input == 'q':
            print('Exiting...')
            exit(0)

