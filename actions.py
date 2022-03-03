"""
So what’s the plan for these classes? Basically, whenever we have an “action”,
we’ll use one of the subclasses of Action to describe it. We’ll be able to detect
which subclass we’re using, and respond accordingly. In this case, EscapeAction
will be when we hit the Esc key (to exit the game),
and MovementAction will be used to describe our player moving around.
"""
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity


class Action:
    def perform(self, engine: Engine, entity: Entity) -> None:

        """
        Perform this action with the objects needed to determine its scope.

        `engine` is the scope this action is being performed in.

        `entity` is the object performing the action.

        This method must be overridden by Action subclasses.
        """
        raise NotImplementedError()


class EscapeAction(Action):
    def perform(self, engine: Engine, entity: Entity) -> None:
        raise SystemExit()


class MovementAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()
        self.dx = dx
        self.dy = dy

    def perform(self, engine: Engine, entity: Entity) -> None:

        dest_x = entity.x + self.dx

        dest_y = entity.y + self.dy

        if not engine.game_map.in_bounds(dest_x, dest_y):
            return  # Destination is out of bounds.

        if not engine.game_map.tiles["walkable"][dest_x, dest_y]:
            return  # Destination is blocked by a tile.

        entity.move(self.dx, self.dy)
