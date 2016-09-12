# save source of data into class instance
class DataProcessor(object):
    def __init__(self, data_source):
        self.data_source = data_source

    def process_data(self, *args):
        # do some stuff

processor = DataProcessor(data_source)
processor.process_data()

# save source of data in partial
from functools import partial

process_with_source = partial(process_data, data_source)
process_with_source()

# currying
process_data = curry(process_data)
process_with_source = process_data(data_source)
process_with_args = process_with_source(args)
