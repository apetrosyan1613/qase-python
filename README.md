# [Qase TMS](https://qase.io) Python Api Client

[![License](https://lxgaming.github.io/badges/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)

# Installation

```
pip install qaseio
```

## Usage ##
Qase.io uses API tokens to authenticate requests. You can view an manage your API keys in [API tokens pages](https://app.qase.io/user/api/token).

You must replace api_token with your personal API key.

```python
from qaseio.client import QaseApi

qase = QaseApi("api_token")
```

### Projects ###

#### Get All Projects ####
This method allows to retrieve all projects available for your account. You can you limit and offset params to paginate.

```python
projects = qase.projects.get_all()
```

#### Get a specific project ####
This method allows to retrieve a specific project.

```python
project = qase.projects.get("PRJCODE")
```

#### Check project exists ####

```python
exists = qase.projects.exists("PRJCODE")
```

#### Create a new project ####
This method is used to create a new project through API.

```python
from qaseio.client.models import ProjectCreate

project = qase.projects.create(
    ProjectCreate("Test project", "PRJCODE")
)
```

### Test cases ###

#### Get all test cases ####
This method allows to retrieve all test cases stored in selected project. You can you limit and offset params to paginate.

```python
test_cases = qase.cases.get_all("PRJCODE")
```

#### Get a specific test case ####
This method allows to retrieve a specific test case.

```python
test_case = qase.cases.get("PRJCODE", 4)
```

#### Check test case exists ####

```python
exists = qase.cases.exists("PRJCODE", 4)
```

#### Delete test case ####
This method completely deletes a test case from repository.

```python
qase.cases.delete("PRJCODE", 4)
```

### Test Suites ###

#### Get all test suites ####
This method allows to retrieve all test suites stored in selected project. You can you limit and offset params to paginate.

```python
from qaseio.client.models import TestSuiteFilters

test_suites = qase.suites.get_all(
    "PRJCODE", filters=TestSuiteFilters(search="query")
)
```

#### Get a specific test suite ####
This method allows to retrieve a specific test suite.

```python
test_suite = qase.suites.get("PRJCODE", 123)
```

#### Check test suite exists ####

```python
exists = qase.suites.exists("PRJCODE", 123)
```

#### Create a new test suite ####
This method is used to create a new test plan through API.

```python
from qaseio.client.models import TestSuiteCreate

test_suite = qase.suites.create(
    "PRJCODE",
    TestSuiteCreate("New test suite"),
)
```

#### Update test suite ####
This method is used to update existing test suite through API.

```python
from qaseio.client.models import TestSuiteUpdate

test_suite = qase.suites.update(
    "PRJCODE",
    123,
    TestSuiteUpdate("Updated suite"),
)
```

#### Delete test suite ####
This method completely deletes a test suite from repository.

```python
qase.suites.delete("PRJCODE", 123)
```

### Test plans ###

#### Get all test plans ####
This method allows to retrieve all test plans stored in selected project. You can you limit and offset params to paginate.

```python
test_plans = qase.plans.get_all("PRJCODE")
```

#### Get a specific test plan ####
This method allows to retrieve a specific test plan.

```python
test_plan = qase.plans.get("PRJCODE", 123)
```

#### Check test plan exists ####

```python
exists = qase.plans.exists("PRJCODE", 123)
```

#### Create a new test plan ####
This method is used to create a new test plan through API.

```python
from qaseio.client.models import TestPlanCreate

test_plan = qase.plans.create(
    "PRJCODE",
    TestPlanCreate("New test run", [1, 2, 3]),
)
```

#### Update test plan ####
This method is used to update existing test plan through API.

```python
from qaseio.client.models import TestPlanCreate

test_plan = qase.plans.update(
    "PRJCODE",
    123,
    TestPlanCreate("New test run", [1, 2, 3]),
)
```

#### Delete test plan ####
This method completely deletes a test plan from repository.

```python
qase.plans.delete("PRJCODE", 123)
```

### Test runs ###

#### Get all test runs ####
This method allows to retrieve all test runs stored in selected project. You can you limit and offset params to paginate.

```python
from qaseio.client.models import TestRunInclude
test_runs = qase.runs.get_all("PRJCODE", include=TestRunInclude.CASES)
```

#### Get a specific test run ####
This method allows to retrieve a specific test run.

```python
test_run = qase.runs.get("PRJCODE", 4)
```

#### Check test run exists ####

```python
exists = qase.runs.exists("PRJCODE", 4)
```

#### Create a new test run ####
This method is used to create a new test run through API.

```python
from qaseio.client.models import TestRunCreate

test_run = qase.runs.create(
    "PRJCODE",
    TestRunCreate("Test run", [1, 2, 3]),
)
```

#### Delete test run ####
This method completely deletes a test run from repository.

```python
qase.runs.delete("PRJCODE", 4)
```

### Test run results ###

#### Get all test run results ####
This method allows to retrieve all test run results stored in selected project. You can you limit and offset params to paginate.

```python
test_run_results = qase.results.get_all("PRJCODE")
```

#### Get a specific test run result ####
This method allows to retrieve a specific test run result.

```python
test_run_result = qase.results.get("PRJCODE", "2898ba7f3b4d857cec8bee4a852cdc85f8b33132")
```

#### Create a new test run result ####
This method is used to create a new test run result through API.

```python
from qaseio.client.models import TestRunResultCreate, TestRunResultStatus

test_run_result = qase.results.create(
    "PRJCODE",
    4,
    TestRunResultCreate(123, TestRunResultStatus.PASSED),
)
```

#### Update test run result ####
This method is used to update existing test run result through API.

```python
from qaseio.client.models import TestRunResultUpdate, TestRunResultStatus

test_run_result = qase.results.update(
    "PRJCODE",
    4,
    "2898ba7f3b4d857cec8bee4a852cdc85f8b33132",
    TestRunResultUpdate(TestRunResultStatus.PASSED),
)
```

#### Delete test run result ####
This method completely deletes a test run result from repository.

```python
qase.results.delete("PRJCODE", 4, "2898ba7f3b4d857cec8bee4a852cdc85f8b33132")
```

# Contribution

Install project locally:

```bash
python3 -m venv .venv
source .venv/bin/activate
python setup.py develop
```

Install dev requirements:

```bash
pip install pre-commit
pre-commit install
```

Test project:

```bash
tox
```
