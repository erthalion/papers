def all_childrens(node_id):
    current_children_ids = Node.objects(
        parent=node_id
    ).values("id")
    result = [node_id]

    while current_children_ids:
        result.extend(current_children_ids)
        current_children_ids = Node.objects(
            parent__in=current_children_ids
        ).values("id")
        current_children_ids = list(current_children_ids)

    return result
