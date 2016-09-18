def all_childrens(node_ids):
    for n in node_ids:
        yield n.id

        childrens = Node.objects(
            parent__in=n.id
        ).values("id")

        for c in all_childrens(childrens):
            yield c

list(all_childrens((root_node,)))
