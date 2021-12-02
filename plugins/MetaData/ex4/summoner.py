from ..base import ActionBase, StatusBase, physic, magic


class Actions:

    class Ruin(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：180

        """
        id = 163
        name = {'Ruin', '毁灭'}

    class Bio(ActionBase):
        """
        对目标附加无属性持续伤害状态 威力：20 持续时间：30秒

        179, 毒菌, Bio, 体力逐渐减少
        """
        id = 164
        name = {'Bio', '毒菌'}

    class Summon(ActionBase):
        """
        召唤擅长远程范围攻击的召唤兽 与(source.job==27?召唤II、召唤III:召唤II)共享复唱时间

        """
        id = 165
        name = {'Summon', '召唤'}

    class Miasma(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：20 追加效果：无属性持续伤害 威力：20 持续时间：30秒

        180, 瘴气, Miasma, 体力逐渐减少
        """
        id = 168
        name = {'Miasma', '瘴气'}

    class SummonIi(ActionBase):
        """
        召唤擅长辅助召唤师的召唤兽 与(source.job==27?召唤、召唤III:召唤)共享复唱时间

        """
        id = 170
        name = {'Summon II', '召唤II'}

    class RuinIi(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：160

        """
        id = 172
        name = {'Ruin II', '毁坏'}

    class Bane(ActionBase):
        """
        令目标所带的毒菌、瘴气系持续伤害状态向周围扩散 对目标之外的敌人威力降低60% (source.job==27?(source.level>=78?追加效果（发动几率100%）：令各状态以原本持续时间扩散 :持续时间：扩散时各状态的剩余持续时间 追加效果（发动几率15%）：令各状态以原本持续时间扩散 ):持续时间：扩散时各状态的剩余持续时间 追加效果（发动几率15%）：令各状态以原本持续时间扩散 )自身没有对目标施加毒菌、瘴气系持续伤害状态时无效 

        """
        id = 174
        name = {'Bane', '灾祸'}

    class BioIi(ActionBase):
        """
        对目标附加无属性持续伤害状态 威力：30 持续时间：30秒

        189, 猛毒菌, Bio II, 体力逐渐减少
        """
        id = 178
        name = {'Bio II', '猛毒菌'}

    class SummonIii(ActionBase):
        """
        召唤擅长近身单体攻击的召唤兽 与召唤、召唤II共享复唱时间

        """
        id = 180
        name = {'Summon III', '召唤III'}

    class Fester(ActionBase):
        """
        对目标发动无属性魔法攻击 该技能威力随自身在目标身上附加的毒菌、瘴气系持续伤害状态数量而变化 无持续伤害时威力：100 1种持续伤害时威力：200 2种持续伤害时威力：300 发动条件：以太超流

        """
        id = 181
        name = {'Fester', '溃烂爆发'}

    class Enkindle(ActionBase):
        """
        令当前同行的召唤兽发动其最强技能 发动条件：自身处于战斗状态且召唤兽处于同行状态

        """
        id = 184
        name = {'Enkindle', '内力迸发'}

    class Gouge(ActionBase):
        """
        对目标发动土属性魔法攻击 威力：40 ※该技能无法设置到热键栏

        """
        id = 633
        name = {'Gouge', '利爪'}

    class ShiningTopaz(ActionBase):
        """
        对自身周围的敌人发动土属性范围魔法攻击 威力：200 ※该技能无法设置到热键栏

        """
        id = 634
        name = {'Shining Topaz', '黄宝石之光'}

    class Gust(ActionBase):
        """
        对目标及其周围敌人发动风属性范围魔法攻击 威力：20 ※该技能无法设置到热键栏

        """
        id = 637
        name = {'Gust', '突风'}

    class Downburst(ActionBase):
        """
        对目标及其周围敌人发动风属性范围魔法攻击 威力：100 ※该技能无法设置到热键栏

        """
        id = 639
        name = {'Downburst', '下行突风'}

    class RockBuster(ActionBase):
        """
        对目标发动土属性魔法攻击 威力：60 ※该技能无法设置到热键栏

        """
        id = 787
        name = {'Rock Buster', '碎岩'}

    class MountainBuster(ActionBase):
        """
        对自身周围的敌人发动土属性范围魔法攻击 威力：250 ※该技能无法设置到热键栏

        """
        id = 788
        name = {'Mountain Buster', '山崩'}

    class EarthenFury(ActionBase):
        """
        对自身周围的敌人发动范围土属性魔法攻击 威力：300 追加效果：生成范围伤害区域 威力：20 持续时间：15秒 ※该技能无法设置到热键栏

        312, 大地之怒, Razed Earth, 产生土属性攻击区域
        """
        id = 791
        name = {'Earthen Fury', '大地之怒'}

    class WindBlade(ActionBase):
        """
        对目标及其周围敌人发动风属性范围魔法攻击 威力：30 ※该技能无法设置到热键栏

        """
        id = 792
        name = {'Wind Blade', '烈风刃'}

    class AerialSlash(ActionBase):
        """
        对目标及其周围敌人发动风属性范围魔法攻击 威力：150 ※该技能无法设置到热键栏

        """
        id = 794
        name = {'Aerial Slash', '大气风斩'}

    class AerialBlast(ActionBase):
        """
        对目标及其周围敌人发动风属性范围魔法攻击 威力：350 ※该技能无法设置到热键栏

        """
        id = 796
        name = {'Aerial Blast', '大气爆发'}

    class CrimsonCyclone(ActionBase):
        """
        对目标发动火属性魔法攻击 威力：250 ※该技能无法设置到热键栏

        """
        id = 797
        name = {'Crimson Cyclone', '深红旋风'}

    class BurningStrike(ActionBase):
        """
        对目标发动火属性魔法攻击 威力：80 ※该技能无法设置到热键栏

        """
        id = 798
        name = {'Burning Strike', '燃火强袭'}

    class FlamingCrush(ActionBase):
        """
        对自身周围的敌人发动火属性范围魔法攻击 威力：250 攻击复数敌人时，对目标之外的敌人威力降低50% ※该技能无法设置到热键栏

        """
        id = 800
        name = {'Flaming Crush', '烈焰碎击'}

    class Inferno(ActionBase):
        """
        向目标所在方向发出火属性扇形范围魔法攻击 威力：300 追加效果：火属性持续伤害 威力：20 持续时间：15秒 ※该技能无法设置到热键栏

        314, 地狱之火炎, Inferno, 火属性持续伤害，体力逐渐流失
        """
        id = 801
        name = {'Inferno', '地狱之火炎'}

    class Painflare(ActionBase):
        """
        对目标及其周围敌人发动无属性范围魔法攻击 威力：130 发动条件：以太超流

        """
        id = 3578
        name = {'Painflare', '痛苦核爆'}

    class RuinIii(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：200

        """
        id = 3579
        name = {'Ruin III', '毁荡'}

    class Tri-disaster(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：150 追加效果：对目标同时施放(source.level>=66?(source.job==27?剧毒菌和瘴暍:猛毒菌和瘴气):猛毒菌和瘴气) 持续时间：各魔法单独施放时的持续时间

        """
        id = 3580
        name = {'Tri-disaster', '三重灾祸'}

    class DreadwyrmTrance(ActionBase):
        """
        一定时间内，自身的魔法咏唱时间缩短2.5秒 持续时间：15秒 (source.level>=70?(source.job==27?持续时间结束后获得附体深度 :):)追加效果：发动时重置三重灾祸的复唱时间(source.level>=70?(source.job==27? 发动条件：自身处于战斗状态且亚灵神巴哈姆特不处于显现状态，附身深度不满2档: 发动条件：自身处于战斗状态): 发动条件：自身处于战斗状态)(source.job==27?(source.level>=72? 与不死鸟附体共享复唱时间:):)

        808, 龙神附体, Dreadwyrm Trance, 得到了龙神巴哈姆特之力，魔法所造成的伤害提高
        """
        id = 3581
        name = {'Dreadwyrm Trance', '龙神附体'}

    class Deathflare(ActionBase):
        """
        对目标及其周围敌人发动无属性范围魔法攻击 威力：400 攻击复数敌人时，对目标之外的敌人威力降低50% 发动后会取消龙神附体状态 发动条件：龙神附体状态中

        """
        id = 3582
        name = {'Deathflare', '死星核爆'}

    class Aetherpact(ActionBase):
        """
        命令召唤兽发动灵护 为召唤兽周围的队员附加灵护状态 灵护效果：攻击造成的伤害提高5% 持续时间：15秒 发动条件：召唤兽处于同行状态

        """
        id = 7423
        name = {'Aetherpact', '以太契约'}

    class BioIii(ActionBase):
        """
        对目标附加无属性持续伤害状态 威力：45 持续时间：30秒

        1214, 剧毒菌, Bio III, 体力逐渐减少
        1326, 剧毒菌, Bio III, 受到持续伤害
        """
        id = 7424
        name = {'Bio III', '剧毒菌'}

    class MiasmaIii(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：45 追加效果：无属性持续伤害 威力：45 持续时间：30秒

        1215, 瘴暍, Miasma III, 体力逐渐减少
        1327, 瘴暍, Miasma III, 受到持续伤害，同时自身所受的体力恢复效果降低
        """
        id = 7425
        name = {'Miasma III', '瘴暍'}

    class RuinIv(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：300 发动条件：毁坏强化状态中 ※该技能无法设置到热键栏

        """
        id = 7426
        name = {'Ruin IV', '毁绝'}

    class SummonBahamut(ActionBase):
        """
        令亚灵神巴哈姆特显现 显现时间：20秒 当召唤者使用魔法攻击目标时，亚灵神巴哈姆特会发动真龙波 亚灵神巴哈姆特显现时，之前召唤出的召唤兽会被暂时回收，并在显现时间结束后再次出现 发动条件：召唤兽处于同行状态，且附体深度为2档 龙神附体状态中无法发动

        """
        id = 7427
        name = {'Summon Bahamut', '龙神召唤'}

    class Wyrmwave(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：150 发动条件：亚灵神巴哈姆特显现中 ※该技能无法设置到热键栏

        """
        id = 7428
        name = {'Wyrmwave', '真龙波'}

    class EnkindleBahamut(ActionBase):
        """
        命令显现的亚灵神巴哈姆特发动死亡轮回 对目标及其周围敌人发动无属性范围魔法攻击 威力：650 攻击复数敌人时，对目标之外的敌人威力降低50% 发动条件：亚灵神巴哈姆特显现中(source.job==27?(source.level>=80? 与不死鸟迸发共享复唱时间:):)

        """
        id = 7429
        name = {'Enkindle Bahamut', '龙神迸发'}

    class AkhMorn(ActionBase):
        """
        对目标及其周围敌人发动无属性范围魔法攻击 威力：650 攻击复数敌人时，对目标之外的敌人威力降低50% 发动条件：亚灵神巴哈姆特显现中 ※该技能无法设置到热键栏

        """
        id = 7449
        name = {'Akh Morn', '死亡轮回'}

    class Devotion(ActionBase):
        """
        为召唤兽周围的队员附加灵护状态 灵护效果：攻击造成的伤害提高5% 持续时间：15秒 ※该技能无法设置到热键栏

        1213, 灵护, Devotion, 攻击所造成的伤害提高
        """
        id = 7450
        name = {'Devotion', '灵护'}

    class Physick(ActionBase):
        """
        恢复目标的体力 恢复力：400

        """
        id = 16230
        name = {'Physick', '医术'}

    class EnergyDrain(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：100 追加效果：2档以太超流(source.job==27?(source.level>=35? 与能量抽取共享复唱时间:):)

        """
        id = 16508
        name = {'Energy Drain', '能量吸收'}

    class EgiAssault(ActionBase):
        """
        令当前同行的召唤兽发动灵攻I对应的技能 积蓄次数：2 发动条件：自身处于战斗状态且召唤兽处于同行状态 该魔法有单独计算的复唱时间

        """
        id = 16509
        name = {'Egi Assault', '灵攻I'}

    class EnergySiphon(ActionBase):
        """
        对目标及其周围的敌人发动无属性范围魔法攻击 威力：40 追加效果：2档以太超流 与能量吸收共享复唱时间

        """
        id = 16510
        name = {'Energy Siphon', '能量抽取'}

    class Outburst(ActionBase):
        """
        对目标及其周围的敌人发动无属性范围魔法攻击 威力：(source.job==27?(source.level>=76?90:70):70)

        """
        id = 16511
        name = {'Outburst', '迸裂'}

    class EgiAssaultIi(ActionBase):
        """
        令当前同行的召唤兽发动灵攻II对应的技能 积蓄次数：2 发动条件：自身处于战斗状态且召唤兽处于同行状态 该魔法有单独计算的复唱时间

        """
        id = 16512
        name = {'Egi Assault II', '灵攻II'}

    class FirebirdTrance(ActionBase):
        """
        一定时间内，自身的魔法咏唱时间缩短2.5秒 同时，毁荡和迸裂会分别变为灵泉之炎和炼狱之炎 持续时间：20秒 追加效果：发动时重置三重灾祸的复唱时间 发动条件：亚灵神巴哈姆特显现结束 满足发动条件后，龙神附体会变为不死鸟附体 与龙神附体共享复唱时间 ※该技能无法设置到热键栏

        """
        id = 16513
        name = {'Firebird Trance', '不死鸟附体'}

    class FountainOfFire(ActionBase):
        """
        对目标发动火属性魔法攻击 威力：250 追加效果：灵泉 持续时间：10秒 发动条件：不死鸟附体状态中 ※该技能无法设置到热键栏

        2029, 灵泉之炎, Fountain of Fire, 受到持续伤害
        """
        id = 16514
        name = {'Fountain of Fire', '灵泉之炎'}

    class BrandOfPurgatory(ActionBase):
        """
        对目标及其周围的敌人发动火属性范围魔法攻击 威力：350 攻击复数敌人时，对目标之外的敌人威力降低50% 发动条件：不死鸟附体及灵泉状态中 ※该技能无法设置到热键栏

        """
        id = 16515
        name = {'Brand of Purgatory', '炼狱之炎'}

    class EnkindlePhoenix(ActionBase):
        """
        命令显现的亚灵神不死鸟发动天启 对目标及其周围的敌人发动火属性范围魔法攻击 威力：650 攻击复数敌人时，对目标之外的敌人威力降低50% 发动条件：亚灵神不死鸟显现中 满足发动条件后，龙神迸发变为不死鸟迸发 与龙神迸发共享复唱时间 ※该技能无法设置到热键栏

        """
        id = 16516
        name = {'Enkindle Phoenix', '不死鸟迸发'}

    class EverlastingFlight(ActionBase):
        """
        持续恢复周围队员的体力 恢复力：100 持续时间：21秒 ※该技能无法设置到热键栏

        1868, 不死鸟之翼, Everlasting Flight, 体力会随时间逐渐恢复
        2030, 不死鸟之翼, Everlasting Flight, 体力会随时间逐渐恢复
        """
        id = 16517
        name = {'Everlasting Flight', '不死鸟之翼'}

    class Revelation(ActionBase):
        """
        对目标及其周围的敌人发动火属性范围魔法攻击 威力：650 攻击复数敌人时，对目标之外的敌人威力降低50% 发动条件：亚灵神不死鸟显现中 ※该技能无法设置到热键栏

        """
        id = 16518
        name = {'Revelation', '天启'}

    class ScarletFlame(ActionBase):
        """
        对目标发动火属性魔法攻击 威力：150 发动条件：亚灵神不死鸟显现中 ※该技能无法设置到热键栏

        """
        id = 16519
        name = {'Scarlet Flame', '赤焰'}

    class GlitteringTopaz(ActionBase):
        """
        对召唤该召唤兽的召唤师附加能够抵御一定伤害的防护罩 该防护罩能够抵消相当于目标最大体力30%的伤害量 持续时间：30秒 ※该技能无法设置到热键栏

        """
        id = 16520
        name = {'Glittering Topaz', '黄宝石之辉'}

    class GlitteringEmerald(ActionBase):
        """
        对目标及其周围敌人发动风属性范围魔法攻击 威力：30 追加效果：以目标为中心产生伤害区域 威力：30 持续时间：9秒 ※该技能无法设置到热键栏

        """
        id = 16521
        name = {'Glittering Emerald', '绿宝石之辉'}

    class EarthenArmor(ActionBase):
        """
        对召唤该召唤兽的召唤师附加能够抵御一定伤害的防护罩 该防护罩能够抵消相当于目标最大体力30%的伤害量 持续时间：30秒 ※该技能无法设置到热键栏

        """
        id = 16522
        name = {'Earthen Armor', '大地之铠'}

    class Slipstream(ActionBase):
        """
        对目标及其周围敌人发动风属性范围魔法攻击 威力：50 追加效果：以目标为中心产生伤害区域 威力：50 持续时间：9秒 ※该技能无法设置到热键栏

        1869, 螺旋气流, Gale Enforcer, 产生风属性攻击区域
        """
        id = 16523
        name = {'Slipstream', '螺旋气流'}

    class FirebirdTrance(ActionBase):
        """
        一定时间内，自身的魔法咏唱时间缩短2.5秒 同时，毁荡和迸裂会分别变为灵泉之炎和炼狱之炎 令亚灵神不死鸟显现 显现时间：20秒 亚灵神不死鸟显现时会发动不死鸟之翼 当召唤者使用魔法攻击目标时，亚灵神不死鸟会发动赤焰 亚灵神不死鸟显现时，之前召唤出的召唤兽会被暂时回收，并在显现时间结束后再次出现 追加效果：发动时重置三重灾祸的复唱时间 发动条件：召唤兽处于同行状态，且亚灵神巴哈姆特显现结束 满足发动条件后，龙神附体会变为不死鸟附体 与龙神附体共享复唱时间 ※该技能无法设置到热键栏

        """
        id = 16549
        name = {'Firebird Trance', '不死鸟附体'}

    class AssaultIGlitteringTopaz(ActionBase):
        """
        令黄宝石兽发动黄宝石之辉 对召唤该召唤兽的召唤师附加能够抵御一定伤害的防护罩 该防护罩能够抵消相当于目标最大体力30%的伤害量 持续时间：30秒 积蓄次数：2 发动条件：自身处于战斗状态且黄宝石兽处于同行状态 该魔法有单独计算的复唱时间

        """
        id = 16791
        name = {'Assault I: Glittering Topaz', '灵攻I：黄宝石之辉'}

    class AssaultIiShiningTopaz(ActionBase):
        """
        令黄宝石兽发动黄宝石之光 对自身周围的敌人发动土属性范围魔法攻击 威力：200 积蓄次数：2 发动条件：自身处于战斗状态且黄宝石兽处于同行状态 该魔法有单独计算的复唱时间

        """
        id = 16792
        name = {'Assault II: Shining Topaz', '灵攻II：黄宝石之光'}

    class AssaultIDownburst(ActionBase):
        """
        令绿宝石兽发动下行突风 对目标及其周围敌人发动风属性范围魔法攻击 威力：100 积蓄次数：2 发动条件：自身处于战斗状态且绿宝石兽处于同行状态 该魔法有单独计算的复唱时间

        """
        id = 16793
        name = {'Assault I: Downburst', '灵攻I：下行突风'}

    class AssaultIiGlitteringEmerald(ActionBase):
        """
        令绿宝石兽发动绿宝石之辉 对目标及其周围敌人发动风属性范围魔法攻击 威力：30 追加效果：以目标为中心产生伤害区域 威力：30 持续时间：9秒 积蓄次数：2 发动条件：自身处于战斗状态且绿宝石兽处于同行状态 该魔法有单独计算的复唱时间

        """
        id = 16794
        name = {'Assault II: Glittering Emerald', '灵攻II：绿宝石之辉'}

    class AssaultIEarthenArmor(ActionBase):
        """
        令泰坦之灵发动大地之铠 对召唤该召唤兽的召唤师附加能够抵御一定伤害的防护罩 该防护罩能够抵消相当于目标最大体力30%的伤害量 持续时间：30秒 积蓄次数：2 发动条件：自身处于战斗状态且泰坦之灵处于同行状态 该魔法有单独计算的复唱时间

        """
        id = 16795
        name = {'Assault I: Earthen Armor', '灵攻I：大地之铠'}

    class AssaultIiMountainBuster(ActionBase):
        """
        令泰坦之灵发动山崩 对自身周围的敌人发动土属性范围魔法攻击 威力：250 积蓄次数：2 发动条件：自身处于战斗状态且泰坦之灵处于同行状态 该魔法有单独计算的复唱时间

        """
        id = 16796
        name = {'Assault II: Mountain Buster', '灵攻II：山崩'}

    class AssaultIAerialSlash(ActionBase):
        """
        令迦楼罗之灵发动大气风斩 对目标及其周围敌人发动风属性范围魔法攻击 威力：150 积蓄次数：2 发动条件：自身处于战斗状态且迦楼罗之灵处于同行状态 该魔法有单独计算的复唱时间

        """
        id = 16797
        name = {'Assault I: Aerial Slash', '灵攻I：大气风斩'}

    class AssaultIiSlipstream(ActionBase):
        """
        令迦楼罗之灵发动螺旋气流 对目标及其周围敌人发动风属性范围魔法攻击 威力：50 追加效果：以目标为中心产生伤害区域 威力：50 持续时间：9秒 积蓄次数：2 发动条件：自身处于战斗状态且迦楼罗之灵处于同行状态 该魔法有单独计算的复唱时间

        """
        id = 16798
        name = {'Assault II: Slipstream', '灵攻II：螺旋气流'}

    class AssaultICrimsonCyclone(ActionBase):
        """
        令伊弗利特之灵发动深红旋风 对目标发动火属性魔法攻击 威力：250 积蓄次数：2 发动条件：自身处于战斗状态且伊弗利特之灵处于同行状态 该魔法有单独计算的复唱时间

        """
        id = 16799
        name = {'Assault I: Crimson Cyclone', '灵攻I：深红旋风'}

    class AssaultIiFlamingCrush(ActionBase):
        """
        令伊弗利特之灵发动烈焰碎击 对自身周围的敌人发动火属性范围魔法攻击 威力：250 攻击复数敌人时，对目标之外的敌人威力降低50% 积蓄次数：2 发动条件：自身处于战斗状态且伊弗利特之灵处于同行状态 该魔法有单独计算的复唱时间

        """
        id = 16800
        name = {'Assault II: Flaming Crush', '灵攻II：烈焰碎击'}

    class EnkindleEarthenFury(ActionBase):
        """
        令泰坦之灵发动大地之怒 对自身周围的敌人发动范围土属性魔法攻击 威力：300 追加效果：生成范围伤害区域 威力：20 持续时间：15秒 发动条件：自身处于战斗状态且泰坦之灵处于同行状态

        """
        id = 16801
        name = {'Enkindle: Earthen Fury', '内力迸发：大地之怒'}

    class EnkindleAerialBlast(ActionBase):
        """
        令迦楼罗之灵发动大气爆发 对目标及其周围敌人发动风属性范围魔法攻击 威力：350 发动条件：自身处于战斗状态且迦楼罗之灵处于同行状态

        """
        id = 16802
        name = {'Enkindle: Aerial Blast', '内力迸发：大气爆发'}

    class EnkindleInferno(ActionBase):
        """
        令伊弗利特之灵发动地狱之火炎 向目标所在方向发出火属性扇形范围魔法攻击 威力：300 追加效果：火属性持续伤害 威力：20 持续时间：15秒 发动条件：自身处于战斗状态且伊弗利特之灵处于同行状态

        """
        id = 16803
        name = {'Enkindle: Inferno', '内力迸发：地狱之火炎'}
