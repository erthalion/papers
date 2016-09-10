def noop(*args, **kwargs):
    pass

def get_item_data(self, entity_id, test_item_id):
    def common_part():
        data["task_questions"] = process_questions()
        data["task_answer_choices"] = process_choices()
    data = {}
    if entity_id:
        entity = course_cache.entities[self.entity_id]
        group = cache.groups.get(entity.group_id)
        step = entity.step_by_id(self.step_id)
        data['section_name'] = getattr(group, "title", None)
        data['entity_prompt'] = getattr(step, "prompt", noop)()
    if test_item_id:
        # do something with data []
        common_part()
    if entity_id is None and test_item_id is None:
        # do something with data []
        common_part()
    return data
