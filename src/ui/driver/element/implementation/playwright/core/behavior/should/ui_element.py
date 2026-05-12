import logging
import re
from typing import Generic

from assertpy import assert_that
from playwright.sync_api import Locator, expect

from core.base.base_behavior import BaseBehavior
from core.types.generic_types import TElement
from core.interface.element import UIAction, UIQuestion, UIShould


class Should(Generic[TElement], BaseBehavior, UIShould):

    def __init__(self, element: TElement):
        super().__init__()
        self._element: TElement = element

    def question(self) -> UIQuestion:
        return self._element.question()

    def action(self) -> UIAction:
        return self._element.action()

    def post_build(self):
        self._encapsulated_element: Locator = self._element.get_underlying_element()

    def be_on_page(self):
        el = self._element.get_parameter('locator') if self._element.get_parameter('locator') is not None else self._element.get_underlying_element()
        assert_that(self._element.question().with_timeout(self.get_timeout() / 1000).is_displayed()).described_as(f"Element '{el}' is not displayed").is_true()
        self._element.action().with_timeout(self.get_timeout() / 1000).go_to()
        if self._element.get_parameter("label"):
            self.have_label()
        # can't remember why I did this, but if element has a text, and is not configured in element builder,
        # here is auto-populated
        # current_tex = self._element.action().get_text()
        # if current_tex != "":
        #     self._element.set_parameter("value", current_tex)
        if self._element.get_parameter("source"):
            self._element.should_().with_timeout(self.get_timeout() / 1000).have_attribute("href", self._element.get_parameter("source"))
        if self._element.get_parameter("value"):
            if self._element.action().with_timeout(self.get_timeout() / 1000).get_attribute("placeholder") and self._element.action().with_timeout(self.get_timeout() / 1000).get_attribute("placeholder") != "":
                assert_that(self._element.action().with_timeout(self.get_timeout() / 1000).get_attribute("placeholder")).is_equal_to(self._element.get_parameter("value"))
            else:
                self._element.should_().with_timeout(self.get_timeout() / 1000).contain_text(self._element.get_parameter("value"))
        if self._element.get_parameter("regexp_value"):
            self._element.should_().with_timeout(self.get_timeout() / 1000).match_text(self._element.get_parameter("regexp_value"))
        self._after_method()
        return self

    # visible means that the element is on the page DOM, is not hidden, and is on the browser viewport
    # if the element is on the DOM, does not have a hidden property but is outside the browser viewport the is not
    # considered as visible, it must be on the visible area of the browser viewport
    def be_visible(self):
        expect(self._encapsulated_element).to_be_visible(timeout=self.get_timeout())
        self._after_method()
        return self

    def be_displayed(self):
        expect(self._encapsulated_element).to_be_attached(timeout=self.get_timeout())
        expect(self._encapsulated_element).not_to_be_hidden(timeout=self.get_timeout())
        self._after_method()
        return self

    def be_disabled(self):
        try:
            expect(self._encapsulated_element).to_be_disabled(timeout=self.get_timeout())
        except AssertionError:
            # Fallback
            has_data_disabled = self._encapsulated_element.get_attribute("data-disabled") is not None
            has_disabled = self._encapsulated_element.get_attribute("disabled") is not None

            if not (has_data_disabled or has_disabled):
                raise AssertionError(f"Element is not disabled [data-disabled:{has_data_disabled}, disabled:{has_disabled}")
        self._after_method()
        return self

    def be_enabled(self):
        expect(self._encapsulated_element).to_be_enabled(timeout=self.get_timeout())
        self._after_method()
        return self

    def be_not_present(self):
        expect(self._encapsulated_element).not_to_be_attached(timeout=self.get_timeout())
        # self._playwright_locator.wait_for(state="detached", timeout=5000)
        self._after_method()
        return self

    def be_present(self):
        expect(self._encapsulated_element).to_be_attached(timeout=self.get_timeout())
        # self._playwright_locator.wait_for(state="attached", timeout=5000)
        self._after_method()
        return self

    def be_not_visible(self):
        expect(self._encapsulated_element).not_to_be_visible(timeout=self.get_timeout())
        self._after_method()
        return self

    def have_text(self, text=None):
        expect(self._encapsulated_element).to_have_text(text, timeout=self.get_timeout())
        self._after_method()
        return self
    is_filled = have_text  # Alias

    def have_no_text(self, text=None):
        expect(self._encapsulated_element).not_to_have_text(text, timeout=self.get_timeout())
        self._after_method()
        return self

    def contain_text(self, text, normalize_text=False):
        final_check = text
        if normalize_text:
            tokens = re.split(r'\s+', text.strip())
            core = r'\s*'.join(map(re.escape, tokens))
            pattern_str = f".*{core}.*"
            final_check = re.compile(pattern_str, re.IGNORECASE | re.DOTALL)
        expect(self._encapsulated_element).to_contain_text(final_check, use_inner_text=True, timeout=self.get_timeout())
        self._after_method()
        return self

    def match_text(self, text_expression=None):
        current_text = self._element.action().get_text()
        assert_that(current_text).matches(text_expression)
        self._after_method()
        return self

    def have_value(self, value):
        expect(self._encapsulated_element).to_have_value(value, timeout=self.get_timeout())
        self._after_method()
        return self

    def have_css_class(self, css):
        expect(self._encapsulated_element).to_have_class(css, timeout=self.get_timeout())
        self._after_method()
        return self

    def no_have_css_class(self, css):
        expect(self._encapsulated_element).not_to_have_class(css, timeout=self.get_timeout())
        self._after_method()
        return self

    def contain_css_class(self, class_name):
        expect(self._encapsulated_element).to_contain_class(class_name, timeout=self.get_timeout())
        self._after_method()
        return self

    def no_contain_css_class(self, css):
        expect(self._encapsulated_element).not_to_contain_class(css, timeout=self.get_timeout())
        self._after_method()
        return self

    def contain_css_class_or_fail_on(self, expected_class: str, failure_class: str):
        import time
        timeout_ms = self.get_timeout()
        poll_interval_ms = 500  # Check every 500ms
        start_time = time.time() * 1000
        last_log_time = start_time  # Track last log time

        while True:
            # Check if failure class appeared (fail fast)
            class_attr = self._encapsulated_element.get_attribute("class", timeout=poll_interval_ms)
            if class_attr:
                classes = class_attr.split()

                # Fail immediately if failure class is found
                if failure_class in classes:
                    self._after_method()
                    raise AssertionError(
                        f"Element has failure class '{failure_class}'. "
                        f"Expected class '{expected_class}' but found failure state. "
                        f"Current classes: {class_attr}"
                    )

                # Success if expected class is found
                if expected_class in classes:
                    self._after_method()
                    return self

            # Check timeout
            elapsed_ms = (time.time() * 1000) - start_time
            if elapsed_ms >= timeout_ms:
                self._after_method()
                raise TimeoutError(
                    f"Timeout waiting for class '{expected_class}'. "
                    f"Neither '{expected_class}' nor '{failure_class}' appeared within {timeout_ms}ms. "
                    f"Current classes: {class_attr}"
                )

            # Log every 10 seconds
            current_time = time.time() * 1000
            if current_time - last_log_time >= 10000:  # 10 seconds
                logging.info(f"Still waiting for '{expected_class}' or '{failure_class}'. Elapsed time: {elapsed_ms:.0f} ms")
                last_log_time = current_time

            # Wait before next poll
            time.sleep(poll_interval_ms / 1000)

    def have_text_label(self, text):
        expect(self._element.action().get_parent().get_underlying_element().locator("label")).to_have_text(text, timeout=self.get_timeout())
        self._after_method()
        return self

    def have_label(self):
        self.have_text_label(self._element.get_parameter("label"))
        self._after_method()
        return self

    def have_data_tip_attribute_empty(self):
        raise NotImplementedError
        self._after_method()
        return self

    def have_attribute(self, attribute, value=None):
        expect(self._encapsulated_element).to_have_attribute(attribute, value, timeout=self.get_timeout())
        self._after_method()
        return self

    def no_have_attribute(self, attribute):
        raise NotImplementedError
        self._after_method()
        return self

    def be_empty(self):
        expect(self._encapsulated_element).to_have_text('', timeout=self.get_timeout())
        self._after_method()
        return self

    def have_css_property(self, attribute, value):
        try:
            expect(self._encapsulated_element).to_have_css(attribute, value, timeout=self.get_timeout())
        except AssertionError as e:
            logging.error(str(e))
            computed_value = self._encapsulated_element.evaluate(f"el => window.getComputedStyle(el).getPropertyValue('{attribute}')")
            error = f"CSS property '{attribute}' does not contain expected value '{value}'. Computed value: '{computed_value}'."
            assert_that(value).described_as(error).is_in(computed_value)
        self._after_method()
        return self

    def have_error(self):
        raise NotImplementedError
        self._after_method()
        return self
