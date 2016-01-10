Templater
=========

# How to use
```
<html>
    <head>
        <title>{{ title }}</title>
    </head>
    <body>
        {% if user %}
            Hi {{ user.name }}!
        {% else %}
            <a href="{{ path("login") }}">Click here to login</a>
        {% end if %}
        <ul>
            {% for item in m_list %}
                <li>{{ item }}</li>
            {% end for %}
        </ul>
    </body>
</html>
```

# Tags

## Echo / Print
```
{{ var_name }}
```

## If / Elif / Else
```
{% if expression %}
    ...
{% elif expression %}
    ...
{% else %}
    ...
{% end if %}
```

## For loop
```
{% for value in list %}
    ...
{% end for %}
```
