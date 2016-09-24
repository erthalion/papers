var myIterable = {}

myIterable[Symbol.iterator] = function* () {
    for(i=0; i < 5; i++) {
        yield i;
    }
};

[...myIterable] // [0, 1, 2, 3, 4]
