from contextlib import contextmanager
from dataclasses import dataclass
from typing import Generic, Iterator, List, Optional, TypeVar

T = TypeVar("T")


@dataclass
class Context(Generic[T]):
    history: Optional[List[T]] = None
    error: Optional[Exception] = None
    data: Optional[T] = None

    def push(self, data: Optional[T], error: Optional[Exception] = None):
        if self.history is None:
            self.history = []
        if self.data:
            self.history.append(self.data)
        self.data = data
        self.error = error

    @contextmanager
    def capture(self):
        try:
            yield
        except Exception as e:
            self.push(None, error=e)

    @contextmanager
    def assert_data(self, name=None) -> Iterator[T]:
        if name is None:
            name = "data"
        assert self.data, f"No {name} computed yet"
        yield self.data

    @contextmanager
    def assert_error(self) -> Iterator[Exception]:
        assert self.error, f"Expected an error and found none"
        yield self.error

    @contextmanager
    def assert_history(self, count):
        assert len(self.history) >= count
        yield self.history[-count:]
