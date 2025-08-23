## Virtual Environment Creation Guide

### 1. Create Virtual Environment

```bash
uv venv <env-name>
````

* Creates a virtual environment with the specified name.
* Example:

```bash
uv venv nutrienv
```

* Automatically installs the required Python version if missing.


### 2. Add Dependency

```bash
uv add <package-name>
```

* Installs the package in the virtual environment **and** adds it to project dependencies.
* Example:

```bash
uv add requests
```



### 3. Sync Environment

```bash
uv sync
```

* Synchronizes the environment with the lockfile (`uv.lock`):

  * Installs missing packages
  * Removes unused packages
  * Creates virtual environment if missing
* Options:

  * `--locked` → ensure lockfile is up-to-date
  * `--frozen` → use lockfile as-is without modification



### Notes

* Use `uv install <package>` **only for temporary installs**, it does **not** add to project dependencies.
* `uv add` is preferred for packages meant to be part of the project.
* Virtual environments can have any name, e.g., `nutrienv`, `dev-env`, `test-env`.
