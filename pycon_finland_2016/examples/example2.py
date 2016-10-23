def get_data(self, obj_id, item_id):
    def common_part():
        data["questions"] = process_questions()
        data["answers"] = process_choices()
    data = {}
    if obj_id:
        # do something with data[]
    if item_id:
        # do something with data[]
        common_part()
    if obj_id is None and item_id is None:
        # do something with data[]
        common_part()
    return data
