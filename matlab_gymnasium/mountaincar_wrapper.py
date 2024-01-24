import time

import gymnasium
import matlab.engine
import numpy as np


class MountainCarWrapper(gymnasium.Env):
    def __init__(
        self,
        matlab_engine=None,
        action_range=np.array([-1.0, 1.0]),
        position_range=np.array([-1.2, 0.6]),
        max_speed=0.07,
        cpower=0.0015,
        goal_position=0.45,
        goal_velocity=0.0,
    ) -> None:
        super().__init__()

        self.action_range = action_range
        self.position_range = position_range
        self.max_speed = max_speed
        self.cpower = cpower
        self.goal_position = goal_position
        self.goal_velocity = goal_velocity

        # Connect to MATLAB engine
        # TODO: switch to using logging package
        print("Connecting to MATLAB engine...")
        start_time = time.time()
        if matlab_engine is not None:
            self.eng = matlab.engine.connect_matlab(matlab_engine)
        else:
            self.eng = matlab.engine.start_matlab()
        print(
            f"MATLAB connection established in {time.time() - start_time:.2f}s."  # noqa: E501
        )  # TODO: switch to using logging package

        # Define spaces
        self.action_space = gymnasium.spaces.Box(
            low=action_range[0], high=action_range[1], shape=(1,)
        )
        self.observation_space = gymnasium.spaces.Box(
            low=np.array([position_range[0], -max_speed]),
            high=np.array([position_range[1], max_speed]),
            shape=(2,),
        )

        self.reset()

    def reset(self) -> np.ndarray:
        # Initialise MATLAB version of the environment
        self.matlab_env = self.eng.MountainCar(
            matlab.double(self.action_range),
            matlab.double(self.position_range),
            matlab.double(self.max_speed),
            matlab.double(self.cpower),
        )

        return np.array(self.eng.reset(self.matlab_env))[0]

    def step(self, action) -> (np.ndarray, float, bool, bool, dict):
        state = np.array(
            self.eng.step(
                self.matlab_env,
                matlab.double(action),
            )
        )[0]

        terminated = bool(
            state[0] >= self.goal_position and state[1] >= self.goal_velocity
        )

        reward = 0
        if terminated:
            reward = 100.0
        reward -= np.power(action[0], 2) * 0.1

        truncated = False
        info = {}

        return state, reward, terminated, truncated, info
