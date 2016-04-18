:css: css/presentation.css
:skip-help: true

.. title:: GENETIC ALGORITHMS

----

Genetic algorithms
==============================================================================

Tomek Kwiecien
----------------------------------------------------------------

----

Mimicing nature
==========================

Genetic algorithms try to imitagte evolution on a very basic / naive level.

----

Type of problems
==========================

Genetic algorithms are used for **optimization** tasks. It means you already have solutions and a way to tell which ones are better.

----

Finding the best solution
===========================

* Brute force: generate all, pick best
* Genetic algorithms: change existing set of solutions until they evolve into the best one

----

Car problem
=================

Create a car out of several parts.

* Brute force: a lot of solutions without wheels
* Genetic algorithms: we evolve only the best solutions, the rest die out

----

Structure
============

* feature
* individuals / solutions
* population
* generation

----

Operations
===========

* fitness
* selection
* reproduction
* crossover
* mutation

----

Diversity
====================

Fitness is not all you need for avoiding local maximum. You want both, fit and diverse individuals.

----

Gen-inder
===============

Grow the best individual for a client.

----

Gosia
===========================

.. image:: images/gosia.jpg

----

Gosia v2
===========

.. image:: images/gosia2.jpg

----

Tofik
============================

.. image:: images/tofiks.jpg

----

Features
============================

* skin
* eyes
* hair
* nose

----

Process
============================

1. We present the current population to Gosia
2. Gosia ranks the individuals
3. We generate new population based on Gosia's ranking
4. Repeast until we have a perfect fit

----

Gosia returns
===============

.. image:: images/gosia2.jpg

----

Links
=====================================

* Evolved Virtual Creatures - https://www.youtube.com/watch?v=JBgG_VSP7f8
* Genetic algorithms overview - https://www.youtube.com/watch?v=ziMHaGQJuSI
* Gen cars - http://rednuht.org/genetic_cars_2/
