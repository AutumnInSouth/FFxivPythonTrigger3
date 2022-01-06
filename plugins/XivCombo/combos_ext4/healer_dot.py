from ..combos import combo_func
from FFxivPythonTrigger import plugins


def target_has_dot(me_id, dots):
    t = plugins.XivMemory.targets.current
    if t:
        effects = t.effects.get_dict(source=me_id)
        for dot in dots:
            if dot in effects:
                return effects[dot].timer
    return 0


whm_dot = {1871, 144, 143}


@combo_func(16532, "whm/dot", "天辉替换gcd")
def whm(me):
    return 121 if me.level >= 2 and target_has_dot(me.id, whm_dot) < 2.5 else 119


sch_dot = {1895, 189, 179}


@combo_func(16540, "sch/dot", "蛊毒法替换gcd")
def sch(me):
    return 17864 if me.level >= 2 and target_has_dot(me.id, sch_dot) < 2.5 else 17869


ast_dot = {838, 843, 1881}


@combo_func(16554, "ast/dot", "焚灼替换gcd")
def ast(me):
    return 16554 if me.level >= 4 and target_has_dot(me.id, ast_dot) < 2.5 else 3596


sge_dot = {2614, 2615, 2616}


@combo_func(24290, "sge/dot", "Eukrasian Dosis III 替换 gcd")
def sge(me):
    return 24283 if me.level < 30 or target_has_dot(me.id, sge_dot) < 2.5 and not me.effects.has(2606) else 24290


combos = [whm, sch, ast, sge]
