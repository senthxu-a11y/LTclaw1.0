# -*- coding: utf-8 -*-
"""LTCLAW-GY.X Agents Module.

This module provides the main agent implementation and supporting utilities
for building AI agents with tools, skills, and memory management.

Public API:
- LTCLAW-GY.XAgent: Main agent class
- create_model_and_formatter: Factory for creating models and formatters

Example:
    >>> from ltclaw_gy_x.agents import LTCLAW-GY.XAgent, create_model_and_formatter
    >>> agent = LTCLAW-GY.XAgent()
    >>> # Or with custom model
    >>> model, formatter = create_model_and_formatter()
"""

# LTCLAW-GY.XAgent is lazy-loaded so that importing agents.skills_manager (e.g.
# from CLI init_cmd/skills_cmd) does not pull react_agent, agentscope, tools.
# pylint: disable=undefined-all-variable
__all__ = ["LTCLAW-GY.XAgent", "create_model_and_formatter"]


def __getattr__(name: str):
    """Lazy load heavy imports."""
    if name == "LTCLAW-GY.XAgent":
        from .react_agent import LTCLAW-GY.XAgent

        return LTCLAW-GY.XAgent
    if name == "create_model_and_formatter":
        from .model_factory import create_model_and_formatter

        return create_model_and_formatter
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
