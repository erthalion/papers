# save source of data in partial
from functools import partial

process_with_source = partial(process_data,
                              data_source)
process_with_source()

# currying
process_data = curry(process_data)
initialized = process_data(data_source)(first_arg)
