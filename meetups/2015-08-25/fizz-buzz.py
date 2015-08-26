import unittest


fizz_input = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20"
fizz_output = ""

"""Write the code here to transform fizz_output such that:
    1) numbers divisible by 3 are replaced with fizz
    2) numbers divisible by 5 are replaced with buzz
    3) numbers divisbile by both 3 and 5 are replaced by fizz buzz"""

split_string = fizz_input.split(" ")
split_list = []

for number in split_string:
    this_num = int(number)

    mod_three = (this_num % 3 == 0)
    mod_five = (this_num % 5 == 0)

    if mod_three and mod_five:
        split_list.append("fizz buzz")
    elif mod_three:
        split_list.append("fizz")
    elif mod_five:
        split_list.append("buzz")
    else:
        split_list.append(number)

fizz_output = " ".join(split_list)


"""Test Case to validate the solution"""
class TestFizzBuzz(unittest.TestCase):
    def test_fizz_input(self):
        """ This will test that our test case wired up to succeed """
        expected = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20"
        self.assertEqual(expected, fizz_input)

    def test_fizz_output(self):
        expected = " ".join(["1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz",
                "13 14 fizz buzz 16 17 fizz 19 buzz"])
        self.assertEqual(expected, fizz_output)
        self.assertEqual(expected, fizz_output)
