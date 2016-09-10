def get_item_data(self):
    data = {}
    if self.entity_id:
        entity = course_cache.entities[self.entity_id]
        if entity.group_id:
            data['section_name'] = cache.groups[entity.group_id].title
        if self.step_id:
            step = entity.step_by_id(self.step_id)
            if step:
                data["entity_prompt"] = step.prompt()
            else:
                logger.warning()
    else:
        if self.test_item_id:
            # do something with data[]
        else:
            # do something with data[]
        data["task_questions"] = process_questions()
        data["task_answer_choices"] = process_choices()
        # do something
    return data
