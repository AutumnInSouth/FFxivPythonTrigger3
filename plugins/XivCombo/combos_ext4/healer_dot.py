from ..combos import combo_func
from FFxivPythonTrigger import plugins


def target_has_dot(me_id, dots):
    t=plugins.XivMemory.targets.current
    if t:
        effects = t.effects.get_dict(source=me_id)
        for dot in dots:
            if dot in effects:
                return effects[dot].timer
    return 0


whm_dot = {1871, 144, 143}


@combo_func(16532, "whm/dot", "天辉替换gcd")
def whm(me):
    return 121 if target_has_dot(me.id, whm_dot) < 2.5 else 119


combos = [whm]
