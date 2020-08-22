Feature: Article manager class

   Allows the user to parse and sort of dump articles

   Scenario: Computing an article's label
      Given an article with authors, year and journal
      When I compute the label for the article
      Then the label is a proper string

   Scenario Outline: Fail to compute a label
      Given a complete article missing <field>
      When I try to compute the label for the article
      Then the label is returned as None

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

   Scenario: Parse article from isi text
      Given some valid isi text
      When I create an article from the isi text
      Then the values in the isi text are part of the article
      And the isi text itself is part of the articles sources

   Scenario: Parse article from invalid isi text
      Given some isi text with invalid lines
      When I create an article from the isi text
      Then an invalid line error is risen

   Scenario: Turn an article to dict
      Given a reference article
      When I turn the article into a dict
      Then I get a reference dict of values

   Scenario: Parse article from citation
      Given some valid isi citation
      When I create an article from the citation
      Then the values of the citation are part of the article
      And the citation itself is part of the articles sources

   Scenario: Parse article from an invalid citation
      Given some invalid isi citation
      When I create an article from the citation
      Then an invalid reference error is risen