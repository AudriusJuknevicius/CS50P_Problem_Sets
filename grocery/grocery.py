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
                sorted(item_dic)
                print("{item_dic}: {}".format(item_dic[item]))
             except KeyError:
                  break
             else:
                  pass

main()







