if __name__ == "__main__" :
    places = ["Kedarnath", "Switzerland" , "Germany", "Tirupati", "Amarnath"]
    secalp = []
    print(places)
    print('sorted list without actully changing its order ' + str(sorted(places)))
    print('original order' + str(places))
    print('Sorting list in reverse order without changing the original list ' + str(sorted(places, reverse=True)))
    print('original order' + str(places))
    places.reverse()
    print('reversed list ' + str(places))
    print(secalp)
    for i in places:
        print(i)