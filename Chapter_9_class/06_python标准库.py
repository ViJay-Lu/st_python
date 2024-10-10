#OrderedDict的实际跟字典几乎相同，区别在于OrderedDict记录了插入顺序
from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages["vijay"] = "python"
favorite_languages["yoyo"] = "CPP"
favorite_languages["lilian"] = "JAVA"
favorite_languages["wangwu"] = "C#"

"""
Vijay's favorite language is python
Yoyo's favorite language is cpp
Lilian's favorite language is java
Wangwu's favorite language is c#
"""
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.lower())

