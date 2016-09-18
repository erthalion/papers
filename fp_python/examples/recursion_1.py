def all_childrens(node_id):
    current_children_ids = Node.objects(
        parent=node_id
    ).values("id")

    result = [node_id]
    for child in current_children_ids:
        result.extend(all_childrens(child))

    return result
