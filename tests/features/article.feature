Feature: Article manager class

   Allows the user to parse and sort of dump articles

   Scenario: Computing an article's label
      Given an article with authors, year and journal
      When I compute the label for the article
      Then the label is a proper string

   Scenario Outline: Fail to compute a label
      Given a complete article missing <field>
      When I try to compute the label for the article
      Then There's an error computing the label

      Examples:
         | field   |
         | year    |
         | authors |
         | journal |

   Scenario: Merge two articles
      Given a complete article
      And theres a similar article that includes a doi

      When I merge the two articles
      And I try to compute the label for the article

      Then the article's doi matches the other
      And there's no error computing the label
      And the label contains the doi of the other
