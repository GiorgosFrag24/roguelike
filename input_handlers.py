from typing import Optional
from actions import Action, EscapeAction, MovementAction
import tcod.event

"""
We’re creating a class called EventHandler, which is a subclass of tcod’s EventDispatch class. 
EventDispatch is a class that allows us to send an event to its proper method based on what 
type of event it is. 
"""


class EventHandler(tcod.event.EventDispatch[Action]):

    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        if key == tcod.event.K_UP:
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = MovementAction(dx=1, dy=0)

        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        # No valid key was pressed
        return action
