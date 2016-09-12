def all_childrens(group_id):
    current_children_ids = Model.objects(
        parent_group=group_id
    ).values("id")

    result = [group_id]

    while current_children_ids:
        result.extend(current_children_ids)
        current_children_ids = Model.objects(
            parent_id__in=current_children_ids
        ).values("id")
        current_children_ids = list(current_children_ids)

    return result
