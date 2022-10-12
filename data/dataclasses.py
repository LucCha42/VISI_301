from dataclasses import dataclass

from numpy import ndarray, zeros
from pygame import Rect, Surface

from data.constants import GOO_PARTICLES_INIT_RADIUS


@dataclass(frozen=True)
class Tile:
    rect: Rect
    sprite: Surface


@dataclass(frozen=True)
class Obstacle:
    rect: Rect
    sprite: Surface
    orientation: ndarray


@dataclass(frozen=True)
class AmethystParticle:
    pos: ndarray
    timer: float = 0


@dataclass(frozen=True)
class GooParticle:
    pos: ndarray
    velocity: ndarray
    timer: float = 0
    radius: float = GOO_PARTICLES_INIT_RADIUS


@dataclass(frozen=True)
class Player:
    pos: ndarray
    rect: Rect
    velocity: ndarray = zeros(2, dtype=float)
    on_ground: bool = False
    obstacle_collision: bool = False


@dataclass(frozen=True)
class Grapple:
    start: ndarray = zeros(2, dtype=float)  # start position of the grapple (=player position) in world space
    end: ndarray = zeros(2, dtype=float)  # end position of the grapple in world space
    head: ndarray = zeros(2, dtype=float)
    head_velocity: ndarray = zeros(2, dtype=float)
    head_start: ndarray = zeros(2, dtype=float)  # point at which the head is fired


@dataclass(frozen=True)
class Lava:
    height: float
    triggered: bool = False


@dataclass(frozen=True)
class Camera:
    center: ndarray  # world position on which the camera is centered
    heading: ndarray = zeros(2, dtype=float)  # world vector pointing on focus position
    top_left: ndarray = zeros(2, dtype=float)  # world position of the top left corner of the camera
    offset: ndarray = zeros(2, dtype=float)  # offset to apply to a sprite position to get its screen position
