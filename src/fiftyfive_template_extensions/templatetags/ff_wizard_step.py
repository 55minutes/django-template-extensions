import lxml.html

from django import template

register = template.Library()


def _parse_prefix(parser, prefix):
    if prefix[0] == prefix[-1] and prefix[0] in ('"', "'"):
        prefix = prefix[1:-1]
    try:
        return parser.compile_filter(prefix)
    except:
        return prefix


def _process_token(parser, token):
    tag_name, my_step, current_step, before_prefix, my_prefix, after_prefix = \
            token.split_contents()
    my_step = parser.compile_filter(my_step)
    current_step = parser.compile_filter(current_step)
    before_prefix, my_prefix, after_prefix = map(
        _parse_prefix, [parser]*3, (before_prefix, my_prefix, after_prefix))
    return my_step, current_step, before_prefix, my_prefix, after_prefix


def _resolve(var, context):
    try:
        return var.resolve(context)
    except:
        return var


def _prefix_content(prefix, content):
    if prefix:
        output = u'%s%s' % (prefix, content)
        if prefix[0] == '<' and prefix[-1] == '>':
            output = lxml.html.tostring(lxml.html.fromstring(output))
    else:
        output = content
    return output


@register.tag(name='wizardstep')
def wizard_step(parser, token):
    """
    A tag used to render each step of the breadcrumb for a wizard.
    {% wizardstep my_step current_step before_my_step_prefix my_step_prefix
    after_mystep_prefix %}step_label{% endwizardstep %}
    """
    my_step, current_step, before_prefix, my_prefix, after_prefix = \
            _process_token(parser, token)
    nodelist = parser.parse(('endwizardstep',))
    parser.delete_first_token()
    return StepNode(my_step, current_step, before_prefix, my_prefix,
                    after_prefix, nodelist)


class StepNode(template.Node):

    def __init__(self, my_step, current_step, before_prefix, my_prefix,
                 after_prefix, nodelist):
        self.my_step = my_step
        self.current_step = current_step
        self.before_prefix = before_prefix
        self.my_prefix = my_prefix
        self.after_prefix = after_prefix
        self.nodelist = nodelist

    def render(self, context):
        my_step, current_step, before_prefix, my_prefix, after_prefix = \
                map(_resolve, (self.my_step, self.current_step,
                               self.before_prefix, self.my_prefix,
                               self.after_prefix), [context] * 5)

        content = self.nodelist.render(context)
        if current_step < my_step:
            output = _prefix_content(before_prefix, content)
        elif current_step == my_step:
            output = _prefix_content(my_prefix, content)
        else:
            output = _prefix_content(after_prefix, content)
        return output
