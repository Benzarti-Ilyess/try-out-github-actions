[![CI](https://github.com/Benzarti-Ilyess/try-out-github-actions/actions/workflows/pipeline.yml/badge.svg)](https://github.com/Benzarti-Ilyess/try-out-github-actions/actions/workflows/pipeline.yml)

# Try-out-github-actions

This repo is intented to try out github actions pipelines. 

The Pipeline will be triggered when code is pushed on **main** branch or on Pull Requests against the **main** branch.

The Pipeline consists of the following steps on a ubuntu-latest docker container: 

* Checkout repository
* Configure python with specific version
* Install Pytest, isort and black
* Check python import modules order with isort and give developer information of how the modules should be sorted
* Check code formatting with black and give developer information of how code should be formatted
* Execute tests with pytest


