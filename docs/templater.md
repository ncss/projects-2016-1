Templater
=========

## Example python usage
```
import templater
user = User("Tim") if user_logged_in else None
templater.render("templates/dashboard.html", user=user, your_lists_count=42)
```

## Example template file
```
<html>
    <head>
        <title>{{ title }}</title>
    </head>
    <body>
        {% if user %}
            Hi {{ user.name }}!
        {% else %}
            <a href="{{ login_path }}">Click here to login</a>
        {% end if %}
        <ul>
            {% for item in m_list %}
                <li>{{ item }}</li>
            {% end for %}
        </ul>
    </body>
</html>
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
{% for value in list %}
    ...
{% end for %}
```
