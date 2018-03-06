from Classes.inventory import Item


def item_function(item):
    if item.cat == "potion":
        return item.get_val()
    elif item.cat == "poison":
        return item.get_val()
    elif item.cat == "scroll":
        return item.get_val()
