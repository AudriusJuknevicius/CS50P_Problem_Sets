def main():

    item_dic = {}

    while True:
             try:
                item = input().upper()
                # item_dic = {item: 0}
                if item in item_dic:
                    item_dic[item] += 1
                else:
                     item_dic[item] = 1
             except KeyError:
                    pass
             except EOFError:
                break

    for item, count in item_dic.items():
        sorted(item_dic)
        print("{} {}".format(count, item))


main()







