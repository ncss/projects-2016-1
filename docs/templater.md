Templater
=========

## Example python usage
```python
import templater
user = User("Tim Dawborn", "tim@ncss.edu.au")
templater.render("templates/listview.html", user=user,
                 movie_list=["Aladdin", "Finding Nemo"])
```

## Example template file

**index.html**:

```html
{% include templates/header.html %}
{% if user %}
    Hi {{ user.name }}!
{% else %}
    <a href="/login">Click here to login</a>
{% end if %}
<ul>
    {% for item in movie_list %}
        <li>{{ item }}</li>
    {% end for %}
</ul>
</body>
</html>
```

**header.html**:

```html
<html>
    <head>
        <title>{{ user.name }}'s Movie List</title>
    </head>
    <body>
```

## Tags

### Echo / Print
```
{{ var_name }}
```

### Include
```
{% include templates/header.html %}
```

### If / Else
```
{% if expression %}
    ...
{% else %}
    ...
{% end if %}
```

### For loop
```
{% for value in movie_list %}
    ...
{% end for %}
```
