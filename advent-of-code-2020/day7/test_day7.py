import unittest
import day7exercise


class TestDay7Exercises(unittest.TestCase):

    # Tests for rule_contains_given_bag method
    def test_rule_can_contain_given_bag(self):
        # Arrange
        rule = "light red bags contain 1 bright white bag, 2 muted yellow bags."
        bag = "shiny gold"

        # Act
        actualResult = day7exercise.rule_contains_given_bag(rule, bag)

        # Assert
        self.assertFalse(actualResult)

    def test_rule_cannot_contain_given_bag(self):
        # Arrange
        rule = "bright white bags contain 1 shiny gold bag."
        bag = "shiny gold"

        # Act
        actualResult = day7exercise.rule_contains_given_bag(rule, bag)

        # Assert
        self.assertTrue(actualResult)

    # Tests for list_bags_that_contain_bag method

    def test_list_bags_that_contain_bag(self):
        # Arrange
        rules = [
            "light red bags contain 1 bright white bag, 2 muted yellow bags.",
            "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
            "bright white bags contain 1 shiny gold bag.",
            "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
            "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
            "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
            "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
            "faded blue bags contain no other bags.",
            "dotted black bags contain no other bags."
        ]
        bag = "shiny gold"

        # Act
        actualResult = day7exercise.list_bags_that_contain_bag(rules, bag)

        # Assert
        expectedResult = ["bright white", "muted yellow"]
        self.assertCountEqual(actualResult, expectedResult)

    def test_no_rules_contain_bag(self):
        # Arrange
        rules = [
            "light red bags contain 1 bright white bag, 2 muted yellow bags.",
            "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
            "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
            "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
            "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
            "faded blue bags contain no other bags.",
            "dotted black bags contain no other bags."
        ]
        bag = "shiny gold"

        # Act
        actualResult = day7exercise.list_bags_that_contain_bag(rules, bag)

        # Assert
        expectedResult = []
        self.assertCountEqual(actualResult, expectedResult)

        # Tests for list_bags_that_contain_bag method

    def test_list_bags_that_eventually_contain_bag(self):
        # Arrange
        rules = [
            "light red bags contain 1 bright white bag, 2 muted yellow bags.",
            "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
            "bright white bags contain 1 shiny gold bag.",
            "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
            "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
            "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
            "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
            "faded blue bags contain no other bags.",
            "dotted black bags contain no other bags."
        ]
        bag = "shiny gold"

        # Act
        actualResult = day7exercise.list_bags_that_eventually_contain_bag(
            rules, bag)

        # Assert
        expectedResult = ["bright white", "muted yellow",
                          "dark orange", "light red"]
        self.assertCountEqual(actualResult, expectedResult)

    def test_no_rules_can_eventually_contain_bag(self):
        # Arrange
        rules = [
            "light red bags contain 1 bright white bag, 2 muted yellow bags.",
            "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
            "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
            "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
            "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
            "faded blue bags contain no other bags.",
            "dotted black bags contain no other bags."
        ]
        bag = "shiny gold"

        # Act
        actualResult = day7exercise.list_bags_that_eventually_contain_bag(
            rules, bag)

        # Assert
        expectedResult = []
        self.assertCountEqual(actualResult, expectedResult)


if __name__ == "__main__":
    unittest.main()
