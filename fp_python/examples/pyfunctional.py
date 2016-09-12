from functional import seq


(seq(1, 2, 3, 4)
    .map(lambda x: x * 2)
    .filter(lambda x: x > 4)
    .reduce(lambda x, y: x + y))
