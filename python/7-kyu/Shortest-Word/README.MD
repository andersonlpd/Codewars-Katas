Simple, given a string of words, return the length of the shortest word(s).<br><br>

String will never be empty and you do not need to account for different data types.

## Assertions:

test.describe("Basic Tests")<br>
test.assert_equals(find_short("bitcoin take over the world maybe who knows perhaps"), 3)<br>
test.assert_equals(find_short("turns out random test cases are easier than writing out basic ones"), 3)<br>
test.assert_equals(find_short("lets talk about javascript the best language"), 3)<br>
test.assert_equals(find_short("i want to travel the world writing code one day"), 1)<br>
test.assert_equals(find_short("Lets all go on holiday somewhere very cold"), 2)<br>
