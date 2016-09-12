def get_data(self):
    data = {}
    if self.obj_id:
        obj = cache.objects[self.obj_id]
        if objg.group_id:
            data['group_name'] = cache.groups[obj.group_id].title
        if self.child_id:
            child = obj.child_by_id(self.child_id)
            if child:
                data["obj_name"] = child.prompt()
            else:
                logger.warning()
    else:
        if self.item_id:
            # do something with data[]
        else:
            # do something with data[]
        data["questions"] = process_questions()
        data["answers"] = process_choices()
        # do something
    return data
