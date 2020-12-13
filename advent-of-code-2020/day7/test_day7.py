import unittest
from day7exercise import rule_contains_given_bag

class TestDay7Exercises(unittest.TestCase):
    def test_rule_can_contain_given_bag(self):
        ## Arrange
        rule = "light red bags contain 1 bright white bag, 2 muted yellow bags."
        bag = "shiny gold"

        ## Act
        actualResult = rule_contains_given_bag(rule, bag)

        ## Assert
        self.assertFalse(actualResult)
        
    def test_rule_cannot_contain_given_bag(self):
            ## Arrange
        rule = "bright white bags contain 1 shiny gold bag."
        bag = "shiny gold"

        ## Act
        actualResult = rule_contains_given_bag(rule, bag)

        ## Assert
        self.assertTrue(actualResult)


if __name__ == "__main__":
    unittest.main()
