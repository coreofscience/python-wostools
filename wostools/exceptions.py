class WosToolsError(Exception):
    """
    Any exception known by wostools.
    """


class InvalidReference(WosToolsError, ValueError):
    """
    Raised when we try to create an article out of an invalid reference.
    """

    def __init__(self, reference: str):
        super().__init__(f"{reference} does not look like an ISI citation")


class InvalidScopusFile(WosToolsError, ValueError):
    def __init__(self):
        super().__init__(f"The file does not look like a valid bib file")


class InvalidIsiLine(WosToolsError, ValueError):
    """
    Raised when we encounter an invalid line when processing an ISI file.
    """

    def __init__(self, line: str):
        super().__init__(f"'{line}' is not a valid ISI file line")


class MissingLabelFields(WosToolsError, ValueError):
    """
    Raised when we don't have any of the required fields for an ISI reference.
    """

    def __init__(self, article, message: str = None):
        self.article = article
        super().__init__(message or "Missing required fields for label")
