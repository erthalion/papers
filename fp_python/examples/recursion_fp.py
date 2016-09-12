def all_childrens(group_ids):
    for g in group_ids:
        yield g.id

        childrens = Model.objects(
            parent_group__in=g.id
        ).values("id")

        for c in all_childrens(childrens):
            yield c

list(all_childrens((root_group,)))
