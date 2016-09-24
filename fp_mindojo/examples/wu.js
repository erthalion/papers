function* fibs() {
  let a = 0;
  let b = 1;
  while (true) {
    yield a;
    [a, b] = [b, a + b];
  }
}
const isEven      = n => n % 2 == 0;
const lessThanTen = n => n < 10;
wu(fibs())
  .filter(isEven)
  .takeWhile(lessThanTen)
  .forEach(console.log.bind(console));
