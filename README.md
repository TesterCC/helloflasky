# helloflasky
## About Project
### It's a practice demo according to dog book 2ed edition, wolf book 1st edition and basic flask demo.

---

## Environment
* Python 3.6 + Flask 1.0.2 + 3rd-party libs, etc.


#### About python 3.6 run flask error in PyCharm on MacOS.

[Click will abort further execution because Python 3 was configured to use ASCII as encoding for the environment](https://stackoverflow.com/questions/36651680/click-will-abort-further-execution-because-python-3-was-configured-to-use-ascii)

PyCharm -> Edit Configurations -> Add Global variable -> Apply
```shell
LC_ALL    zh_CN.UTF-8
LANG      zh_CN.UTF-8
```

in shell
```shell
export LC_ALL="zh_CN.UTF-8"
export LANG="zh_CN.UTF-8"
```
#### if you local/user dir had dir named ".env", it will cause python-dotenv error, rename the dir ".env"

## About Launch 
#### Use ".env" or ".flaskenv" launch flask app
```python
flask run
```