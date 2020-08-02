Feature: cached collection

   We want this kind of collection to avoid duplication at all costs

   Scenario: preheat cache

      Given some valid isi text
      When I create a collection from that text
      Then the collection's cache is preheated

   Scenario: collection list articles and references

      Given a valid collection
      When I iterate over the collection
      Then all articles and references are present

   Scenario: list authors

      Given a valid collection
      When I iterate over the collection authors
      Then all authors are included
      And the author list include duplicates

   Scenario: list coauthors

      Given a valid collection
      When I iterate over the collection coauthors
      Then all coauthor pairs are included
      And the coauthor list include duplicates

   Scenario: duplicated articles are removed

      Given somve valid isi text
      When I create a collection from that text
      And I create a collection from twice that text
      Then both collections have the same number of articles

   Scenario: citation pairs

      Given a valid collection
      When I list the collection's citation pairs
      Then all citation pairs are included

   Scenario: citation pairs include complete info from references

      Given some valid isi record
      And a diferent isi record that references the former
      When I create a collection from that text
      And I list the collection's citation pairs
      Then the citation always include all the available data