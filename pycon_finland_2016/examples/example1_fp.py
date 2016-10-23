def noop(*args, **kwargs):
    pass

def get_data(self, obj_id, item_id, child_id):
    def common_part():
        data["questions"] = process_questions()
        data["answers"] = process_choices()
    data = {}
    if obj_id:
        obj = cache.objects[obj_id]
        group = cache.groups.get(obj.group_id)
        child = obj.child_by_id(child_id)
        data["group_name"] = getattr(group, "title", None)
        data["object_name"] = getattr(child, "prompt", noop)()
    if item_id:
        # do something with data []
        common_part()
    if obj_id is None and item_id is None:
        # do something with data []
        common_part()
    return data
