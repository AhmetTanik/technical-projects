"""Autonomous drone navigation system skeleton.

This module defines classes for sensor fusion, obstacle detection, path planning,
and high‑level control. The goal is to illustrate how these components
interoperate rather than to provide a complete implementation.

Author: Ahmet Tanık
Date: 2024
"""

from dataclasses import dataclass
from typing import List, Tuple
import math
import random


@dataclass
class Pose:
    """Represents a 2‑D position and orientation."""

    x: float
    y: float
    yaw: float


class SensorFusion:
    """Aggregates data from multiple sensors to estimate the drone's pose."""

    def __init__(self) -> None:
        # Initialize state estimate (x, y, yaw) and velocities
        self.pose = Pose(0.0, 0.0, 0.0)
        self.velocity = (0.0, 0.0)

    def update(self) -> Pose:
        """Update the pose estimate using dummy sensor data.

        In a real implementation this method would fuse data from IMU,
        GPS, and LiDAR/sonar sensors. Here we randomly wander to simulate
        motion.

        Returns
        -------
        Pose
            The estimated pose after the update step.
        """
        dx = random.uniform(-0.5, 0.5)
        dy = random.uniform(-0.5, 0.5)
        dyaw = random.uniform(-math.pi / 10, math.pi / 10)
        self.pose = Pose(
            self.pose.x + dx,
            self.pose.y + dy,
            (self.pose.yaw + dyaw) % (2 * math.pi),
        )
        return self.pose


class ObstacleDetector:
    """Detects obstacles around the drone and suggests avoidance actions."""

    def __init__(self, detection_range: float = 5.0) -> None:
        self.detection_range = detection_range

    def detect(self, pose: Pose, obstacles: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
        """Return a list of obstacles within the detection range.

        Parameters
        ----------
        pose : Pose
            The current estimated pose of the drone.
        obstacles : list of tuple
            A list of (x, y) coordinates representing obstacle positions.

        Returns
        -------
        list of tuple
            Obstacles within detection range.
        """
        nearby = []
        for (ox, oy) in obstacles:
            distance = math.hypot(ox - pose.x, oy - pose.y)
            if distance < self.detection_range:
                nearby.append((ox, oy))
        return nearby


class PathPlanner:
    """Plans a path to a goal using a simple greedy algorithm.

    For demonstration, this planner moves directly toward the goal
    while making small adjustments to avoid obstacles. In practice,
    a more sophisticated algorithm like A* would be used.
    """

    def __init__(self, step_size: float = 1.0) -> None:
        self.step_size = step_size

    def plan(self, start: Pose, goal: Tuple[float, float], obstacles: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
        """Generate a list of waypoints from start to goal.

        Parameters
        ----------
        start : Pose
            Starting pose.
        goal : tuple
            Desired (x, y) goal location.
        obstacles : list of tuple
            Positions of obstacles to avoid.

        Returns
        -------
        list of tuple
            Waypoints forming a path to the goal.
        """
        path = []
        current = (start.x, start.y)
        while math.hypot(goal[0] - current[0], goal[1] - current[1]) > self.step_size:
            # naive direction vector toward the goal
            direction = (
                goal[0] - current[0],
                goal[1] - current[1],
            )
            length = math.hypot(*direction)
            if length == 0:
                break
            step = (direction[0] / length * self.step_size, direction[1] / length * self.step_size)
            next_pos = (current[0] + step[0], current[1] + step[1])
            # simple obstacle avoidance: if next position collides, sidestep
            collision = any(math.hypot(ob[0] - next_pos[0], ob[1] - next_pos[1]) < self.step_size for ob in obstacles)
            if collision:
                # sidestep perpendicular to direction vector
                next_pos = (current[0] - step[1], current[1] + step[0])
            path.append(next_pos)
            current = next_pos
        path.append(goal)
        return path


class DroneController:
    """High‑level controller coordinating sensor fusion, obstacle detection, and path planning."""

    def __init__(self) -> None:
        self.sensor_fusion = SensorFusion()
        self.obstacle_detector = ObstacleDetector()
        self.path_planner = PathPlanner(step_size=1.0)

    def navigate_to(self, goal: Tuple[float, float], obstacles: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
        """Plan a path to the goal given the current sensor estimates and obstacles.

        Returns
        -------
        list of tuple
            The planned waypoints.
        """
        pose = self.sensor_fusion.update()
        nearby = self.obstacle_detector.detect(pose, obstacles)
        path = self.path_planner.plan(pose, goal, nearby)
        return path


def main() -> None:
    """Run a simple simulation demonstrating the components."""
    controller = DroneController()
    goal = (10.0, 10.0)
    # generate random obstacles
    obstacles = [(random.uniform(-5, 15), random.uniform(-5, 15)) for _ in range(10)]
    for step in range(5):
        pose = controller.sensor_fusion.update()
        nearby = controller.obstacle_detector.detect(pose, obstacles)
        path = controller.path_planner.plan(pose, goal, nearby)
        print(f"\nStep {step + 1}:")
        print(f"Current pose: {pose}")
        print(f"Nearby obstacles: {nearby}")
        print(f"Planned path: {path[:3]} ... (truncated)")


if __name__ == "__main__":
    main()