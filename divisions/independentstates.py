# --- Imports --- #

from .states import State

__all__ = ("IndependentState",)


# --- IndependentState Class --- #

class IndependentState(State):
    """A state-like object that is not a state. Ex. Washington, D.C., US"""
    pass
