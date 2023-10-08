"""
product
    0: name
    1: manufacturer
    2: cost
    3: number
"""

def linear_search_product(prod_list, name=""):
    ret = []

    for i in range(len(prod_list)):
        if prod_list[i][0].lower() == name.lower():
            ret.append(i)

    return ret

def display_results(prod_list, res_list):
    if res_list == [] :
        print("No products found")
        return

    for i in res_list:
        print(prod_list[i])

def main():
    pl = [
        [ "Pencil",       "Apsara",  20, 30 ],
        [ "Pen",          "Camlin",  20, 30 ],
        [ "Pencil",       "Camlin",  20, 30 ],
        [ "Geometry Box", "Camlin",  20, 30 ],
        [ "Pencil",       "Natraja", 20, 30 ],
        [ "Pen",          "Parker",  20, 30 ],
        [ "Pen",          "Flair",   20, 30 ],
        [ "Geometry Box", "Apsara",  20, 30 ],
        [ "Pencil",       "Apsara",  20, 30 ],
        [ "Pencil",       "Apsara",  20, 30 ],
    ]

    print(pl)
    print("Searching for \"pencil\"")
    display_results(pl, linear_search_product(pl, "pencil"))
    print("Searching for \"pen\"")
    display_results(pl, linear_search_product(pl, "pen"))
    print("Searching for \"notebook\"")
    display_results(pl, linear_search_product(pl, "notebook"))

if __name__ == "__main__":
    main()
