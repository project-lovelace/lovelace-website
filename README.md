# Project Lovelace website

[![Tests](https://github.com/project-lovelace/lovelace-website/actions/workflows/ci.yml/badge.svg)](https://github.com/project-lovelace/lovelace-website/actions/workflows/ci.yml)

[Project Lovelace](http://projectlovelace.net) is a bunch of free scientific programming problems. Each problem teaches you some science like how to simulate a guitar, splice DNA, or predict the weather, and requires the use of scientific insight and some programming skills to solve. The problems get progressively harder but the goal is to learn cool science through programming (or vice versa)!

This repository holds the website frontend HTML, CSS, and Django template code which was created using Bulma as well as the server backend code which uses the Django framework.

## New problem submission guide

If you have an idea for a new problem please consider submitting a new problem, we love receiving new contributions!
We discuss new problems on Discord mostly but you can also open a GitHub issue or post on Discourse to discuss. Also feel free to ask us any questions at all!
Let us know if you're interested in submitting new problems so we can invite you to the [Project Lovelace GitHub organization](https://github.com/project-lovelace).

There are three steps to submitting a new problem:

1. Open a pull request to [lovelace-solutions](https://github.com/project-lovelace/lovelace-solutions#new-problem-submission-guide) with the solution to the problem.
2. Open a pull request to [lovelace-problems](https://github.com/project-lovelace/lovelace-problems#new-problem-submission-guide) with code to generate test cases for the problem.
3. Open a pull request to lovelace-website with the problem description, code stubs, and any visualization code. (You are here!)

### How to submit a new problem description

1. Add a new problem description to the [`src/problems/templates/problems/`](https://github.com/project-lovelace/lovelace-website/tree/main/src/problems/templates/problems) directory. It's mostly HTML but has some Django template stuff in there, but you should be able to create one by following what the other templates look like.
2. Add code stubs for the new problem in the [`src/static/code_stubs/`](https://github.com/project-lovelace/lovelace-website/tree/main/src/static/code_stubs) directory. If you're not sure what the code stub should look like, you can leave it blank (i.e. leave an empty file).
3. Add problem-specific visualization code to the [`src/static/visualization/`](https://github.com/project-lovelace/lovelace-website/tree/main/src/static/visualization) directory. This tells your browser how to render and visualize the test case results. Usually it's just text but you could get fancy and plot things with Plotly if you want.
4. Open a pull request! Once all the tests pass it can be merged.
