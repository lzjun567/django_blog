采用Django+Bootstrap开发的个人博客
===============
Django_Blog是一个基于Django、Bootstrap开发的个人极简博客应用，响应式设计，仅支持markdown格式WYSIWYG(所见即所得)的编辑方式。
####开发哲学
简约原则，开源精神
####项目结构

    ├─django_blog
    │  ├─libs
    │  └─settings
    ├─requirements
    ├─templates
    │  └─admin
    │      └─blog
    └─apps
        ├─blog
        │  ├─templates
        │  ├─static
        │  │  ├─css
        │  │  ├─js
        │  │  └─fonts
        │  ├─templatetags
        │  └─migrations
        └─bootstrap_pagination
            ├─templates
            │  └─bootstrap_pagination
            └─templatetags

####安装运行

    git clone https://github.com/lzjun567/django_blog.git
    cd django_blog
    pip install -r requirements/dev.txt
    python manage.py syncdb
    python manage.py runserver localhost:8000


任何建议或者参与开发，可以[New Issue](https://github.com/lzjun567/django_blog/issues)。项目遵循[Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)协议  
from opensource to opensource
####Requirements
* Python >=2.6
* pip >=0.8
* django >=1.6
* South==0.8.4
* MySQL-python
* django-reversion
* markdown2
* django-pagedown (https://github.com/timmyomahony/django-pagedown)

Optional:

* gunicorn (https://github.com/benoitc/gunicorn)

####License

This project is licensed under the terms of the MIT License describe below.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


