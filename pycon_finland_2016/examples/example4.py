def noop(*args, **kwargs):
    return

obj = cache.objects[obj_id]
group = cache.groups.get(obj.group_id)
child = obj.child_by_id(child_id)
data["group_name"] = getattr(
                     group, "title", None)
data["object_name"] = getattr(
                      child, "prompt", noop)()
