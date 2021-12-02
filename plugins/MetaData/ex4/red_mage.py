from ..base import ActionBase, StatusBase, physic, magic


class Actions:

    class Jolt(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：180 追加效果：获得3点黑魔元与3点白魔元

        """
        id = 7503
        name = {'Jolt', '摇荡'}

    class Riposte(ActionBase):
        """
        对目标发动物理攻击 威力：130(source.level>=2?(source.job==35? 平衡量谱中黑魔元与白魔元都在30点以上时，该技能变为魔回刺:):)

        """
        id = 7504
        name = {'Riposte', '回刺'}

    class Verthunder(ActionBase):
        """
        对目标发动雷属性魔法攻击 威力：(source.job==35?(source.level>=62?370:310):310) 追加效果：获得11点黑魔元(source.level>=26?(source.job==35? 追加效果（发动几率50%）：赤火炎预备 持续时间：30秒:):)

        """
        id = 7505
        name = {'Verthunder', '赤闪雷'}

    class Corps-a-corps(ActionBase):
        """
        冲向目标并发动物理攻击 威力：130 止步状态下无法发动

        2012, 短兵相接, Corps-a-corps, 抵消一定伤害
        """
        id = 7506
        name = {'Corps-a-corps', '短兵相接'}

    class Veraero(ActionBase):
        """
        对目标发动风属性魔法攻击 威力：(source.job==35?(source.level>=62?370:310):310) 追加效果：获得11点白魔元(source.level>=30?(source.job==35? 追加效果（发动几率50%）：赤飞石预备 持续时间：30秒:):)

        """
        id = 7507
        name = {'Veraero', '赤疾风'}

    class Scatter(ActionBase):
        """
        对目标及其周围的敌人发动无属性范围魔法攻击 威力：120 追加效果：获得3点黑魔元与3点白魔元

        """
        id = 7509
        name = {'Scatter', '散碎'}

    class Verfire(ActionBase):
        """
        对目标发动火属性魔法攻击 威力：(source.job==35?(source.level>=62?310:270):270) 追加效果：获得9点黑魔元 发动条件：赤火炎预备状态中

        """
        id = 7510
        name = {'Verfire', '赤火炎'}

    class Verstone(ActionBase):
        """
        对目标发动土属性魔法攻击 威力：(source.job==35?(source.level>=62?310:270):270) 追加效果：获得9点白魔元 发动条件：赤飞石预备状态中

        """
        id = 7511
        name = {'Verstone', '赤飞石'}

    class Zwerchhau(ActionBase):
        """
        对目标发动物理攻击 威力：100 连击条件：回刺或魔回刺 连击中威力：150 平衡量谱中黑魔元与白魔元都在25点以上时，该技能变为魔交击斩

        """
        id = 7512
        name = {'Zwerchhau', '交击斩'}
        combo_action = 7504

    class Moulinet(ActionBase):
        """
        向目标所在方向发出扇形范围物理攻击 威力：60 平衡量谱中黑魔元与白魔元都在20点以上时，该技能变为魔划圆斩

        """
        id = 7513
        name = {'Moulinet', '划圆斩'}

    class Vercure(ActionBase):
        """
        恢复目标的体力 恢复力：350

        """
        id = 7514
        name = {'Vercure', '赤治疗'}

    class Displacement(ActionBase):
        """
        对目标发动物理攻击 威力：(source.job==35?(source.level>=72?200:130):130) 追加效果：后跳15米距离 止步状态下无法发动(source.job==35?(source.level>=72? 与交剑共享复唱时间:):)

        2013, 移转, Displacement, 自身发动的下一个魔法造成的伤害提高
        """
        id = 7515
        name = {'Displacement', '移转'}

    class Redoublement(ActionBase):
        """
        对目标发动物理攻击 威力：100 连击条件：交击斩或魔交击斩 连击中威力：230 平衡量谱中黑魔元与白魔元都在25点以上时，该技能变为魔连攻

        """
        id = 7516
        name = {'Redoublement', '连攻'}
        combo_action = 7512

    class Fleche(ActionBase):
        """
        对目标发动物理攻击 威力：440

        """
        id = 7517
        name = {'Fleche', '飞刺'}

    class Acceleration(ActionBase):
        """
        一定时间内，前3次能附加赤火炎预备状态与赤飞石预备状态的技能追加效果发动率变为100% 持续时间：20秒

        1238, 促进, Acceleration, 发动附加赤火炎预备或赤飞石预备的魔法时必定发动追加效果
        """
        id = 7518
        name = {'Acceleration', '促进'}

    class ContreSixte(ActionBase):
        """
        对目标及其周围敌人发动范围物理攻击 威力：400

        """
        id = 7519
        name = {'Contre Sixte', '六分反击'}

    class Embolden(ActionBase):
        """
        一定时间内，自身发动魔法攻击造成的伤害提高10% 持续时间：20秒 此效果每4秒降低2% 追加效果：令周围队员发动物理攻击造成的伤害提高10% 持续时间：20秒 此效果每4秒降低2%

        1239, 鼓励, Embolden, 魔法攻击所造成的伤害提高
        1297, 鼓励, Embolden, 物理攻击所造成的伤害提高
        2282, 鼓励, Embolden, 攻击所造成的伤害提高
        """
        id = 7520
        name = {'Embolden', '鼓励'}

    class Manafication(ActionBase):
        """
        当前平衡量谱中积累的量值翻倍 追加效果：重置短兵相接和移转(source.job==35?(source.level>=72?以及交剑:):)的复唱时间(source.job==35?(source.level>=74? 追加效果：自身发动魔法攻击造成的伤害提高5% 持续时间：10秒:):) 此技能会中断连击

        1971, 倍增, Manafication, 魔法攻击所造成的伤害提高
        """
        id = 7521
        name = {'Manafication', '倍增'}

    class Verraise(ActionBase):
        """
        令无法战斗的目标以衰弱状态重新振作起来

        """
        id = 7523
        name = {'Verraise', '赤复活'}

    class JoltIi(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：290 追加效果：获得3点黑魔元与3点白魔元

        1498, 震荡, Shocked, 受到了强烈冲击，偶尔会无法行动，体力逐渐流失
        """
        id = 7524
        name = {'Jolt II', '震荡'}

    class Verflare(ActionBase):
        """
        对目标发动火属性魔法攻击 威力：600 连击条件：魔连攻 追加效果：获得21点黑魔元 追加效果（发动几率20%）：赤火炎预备 持续时间：30秒 发动时白魔元高于黑魔元则100%发动追加效果 发动条件：魔连攻成功时 若满足发动条件，则赤闪雷变为赤核爆 ※该技能无法设置到热键栏

        """
        id = 7525
        name = {'Verflare', '赤核爆'}
        combo_action = 7529

    class Verholy(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：600 连击条件：魔连攻 追加效果：获得21点白魔元 追加效果（发动几率20%）：赤飞石预备 持续时间：30秒 发动时黑魔元高于白魔元则100%发动追加效果 发动条件：魔连攻成功时 若满足发动条件，则赤疾风变为赤神圣 ※该技能无法设置到热键栏

        """
        id = 7526
        name = {'Verholy', '赤神圣'}
        combo_action = 7529

    class EnchantedRiposte(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：220 发动条件：黑魔元、白魔元各30点 ※该技能无法设置到热键栏

        """
        id = 7527
        name = {'Enchanted Riposte', '魔回刺'}

    class EnchantedZwerchhau(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：100 连击条件：回刺或魔回刺 连击中威力：290 发动条件：黑魔元、白魔元各25点 ※该技能无法设置到热键栏

        """
        id = 7528
        name = {'Enchanted Zwerchhau', '魔交击斩'}
        combo_action = 7504

    class EnchantedRedoublement(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：100 连击条件：魔交击斩 连击中威力：470 发动条件：黑魔元、白魔元各25点 ※该技能无法设置到热键栏

        """
        id = 7529
        name = {'Enchanted Redoublement', '魔连攻'}
        combo_action = 7512

    class EnchantedMoulinet(ActionBase):
        """
        向目标所在方向发出扇形范围魔法攻击 威力：200 发动条件：黑魔元、白魔元各20点 ※该技能无法设置到热键栏

        """
        id = 7530
        name = {'Enchanted Moulinet', '魔划圆斩'}

    class VerthunderIi(ActionBase):
        """
        对目标及其周围敌人发动雷属性魔法攻击 威力：(source.job==35?(source.level>=78?120:100):100) 追加效果：获得7点黑魔元

        """
        id = 16524
        name = {'Verthunder II', '赤震雷'}

    class VeraeroIi(ActionBase):
        """
        对目标及其周围敌人发动风属性魔法攻击 威力：(source.job==35?(source.level>=78?120:100):100) 追加效果：获得7点白魔元

        """
        id = 16525
        name = {'Veraero II', '赤烈风'}

    class Impact(ActionBase):
        """
        对目标及其周围敌人发动无属性范围魔法攻击 威力：220 追加效果：获得3点黑魔元与3点白魔元

        995, 冲击, Headache, 受到冲击，攻击所造成的伤害降低，积累档数过多会被附加脑震荡状态
        """
        id = 16526
        name = {'Impact', '冲击'}

    class Engagement(ActionBase):
        """
        对目标发动物理攻击 威力：150 与移转共享复唱时间

        2033, 交剑, Engagement, 抵消一定伤害
        """
        id = 16527
        name = {'Engagement', '交剑'}

    class EnchantedReprise(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：300 发动条件：黑魔元与白魔元各5点 ※该技能无法设置到热键栏

        """
        id = 16528
        name = {'Enchanted Reprise', '魔续斩'}

    class Reprise(ActionBase):
        """
        对目标发动物理攻击 威力：100 平衡量谱中黑魔元与白魔元都在5点以上时，该技能变为魔续斩

        """
        id = 16529
        name = {'Reprise', '续斩'}

    class Scorch(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：700 连击条件：赤核爆或赤神圣 追加效果：获得7点黑魔元与7点白魔元 发动条件：赤核爆或赤神圣成功时 满足发动条件后，震荡变为焦热 ※该技能无法设置到热键栏

        """
        id = 16530
        name = {'Scorch', '焦热'}
        combo_action = 7525
