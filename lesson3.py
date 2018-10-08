from pymonad import curry


# 3.1
@curry
def tag(html_tag, value):
    return '<{0}>{1}</{0}>'.format(html_tag, value)


bold = tag('b')
italic = tag('i')
li = tag('li')

print(bold('string'))
print(italic('string'))
print(li('string'))


bold_italic = bold() * italic()
print(bold_italic('string'))


# 3.2
@curry
def tag(html_tag, attr, value):
    return '<{0} {1}>{2}</{0}>'.format(
        html_tag,
        ' '.join([elem[0] + '=' + elem[1] for elem in attr.items()]),
        value
    )


dict_a = {'class': 'list-group', 'id': 'li'}
print(tag('li', dict_a, 'item 23'))
print(tag('li', {'class': 'list-group'}, 'item 23'))
