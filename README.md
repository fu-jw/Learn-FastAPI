# Learn-FastAPI
记录**FastAPI**的学习笔记

[文档链接](https://fastapi.tiangolo.com/zh/learn/)
## 类型提示
不要如下写法：
```python
def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_full_name("john", "doe"))
```
修改成：
```python
def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_full_name("john", "doe"))
```
是添加参数类型，不是声明默认值
```python
    first_name="john", last_name="doe"
```
