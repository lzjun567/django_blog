{% extends '_layout.swig' %}

{% block title %} {{ config.title }} {% endblock %}

{% block page_class %}
  {% if is_home %} page-home {% endif %}
{% endblock %}

{% block content %}
  <section id="posts" class="posts-expand">
    {% for post in page.posts %}

    {% endfor %}
  </section>

  {% include '_partials/pagination.swig' %}
{% endblock %}

{% block sidebar %}
{% endblock %}
