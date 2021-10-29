def flat_list(list_):
    arr = []
    def flatter(sublist):
        try:
            for item in sublist:
                if(type(item) is str):
                    arr.append(item)
                else:
                    flatter(item)
        except TypeError:
            arr.append(sublist)
    flatter(list_)

    return arr
