from .ui_element import Action
from core.interface.button import Button, BtnAction, BtnQuestion, BtnShould


class ButtonAction(Action[Button], BtnAction):

    def __init__(self, element: Button):
        super().__init__(element)

    def should_(self) -> BtnShould:
        return self._element.should_()

    def question(self) -> BtnQuestion:
        return self._element.question()

    # In some actions, there is a loader at left on the button.
    # This method check that the action that trigger the button finish
    def wait_until_process_action_finish(self):
        raise NotImplementedError
