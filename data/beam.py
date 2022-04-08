from dataclasses import dataclass, replace
from typing import List

import pygame
from pygame.math import Vector2
from pygame.surface import Surface

from data.constants import BEAM_STRENGTH, RED, BEAM_DECREASE, TILE_EDGE, BEAM_VECTOR_STEP, \
    BEAM_MAX_VECTOR_STEP
from data.player import Player
from data.tile import Tile


@dataclass(frozen=True)
class Beam:
    start: Vector2 = Vector2(0)
    end: Vector2 = Vector2(0)
    power: float = 0.0


def display_beam(beam: Beam, screen: Surface) -> None:
    """
    Displays the beam on the screen.

    :param beam: beam object
    :param screen: screen surface
    """
    pygame.draw.line(
        screen,
        RED,
        beam.start,
        beam.end,
        int(beam.power * TILE_EDGE / 2)
    )


def update_beam(
        beam: Beam,
        player: Player,
        tiles: List[Tile],
        delta: float
) -> Beam:
    """
    Updates the beam, decreasing its power and setting its start and end points.

    :param beam: beam object
    :param player: player object
    :param tiles: list of tile objects
    :param delta: delta time
    :return: updated beam object
    """
    start: Vector2 = Vector2(player.rect.center)
    end: Vector2 = Vector2(start)

    step: Vector2 = pygame.mouse.get_pos() - start
    step.scale_to_length(BEAM_VECTOR_STEP)

    # increasing vector until it collides with a tile
    end += step
    collide: bool = False
    for _ in range(BEAM_MAX_VECTOR_STEP):

        for tile in tiles:
            if tile.rect.collidepoint(tuple(end)):
                collide = True
                break

        if collide:
            break

        end += step

    power: float = beam.power - BEAM_DECREASE * delta
    power = power if beam.power > 0 else 0  # clamp power to 0

    return replace(beam, start=start, end=end, power=power)


def fire(beam: Beam) -> Beam:
    """
    Fires the beam, setting its power to the maximum.

    :param beam: beam object
    :return: updated beam object
    """
    return replace(beam, power=1)


def get_beam_velocity(beam: Beam) -> Vector2:
    """
    Returns the velocity impulse the beam would give to the player.
    Returns a zero vector if the beam has no power left.

    :param beam: beam object
    :return: updated beam object
    """
    if beam.power > 0:
        v: Vector2 = beam.start - beam.end
        v.scale_to_length(BEAM_STRENGTH)
        return v
    return Vector2(0)