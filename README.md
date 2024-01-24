# MATLAB/Python Gymnasium interface

This repository provides an example of a Python Gymnasium interface to a MATLAB simulation.
In this case, the MATLAB simulation is a MATLAB version of the continuous MountainCar environment.

## Installation

Note that because `matlabengine` requires an existing MATLAB installation, it can be quite finicky to get everything to install correctly.

| MATLAB Release | Compatible Python versions | Compatible `matlabengine` versions                                  |
| -------------- | -------------------------- | ------------------------------------------------------------------- |
| R2023b         | 3.9, 3.10, 3.11            | 23.2.1, 9.15.2                                                      |
| R2023a         | 3.8, 3.9, 3.10             | 9.14.3, 9.14.2                                                      |
| R2022b         | 3.8, 3.9, 3.10             | 9.13.9, 9.13.8, 9.13.7, 9.13.6, 9.13.5, 9.13.4, 9.13.1              |
| R2022a         | 3.8, 3.9                   | 9.12.19, 9.12.17, 9.12.16, 9.12.15, 9.12.14, 9.12.12, 9.12.10, 9.12 |
| R2021b         | 3.7, 3.8, 3.9              | 9.11.21, 9.11.19                                                    |
| R2021a         | 3.7, 3.8                   | 9.10.3, 9.10.1                                                      |
| R2020b         | 3.6, 3.7, 3.8              | 9.9.4, 9.9.1                                                        |

There may be other `matlabengine` releases, these were the ones available on [PyPI](https://pypi.org/project/matlabengine/#history).

## Development

Python version is managed with `conda`.

Tests should be done with `pytest` (TODO).

Code should be linted with `flake8`.

Code should be formatted with `black`.


## TODO

- [ ] Write unit tests
  - [ ] Python
  - [ ] MATLAB
- [ ] Write CI/CD
  - [ ] Pre-commit hooks
  - [ ] Testing
- [ ] Check for compatibility with containerised MATLAB codes
