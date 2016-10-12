obj = cache.objects[self.obj_id]
if obj.group_id:
    data['group_name'] = cache.groups[
        obj.group_id].title
if self.child_id:
    child = obj.child_by_id(self.child_id)
    if child:
        data["obj_name"] = child.prompt()
    else:
        logger.warning()
