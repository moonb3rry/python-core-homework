def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    categories = []
    for categoryId in mapping["categoryIdsSorted"]:
        id = "category-" + categoryId
        text = mapping["categories"][categoryId]["name"]
        items = [{"id": i, "text": mapping["roles"][i]["name"]} for i in mapping["categories"][categoryId]["roleIds"]]
        element = {"id": id, "text": text, "items": items}
        categories.append(element)
    categoriesTree = {'categories': categories}
    return categoriesTree
