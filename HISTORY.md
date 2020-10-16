# History

## 3.0.0 (2020-10-15)

- (!) Adds scopus RIS format support.
- Drops support for `LazyCollection`.
- Adds docummented support for Python 3.8 and 3.9
- Drops docummented support for Python 3.6.
- Improves article matching in collections.

## 2.0.7 (2020-08-23)

- Remove from the collection those documents whose label is unknow or conflictive.

## 2.0.6 (2020-08-21)

- Accomodate for unknown fields in ISI WOS files.

## 2.0.5 (2020-08-15)

- Fix and prevent distribution accidents.

## 2.0.4 (2020-08-15)

- Add issue to the articles plain dict output.
- Fix some bugs with issues.

## 2.0.3 (2020-08-15)

- Add issue to the articles top level.

## 2.0.2 (2020-08-09)

- Fix bug with first author merging articles.
- Remove instances where we inherit from `object`.

## 2.0.1 (2020-08-09)

- Fix error with wos files that have an invisible character before the field
  key.

## 2.0.0 (2020-08-08)

- Make the article class more concrete
- Make collections iterable
- Add cached and lazy collections for different use cases

## 0.2.0 (2018-08-12)

- Add support for all WOS fields.
- Add graph building support.
- Add a little cli for common tasks.

## 0.1.1 (2018-05-10)

- First release on PyPI.
