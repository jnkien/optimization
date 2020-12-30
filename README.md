# Optimization algorithms

![equ](https://latex.codecogs.com/gif.latex?\arg\min_{x}&space;f(x))

A description of algorithms is available [here](http://fa.bianp.net/teaching/2018/COMP-652/).

This repository contains my naive implementations in python in order to understand the different methods.

# Stochastic Gradient Descent

Talk [here](https://www.youtube.com/watch?v=k3AiUhwHQ28)

SGD is like GD but with a "partial" gradient computation. This "partial" part can be done by randomness + bagging and this allows parallelization for GD.

SGD is more sensitive to the step-size than GD.

SGD convergence is sensitive to the step-size. It is stable at start and the closer it goes to the solution the more fluctuating it is. It is good in ML to go to a solution quickly.

SGD is unbiased with respect to the randomness used.

The speed of the SGD convergence depends of the level of noise it has => the variance of the SGD.

Back-propagation in neural networks IS SGD.
