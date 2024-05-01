def main():

    item_dic = {}

    while True:
             try:
                item = input().upper()
                item_dic = {item: 0}
                if item in item_dic:
                    item = item [+1]
             except EOFError:
                    print(item_dic)
                    break
             else:
                    pass


main()







