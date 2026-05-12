from core.interface.collection_element import (
    CollectionElement, CollectionElmntAction, CollectionElmntFilter, CollectionElmntShould
)
from core.interface.element import Element


class CollectionElementFilter(CollectionElmntFilter):

    def __init__(self, collection: CollectionElement):
        self._collection: CollectionElement = collection

    def should_(self) -> CollectionElmntShould:
        return self._collection.should_()

    def action(self) -> CollectionElmntAction:
        return self._collection.action()

    def by_text(self, text: str) -> "CollectionElementFilter":
        """All elements containing the given text."""
        main_locator = self._collection.get_parameter("locator")
        self._collection._underlying_collection = self._collection.get_parameter("driver").utilities().get_underlying_driver().locator(main_locator).filter(has_text=text).all()
        return self

    def by_exact_text(self, text: str) -> "CollectionElementFilter":
        """All elements matching the given text."""
        raise NotImplementedError

    def by_attribute(self, attribute: tuple[str, str]) -> "CollectionElementFilter":
        """All elements matching the attribute."""
        main_locator = self._collection.get_parameter("locator")
        filter_locator = self._collection.get_parameter("driver").locator(f"[{attribute[0]}='{attribute[1]}']")
        self._collection._underlying_collection = self._collection.get_parameter("driver").locator(main_locator).filter(has=filter_locator).all()
        return self

    def nth(self, index: int) -> Element:
        locator = self._collection.get_underlying_collection()[index]
        element = self._collection.get_parameter("driver").Element().from_wrapped(locator).build()
        return element

    def first(self) -> Element:
        return self.nth(0)

    def second(self) -> Element:
        return self.nth(1)

    def by_first_match(self, text: str) -> Element:
        """Return first element that matches the given text."""
        raise NotImplementedError
