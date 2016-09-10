# NOTES:
# * pattern matching
#       >>> if entity_id:
#           ....
#       >>> if test_item_id:
#       >>> ....
# * Maybe monad
#       >>> getattr(course_cache.groups.get(entity_group_id), "title", None)
#       >>> step = entity.step_by_id(self.step_id)


def get_item_data(self, entity_id, test_item_id):

    def shared_part(task, title, chosen_response_ids):
        snippet = task.snippet or ''
        data['entity_task_title'] = title
        data['task_question'] = process_tags(
            task.root_step.prompt_with_markdown_images(), snippet=snippet)
        data['task_answer_choices'] = self._get_answer_choices(
            task, task.root_step, chosen_response_ids)

    data = {}
    course_cache = self.course.cache

    if entity_id:
        entity = course_cache.entities[self.entity_id]
        entity_group_id = course_cache.arenas_by_entity.get(entity.id)

        data['entity_task_title'] = entity.title
        data['section_name'] = getattr(course_cache.groups.get(entity_group_id),
                                       "title", None)

        # log empty step inside this function
        step = entity.step_by_id(self.step_id)

        summary = entity.summary_with_markdown_images() if entity.summary else ''
        # getattr * exec * process_tags $ step, summary
        # or throw exceptions
        data['entity_prompt'] = process_tags(
            getattr(step, "prompt_with_markdown_images", lambda _: None)(),
            summary=summary)

        # _get_chosen_response_ids * _get_answer_choices $ step, entity
        chosen_response_ids = self._get_chosen_response_ids(
            {'entity_id': self.entity_id}, step)

        data['entity_answer_choices'] = self._get_answer_choices(
            entity, step, chosen_response_ids)

    if test_item_id:
        test_num, section_pos, item_pos = self.course.TestSession.parse_item_id(
            self.test_item_id)
        title = "Simulation exam #{}, Question {}".format(test_num, item_pos + 1)
        test_session, section = get_session_and_section(
            self.course, self.student_id, test_num, section_pos)
        test_item = section.items[item_pos]

        if test_item.task_id != self.task_id:
            logger.warning(
                'Passed task id differs from task id stored in the test session item')

        chosen_response_ids = test_item.response_ids
        task = course_cache.all_tasks[test_item.task_id]
        shared_part(task, title, chosen_response_ids)

    if entity_id is None and test_item_id is None:
        task = course_cache.all_tasks[self.task_id]
        title = task.title
        chosen_response_ids = self._get_chosen_response_ids(
            {'task_id': self.task_id}, task.root_step)

        shared_part(task, title, chosen_response_ids)

    return data
