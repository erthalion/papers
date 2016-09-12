from collections import namedtuple

Node = namedtuple('Node', 'id childrens')
root = Node(1,
    (
        Node(2,
            (
                Node(5, ()),
                Node(6, ()),
            )
        ),
        Node(3, ()),
        Node(4, ()),
    )
)

def all_childrens(group_ids):
    for g in group_ids:
        yield g.id

        for c in all_childrens(g.childrens):
            yield c

list(all_childrens((root,)))
