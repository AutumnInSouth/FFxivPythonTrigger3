from ..base import ActionBase, StatusBase, physic, magic


class Actions:

    class Snort(ActionBase):
        """
        将自身前方扇形范围内的敌人击退20米

        """
        id = 11383
        name = {"Snort", "鼻息"}

    class 4TonzeWeight(ActionBase):
        """
        对指定地点发动无属性范围物理攻击 威力：200 攻击复数敌人时，对第一个之外的敌人威力降低50% 追加效果：40%加重 持续时间：30秒

        """
        id = 11384
        name = {"4-tonze Weight", "4星吨"}

    class WaterCannon(ActionBase):
        """
        对目标发动水属性魔法攻击 威力：200

        """
        id = 11385
        name = {"Water Cannon", "水炮"}

    class SongOfTorment(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：50 追加效果：无属性持续伤害 威力：50 持续时间：30秒

        """
        id = 11386
        name = {"Song of Torment", "苦闷之歌"}

    class HighVoltage(ActionBase):
        """
        对自身周围的敌人发动雷属性范围魔法攻击 威力：180 攻击复数敌人时，对第一个之外的敌人威力降低50% 追加效果：麻痹 持续时间：15秒 追加效果：目标处于水毒状态时威力提高，持续时间增加 目标处于水毒状态时威力：220 目标处于水毒状态时持续时间：30秒 

        """
        id = 11387
        name = {"High Voltage", "高压电流"}

    class BadBreath(ActionBase):
        """
        向自身前方扇形范围内喷吐臭气 令范围内的敌人陷入中毒、伤害降低10%、加重40%、减速20%、失明、麻痹状态 中毒威力：20 持续时间：15秒 同时中断目标的技能咏唱

        """
        id = 11388
        name = {"Bad Breath", "臭气"}

    class FlyingFrenzy(ActionBase):
        """
        跃向目标并对目标及其周围敌人发动范围物理攻击 威力：150 攻击复数敌人时，对目标之外的敌人威力降低50% 止步状态下无法发动

        """
        id = 11389
        name = {"Flying Frenzy", "狂乱"}

    class AquaBreath(ActionBase):
        """
        向自身前方发动水属性扇形范围魔法攻击 威力：140 攻击复数敌人时，对第一个之外的敌人威力降低50% 追加效果：水属性持续伤害 威力：20 持续时间：12秒

        """
        id = 11390
        name = {"Aqua Breath", "水流吐息"}

    class Plaincracker(ActionBase):
        """
        对自身周围的敌人发动土属性范围魔法攻击 威力：220 攻击复数敌人时，对第一个之外的敌人威力降低50%

        """
        id = 11391
        name = {"Plaincracker", "平原震裂"}

    class AcornBomb(ActionBase):
        """
        令目标及其周围的敌人陷入睡眠状态 持续时间：30秒 发动之后会停止自动攻击

        """
        id = 11392
        name = {"Acorn Bomb", "橡果炸弹"}

    class Bristle(ActionBase):
        """
        效果时间内，自身发动的1次魔法威力提升50% 持续时间：30秒 无法与攻击准备效果共存

        402, 怒发冲冠, Thrown for a Loop, 受到挑衅愤怒不已，会不停地追赶挑衅者
        """
        id = 11393
        name = {"Bristle", "怒发冲冠"}

    class MindBlast(ActionBase):
        """
        对自身周围的敌人发动无属性范围魔法攻击 威力：200 攻击复数敌人时，对第一个之外的敌人威力降低50% 追加效果：麻痹 持续时间：30秒

        """
        id = 11394
        name = {"Mind Blast", "精神冲击"}

    class BloodDrain(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：50 追加效果：恢复自身魔力

        """
        id = 11395
        name = {"Blood Drain", "吸血"}

    class BombToss(ActionBase):
        """
        对指定地点发动火属性范围魔法攻击 威力：200 攻击复数敌人时，对第一个之外的敌人威力降低50% 追加效果：眩晕 持续时间：3秒

        """
        id = 11396
        name = {"Bomb Toss", "投弹"}

    class 1000Needles(ActionBase):
        """
        对自身周围的敌人发动无属性范围物理攻击 固定伤害：1000 伤害由范围内的敌人分摊

        """
        id = 11397
        name = {"1000 Needles", "千针刺"}

    class DrillCannons(ActionBase):
        """
        向目标所在方向发出无属性直线范围物理攻击 威力：200 攻击复数敌人时，对第一个之外的敌人威力降低50% 目标处于石化状态时威力提高 目标处于石化状态时威力：600 追加效果：解除敌对目标身上的石化状态

        """
        id = 11398
        name = {"Drill Cannons", "钻头炮"}

    class TheLook(ActionBase):
        """
        向自身前方发动无属性扇形范围魔法攻击 威力：220 攻击复数敌人时，对第一个之外的敌人威力降低50% 追加效果：提升仇恨

        """
        id = 11399
        name = {"the Look", "诡异视线"}

    class SharpenedKnife(ActionBase):
        """
        对目标发动无属性物理攻击 威力：220 目标处于眩晕状态时威力提高 目标处于眩晕状态时威力：450

        """
        id = 11400
        name = {"Sharpened Knife", "锋利菜刀"}

    class Loom(ActionBase):
        """
        迅速移动到指定地点 止步状态下无法发动

        """
        id = 11401
        name = {"Loom", "若隐若现"}

    class FlameThrower(ActionBase):
        """
        向自身前方发动火属性扇形范围魔法攻击 威力：220 攻击复数敌人时，对第一个之外的敌人威力降低50%

        """
        id = 11402
        name = {"Flame Thrower", "火炎放射"}

    class Faze(ActionBase):
        """
        令自身前方扇形范围内的敌人陷入眩晕状态 持续时间：6秒

        """
        id = 11403
        name = {"Faze", "拍掌"}

    class Glower(ActionBase):
        """
        向目标所在方向发出雷属性直线范围魔法攻击 威力：220 攻击复数敌人时，对第一个之外的敌人威力降低50% 追加效果：麻痹 持续时间：6秒

        """
        id = 11404
        name = {"Glower", "怒视"}

    class Missile(ActionBase):
        """
        给予目标等同其当前体力50%的伤害 命中率较低 目标等级高于自身等级时无效

        """
        id = 11405
        name = {"Missile", "导弹"}

    class WhiteWind(ActionBase):
        """
        恢复自身及周围队员的体力，恢复量等同于自身当前的体力量

        """
        id = 11406
        name = {"White Wind", "白风"}

    class FinalSting(ActionBase):
        """
        对目标发动无属性物理攻击 威力：2000 发动后自身陷入无法战斗状态 追加效果：意志薄弱 即使进入无法战斗状态也不会解除意志薄弱 持续时间：600秒 发动条件：非意志薄弱状态中

        """
        id = 11407
        name = {"Final Sting", "终极针"}

    class SelfDestruct(ActionBase):
        """
        对自身周围的敌人发动火属性范围魔法攻击 威力：1500 自身处于油性分泌物状态时威力提高至1800 发动后自身陷入无法战斗状态 追加效果：意志薄弱 即使进入无法战斗状态也不会解除意志薄弱 持续时间：600秒 发动条件：非意志薄弱状态中

        """
        id = 11408
        name = {"Self-destruct", "自爆"}

    class Transfusion(ActionBase):
        """
        令一名队员的体力与魔力完全恢复 发动后自身陷入无法战斗状态 追加效果：意志薄弱 即使进入无法战斗状态也不会解除意志薄弱 持续时间：600秒 发动条件：非意志薄弱状态中

        """
        id = 11409
        name = {"Transfusion", "融合"}

    class ToadOil(ActionBase):
        """
        一定时间内，自身的回避率提高20% 持续时间：180秒

        1737, 油性分泌物, Toad Oil, 回避率提高
        """
        id = 11410
        name = {"Toad Oil", "油性分泌物"}

    class OffGuard(ActionBase):
        """
        一定时间内，目标所受伤害提高5% 持续时间：15秒 该魔法有单独计算的复唱时间，不受其他魔法复唱时间的影响 与惊奇光共享复唱时间

        1717, 破防, Off-guard, 受到攻击的伤害增加
        """
        id = 11411
        name = {"Off-guard", "破防"}

    class StickyTongue(ActionBase):
        """
        将目标拉向自身，同时令目标陷入眩晕状态 持续时间：4秒 追加效果：提升仇恨

        """
        id = 11412
        name = {"Sticky Tongue", "滑舌"}

    class TailScrew(ActionBase):
        """
        令目标的体力降至个位数 命中率较低 目标等级高于自身等级时无效

        """
        id = 11413
        name = {"Tail Screw", "螺旋尾"}

    class Level5Petrify(ActionBase):
        """
        令自身前方扇形范围内等级为5的倍数的敌人陷入石化状态 持续时间：20秒 命中率较低 目标等级高于自身等级时无效

        """
        id = 11414
        name = {"Level 5 Petrify", "5级石化"}

    class MoonFlute(ActionBase):
        """
        令自身发动攻击造成的伤害提高50%，同时移动速度提高30% 持续时间：15秒 效果结束后对自身附加狂战士化的副作用状态 持续时间：15秒 狂战士化的副作用效果：无法发动自动攻击、魔法、战技、能力

        """
        id = 11415
        name = {"Moon Flute", "月之笛"}

    class Doom(ActionBase):
        """
        令目标陷入死亡宣告状态 持续时间：15秒 持续时间结束后，目标陷入无法战斗状态 命中率较低 目标等级高于自身等级时无效

        210, 死亡宣告, Doom, 倒计时为0时会陷入无法战斗状态
        910, 死亡宣告, Doom, 倒计时为0时会陷入无法战斗状态
        1738, 死亡宣告, Doom, 倒计时为0时会陷入无法战斗状态
        1769, 死亡宣告, Doom, 倒计时为0时会陷入无法战斗状态
        1970, 死亡宣告, Doom, 倒计时为0时会陷入无法战斗状态
        2516, 死亡宣告, Doom, 倒计时为0时会陷入无法战斗状态
        2519, 死亡宣告, Doom, 倒计时为0时会陷入无法战斗状态
        """
        id = 11416
        name = {"Doom", "死亡宣告"}

    class MightyGuard(ActionBase):
        """
        令自身所受到的伤害减轻40%，同时以令攻击造成的伤害降低40%为代价提升自身仇恨 持续时间内咏唱不会因受到伤害而中断 再次发动时则取消该状态 持续时间：永久

        1719, 强力守护, Mighty Guard, 令自身所受到的伤害减少，同时会以攻击力降低为代价提高自身仇恨
        """
        id = 11417
        name = {"Mighty Guard", "强力守护"}

    class IceSpikes(ActionBase):
        """
        一定时间内，自身受到物理攻击时会对对方造成冰属性魔法伤害 威力：40 持续时间：15秒 追加效果（发动几率50%）：减速20% 持续时间：15秒

        198, 冰棘屏障, Ice Spikes, 能够发动冰属性反击，偶尔会追加减速效果
        1307, 冰棘屏障, Ice Spikes, 受到物理攻击时，攻击方将受到冰属性伤害，并有一定几率被附加减速状态
        1720, 冰棘屏障, Ice Spikes, 受到物理攻击时，攻击方将受到冰属性伤害，并有一定几率被附加减速状态
        2528, 冰棘屏障, Ice Spikes, 能够发动冰属性反击，追加减速效果
        """
        id = 11418
        name = {"Ice Spikes", "冰棘屏障"}

    class TheRamsVoice(ActionBase):
        """
        对自身周围的敌人发动冰属性范围魔法攻击 威力：220 攻击复数敌人时，对第一个之外的敌人威力降低50% 追加效果：冻结 持续时间：12秒

        """
        id = 11419
        name = {"the Ram's Voice", "寒冰咆哮"}

    class TheDragonsVoice(ActionBase):
        """
        对自身周围的敌人发动雷属性范围魔法攻击 威力：200 无法攻击到自身周围8米以内的敌人 攻击复数敌人时，对第一个之外的敌人威力降低50% 追加效果：麻痹 持续时间：9秒 目标处于冻结状态时威力提高，对特定敌人无效 冻结状态时威力：400 追加效果：解除目标身上的冻结状态，对特定敌人无效

        """
        id = 11420
        name = {"the Dragon's Voice", "雷电咆哮"}

    class PeculiarLight(ActionBase):
        """
        令自身周围的敌人所受到的魔法伤害提高5% 持续时间：15秒 该魔法有单独计算的复唱时间，不受其他魔法复唱时间的影响 与破防共享复唱时间

        1721, 惊奇光, Peculiar Light, 受到魔法攻击的伤害增加
        """
        id = 11421
        name = {"Peculiar Light", "惊奇光"}

    class InkJet(ActionBase):
        """
        向自身前方发动无属性扇形范围魔法攻击 威力：200 攻击复数敌人时，对第一个之外的敌人威力降低50% 追加效果：失明 持续时间：30秒

        """
        id = 11422
        name = {"Ink Jet", "喷墨"}

    class FlyingSardine(ActionBase):
        """
        对目标发动无属性物理攻击 威力：10 追加效果：中断目标的技能咏唱

        """
        id = 11423
        name = {"Flying Sardine", "投掷沙丁鱼"}

    class Diamondback(ActionBase):
        """
        一定时间内，将自身所受的伤害减轻90%，同时除特定攻击之外其他所有击退与吸引效果失效 但是持续时间内无法移动或使用技能 持续时间：10秒 追加效果：解除自身的狂战士化状态 此技能发动后无法主动中断

        1722, 超硬化, Diamondback, 无法自由活动，但受到攻击的伤害减少
        """
        id = 11424
        name = {"Diamondback", "超硬化"}

    class FireAngon(ActionBase):
        """
        对目标及其周围的敌人发动火属性范围物理攻击 威力：200 攻击复数敌人时，对目标之外的敌人威力降低50%

        """
        id = 11425
        name = {"Fire Angon", "火投枪"}

    class FeatherRain(ActionBase):
        """
        对指定地点发动风属性范围魔法攻击 威力：220 追加效果：风属性持续伤害 威力：40 持续时间：6秒 与部分青魔法共享复唱时间

        """
        id = 11426
        name = {"Feather Rain", "飞翎雨"}

    class Eruption(ActionBase):
        """
        对指定地点发动火属性范围魔法攻击 威力：300 与部分青魔法共享复唱时间

        """
        id = 11427
        name = {"Eruption", "地火喷发"}

    class MountainBuster(ActionBase):
        """
        向自身前方发动土属性扇形范围物理攻击 威力：400 攻击复数敌人时，对第一个之外的敌人威力降低50% 与部分青魔法共享复唱时间

        """
        id = 11428
        name = {"Mountain Buster", "山崩"}

    class ShockStrike(ActionBase):
        """
        对目标及其周围的敌人发动雷属性范围魔法攻击 威力：400 攻击复数敌人时，对目标之外的敌人威力降低50% 与部分青魔法共享复唱时间

        """
        id = 11429
        name = {"Shock Strike", "轰雷"}

    class GlassDance(ActionBase):
        """
        向自身前方与两侧发动冰属性扇形范围魔法攻击 威力：350 攻击复数敌人时，对第一个之外的敌人威力降低50% 与部分青魔法共享复唱时间

        """
        id = 11430
        name = {"Glass Dance", "冰雪乱舞"}

    class VeilOfTheWhorl(ActionBase):
        """
        一定时间内，自身受到攻击时会对对方造成水属性魔法伤害 威力：50 持续时间：30秒 与部分青魔法共享复唱时间

        478, 水神的面纱, Veil of the Whorl, 反射远程物理攻击所造成的伤害
        1724, 水神的面纱, Veil of the Whorl, 受到攻击时，攻击方将受到水属性伤害
        """
        id = 11431
        name = {"Veil of the Whorl", "水神的面纱"}

    class AlpineDraft(ActionBase):
        """
        向目标所在方向发出风属性直线范围魔法攻击 威力：220 攻击复数敌人时，对第一个之外的敌人威力降低50%

        """
        id = 18295
        name = {"Alpine Draft", "高山气流"}

    class ProteanWave(ActionBase):
        """
        向自身前方发动水属性扇形范围魔法攻击 威力：220 攻击复数敌人时，对第一个之外的敌人威力降低50% 追加效果：将范围内的敌人击退15米

        """
        id = 18296
        name = {"Protean Wave", "万变水波"}

    class Northerlies(ActionBase):
        """
        向自身前方发动冰属性扇形范围魔法攻击 威力：220 攻击复数敌人时，对第一个之外的敌人威力降低50% 追加效果：敌人处于水毒状态时解除该状态，同时附加冻结状态 持续时间：20秒

        """
        id = 18297
        name = {"Northerlies", "狂风暴雪"}

    class Electrogenesis(ActionBase):
        """
        对目标及其周围的敌人发动雷属性范围魔法攻击 威力：220 攻击复数敌人时，对目标之外的敌人威力降低50%

        """
        id = 18298
        name = {"Electrogenesis", "生物电"}

    class Kaltstrahl(ActionBase):
        """
        向自身前方发出无属性扇形范围物理攻击 威力：220 攻击复数敌人时，对第一个之外的敌人威力降低50%

        """
        id = 18299
        name = {"Kaltstrahl", "寒光"}

    class AbyssalTransfixion(ActionBase):
        """
        对目标发动无属性物理攻击 威力：220 追加效果：麻痹 持续时间：30秒

        """
        id = 18300
        name = {"Abyssal Transfixion", "深渊贯穿"}

    class Chirp(ActionBase):
        """
        令自身周围的敌人陷入睡眠状态 持续时间：40秒 发动之后会停止自动攻击

        """
        id = 18301
        name = {"Chirp", "唧唧咋咋"}

    class EerieSoundwave(ActionBase):
        """
        解除自身周围敌人身上强化效果中的一种

        """
        id = 18302
        name = {"Eerie Soundwave", "怪音波"}

    class PomCure(ActionBase):
        """
        恢复目标的体力 恢复力：100 自身处于以太复制：治疗状态时 恢复力：500

        """
        id = 18303
        name = {"Pom Cure", "绒绒治疗"}

    class Gobskin(ActionBase):
        """
        为自身和周围队员附加能够抵御一定伤害的防护罩 该防护罩能够抵消相当于恢复力100的伤害量 持续时间：30秒 自身处于以太复制：治疗状态时 该防护罩能够抵消相当于恢复力250的伤害量 无法与学者的鼓舞和占星术士的黑夜领域效果共存

        2114, 哥布防御, Gobskin, 抵消一定伤害
        """
        id = 18304
        name = {"Gobskin", "哥布防御"}

    class MagicHammer(ActionBase):
        """
        对目标及其周围的敌人发动无属性魔法攻击 威力：250 攻击复数敌人时，对目标之外的敌人威力降低50% 追加效果：令目标的智力与精神降低10% 持续时间：10秒 追加效果：恢复自身最大魔力的10% 该魔法有单独计算的复唱时间

        """
        id = 18305
        name = {"Magic Hammer", "魔法锤"}

    class Avail(ActionBase):
        """
        让目标队员替自己承受来自敌人的攻击 但对部分攻击无效 持续时间：12秒 与目标的距离不能超过10米 该魔法有单独计算的复唱时间

        2116, 防御指示, Meatily Shielded, 下达了防御指示，让特定队员替自己承受伤害
        2117, 防御指示, Meat Shield, 被下达了防御指示，替特定队员承受伤害
        """
        id = 18306
        name = {"Avail", "防御指示"}

    class FrogLegs(ActionBase):
        """
        向周围的敌人进行挑衅，令自身的仇恨变为最高

        """
        id = 18307
        name = {"Frog Legs", "蛙腿"}

    class SonicBoom(ActionBase):
        """
        对目标发动风属性魔法攻击 威力：210

        """
        id = 18308
        name = {"Sonic Boom", "音爆"}

    class Whistle(ActionBase):
        """
        效果时间内自身发动的1次魔法为物理攻击时，威力提升80% 持续时间：30秒 无法与蓄力效果共存

        """
        id = 18309
        name = {"Whistle", "口笛"}

    class WhiteKnightsTour(ActionBase):
        """
        向目标所在方向发出无属性直线范围魔法攻击 威力：200 敌人处于止步状态时解除该状态，同时提升威力 敌人处于止步状态时威力：400 攻击复数敌人时，对第一个之外的敌人威力降低50% 追加效果：减速20% 持续时间：20秒

        """
        id = 18310
        name = {"White Knight's Tour", "白骑士之旅"}

    class BlackKnightsTour(ActionBase):
        """
        向目标所在方向发出无属性直线范围魔法攻击 威力：200 敌人处于减速状态时解除该状态，同时提升威力 敌人处于减速状态时威力：400 攻击复数敌人时，对第一个之外的敌人威力降低50% 追加效果：止步 持续时间：20秒

        """
        id = 18311
        name = {"Black Knight's Tour", "黑骑士之旅"}

    class Level5Death(ActionBase):
        """
        令自身周围等级为5的倍数的敌人陷入无法战斗状态 命中率较低 目标等级高于自身等级时无效 该魔法有单独计算的复唱时间，并与部分青魔法共享复唱时间

        """
        id = 18312
        name = {"Level 5 Death", "5级即死"}

    class Launcher(ActionBase):
        """
        给予自身周围敌人等同其当前体力50%或30%或20%或10%的伤害 目标等级高于自身等级时无效

        """
        id = 18313
        name = {"Launcher", "火箭炮"}

    class PerpetualRay(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：220 追加效果：眩晕 持续时间：1秒 该技能的眩晕效果不受其他眩晕影响

        """
        id = 18314
        name = {"Perpetual Ray", "永恒射线"}

    class Cactguard(ActionBase):
        """
        指定一名队员，令其受到的伤害减轻5% 持续时间：6秒 自身处于以太复制：防护状态时 队员受到的伤害减轻15%

        2119, 仙人盾, Cactguard, 受到的伤害降低
        """
        id = 18315
        name = {"Cactguard", "仙人盾"}

    class RevengeBlast(ActionBase):
        """
        对目标发动无属性物理攻击 威力：50 自身剩余体力在20%以下时威力提升 体力在20%以下时：500

        """
        id = 18316
        name = {"Revenge Blast", "复仇冲击"}

    class AngelWhisper(ActionBase):
        """
        令无法战斗的目标以衰弱状态重新振作起来 该魔法有单独计算的复唱时间

        """
        id = 18317
        name = {"Angel Whisper", "天使低语"}

    class Exuviation(ActionBase):
        """
        恢复自身及周围队员的体力 恢复力：50 追加效果：解除部分弱化效果中的一种 自身处于以太复制：治疗状态时 恢复力：300

        """
        id = 18318
        name = {"Exuviation", "蜕皮"}

    class Reflux(ActionBase):
        """
        对目标发动雷属性魔法攻击 威力：220 追加效果：40%加重 持续时间：10秒 该技能的加重效果不受其他加重影响

        """
        id = 18319
        name = {"Reflux", "逆流"}

    class Devour(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：250 追加效果：一定时间内，自身的最大体力提高20% 持续时间：15秒 以太复制：防护状态下的持续时间变为70秒 追加效果：恢复伤害量100%的体力 该魔法有单独计算的复唱时间

        421, 捕食, Devoured, 被吞了下去无法做出任何行动，体力逐渐减少
        """
        id = 18320
        name = {"Devour", "捕食"}

    class CondensedLibra(ActionBase):
        """
        对目标随机附加星极性耐性降低、灵极性耐性降低、物理受伤加重状态 持续时间：30秒 星极性耐性降低效果：所受火、风、雷属性伤害提高5% 灵极性耐性降低效果：所受水、土、冰属性伤害提高5% 物理受伤加重效果：所受物理伤害提高5% 以上状态无法叠加

        """
        id = 18321
        name = {"Condensed Libra", "小侦测"}

    class AetherialMimicry(ActionBase):
        """
        指定一名除自身外的玩家，复制其以太特性 对自身附加以太复制：防护、以太复制：进攻、以太复制：治疗状态中的一种 指定玩家的职能将决定附加的状态 以太复制：防护状态下，自身的防御力上升，同时强化部分青魔法 以太复制：进攻状态下，自身的暴击发动率和直击发动率提高20% 以太复制：治疗状态下，自身发动治疗魔法的治疗量提高20%，同时强化部分青魔法 再次发动时则取消该状态 持续时间：永久

        """
        id = 18322
        name = {"Aetherial Mimicry", "以太复制"}

    class Surpanakha(ActionBase):
        """
        向自身前方发出土属性扇形范围魔法攻击 威力：200 攻击复数敌人时，对第一个之外的敌人威力降低50% 积蓄次数：4 追加效果：穿甲散弹的威力提高50% 最大档数：3档 持续时间：3秒 若在持续时间中发动穿甲散弹之外的技能，会立即解除该状态

        """
        id = 18323
        name = {"Surpanakha", "穿甲散弹"}

    class Quasar(ActionBase):
        """
        对自身周围的敌人发动无属性魔法攻击 威力：300 攻击复数敌人时，对第一个之外的敌人威力降低50% 与部分青魔法共享复唱时间

        """
        id = 18324
        name = {"Quasar", "类星体"}

    class JKick(ActionBase):
        """
        跳起接近目标并发动无属性范围物理攻击 威力：300 攻击复数敌人时，对目标之外的敌人威力降低50% 止步状态下无法发动 与部分青魔法共享复唱时间

        """
        id = 18325
        name = {"J Kick", "正义飞踢"}

    class AetherialMimicry(ActionBase):
        """
        指定一名除自身外的玩家，复制其以太特性 对自身附加以太复制：防护、以太复制：进攻、以太复制：治疗状态中的一种 指定玩家的职能将决定附加的状态 以太复制：防护状态下，自身的防御力上升，同时强化部分青魔法 以太复制：进攻状态下，自身的暴击发动率和直击发动率提高20% 以太复制：治疗状态下，自身发动治疗魔法的治疗量提高20%，同时强化部分青魔法 再次发动时则取消该状态 持续时间：永久

        """
        id = 19238
        name = {"Aetherial Mimicry", "以太复制"}

    class AetherialMimicry(ActionBase):
        """
        指定一名除自身外的玩家，复制其以太特性 对自身附加以太复制：防护、以太复制：进攻、以太复制：治疗状态中的一种 指定玩家的职能将决定附加的状态 以太复制：防护状态下，自身的防御力上升，同时强化部分青魔法 以太复制：进攻状态下，自身的暴击发动率和直击发动率提高20% 以太复制：治疗状态下，自身发动治疗魔法的治疗量提高20%，同时强化部分青魔法 再次发动时则取消该状态 持续时间：永久

        """
        id = 19239
        name = {"Aetherial Mimicry", "以太复制"}

    class AetherialMimicry(ActionBase):
        """
        指定一名除自身外的玩家，复制其以太特性 对自身附加以太复制：防护、以太复制：进攻、以太复制：治疗状态中的一种 指定玩家的职能将决定附加的状态 以太复制：防护状态下，自身的防御力上升，同时强化部分青魔法 以太复制：进攻状态下，自身的暴击发动率和直击发动率提高20% 以太复制：治疗状态下，自身发动治疗魔法的治疗量提高20%，同时强化部分青魔法 再次发动时则取消该状态 持续时间：永久

        """
        id = 19240
        name = {"Aetherial Mimicry", "以太复制"}

    class TripleTrident(ActionBase):
        """
        对目标发动连续3次物理攻击 威力：150 该魔法有单独计算的复唱时间

        """
        id = 23264
        name = {"Triple Trident", "渔叉三段"}

    class Tingle(ActionBase):
        """
        对目标及其周围敌人发动雷属性范围魔法攻击 威力：100 攻击复数敌人时，对目标之外的敌人威力降低50% 追加效果：效果时间内自身发动的1次魔法为物理攻击时，威力提升100 持续时间：15秒

        2492, 哔哩哔哩, Tingling, 下一个发动的魔法属于物理攻击时威力提升
        """
        id = 23265
        name = {"Tingle", "哔哩哔哩"}

    class TatamiGaeshi(ActionBase):
        """
        向目标所在方向发出无属性直线范围魔法攻击 威力：220 追加效果：眩晕 持续时间：3秒 攻击复数敌人时，对目标之外的敌人威力降低50%

        """
        id = 23266
        name = {"Tatami-gaeshi", "掀地板之术"}

    class ColdFog(ActionBase):
        """
        对自身附加彻骨雾寒状态 持续时间：5秒 持续时间内如果受到敌人的攻击，则效果会变化成冰雾 冰雾效果：技能彻骨雾寒变化为冰雾 持续时间：15秒 该魔法有单独计算的复唱时间 冰雾 对目标发动冰属性魔法攻击 威力：400 追加效果：冻结 持续时间：10秒 发动条件：冰雾状态中

        2493, 彻骨雾寒, Cold Fog, 被彻骨雾寒包裹，受到伤害后将附加冰雾状态
        """
        id = 23267
        name = {"Cold Fog", "彻骨雾寒"}

    class WhiteDeath(ActionBase):
        """
        对目标发动冰属性魔法攻击 威力：400 追加效果：冻结 持续时间：10秒 发动条件：冰雾状态中

        2494, 冰雾, Touch of Frost, 被冰雾包裹，可以使用青魔法“冰雾”
        """
        id = 23268
        name = {"White Death", "冰雾"}

    class Stotram(ActionBase):
        """
        对周围的敌人发动无属性范围魔法攻击 威力：140 自身处于以太复制：治疗状态时效果变为 恢复自身及周围队员的体力 恢复力：300

        """
        id = 23269
        name = {"Stotram", "赞歌"}

    class SaintlyBeam(ActionBase):
        """
        对目标及其周围的敌人发动无属性范围魔法攻击 威力：100 目标为不死系怪物时，威力提高 对不死系怪物的威力：500

        """
        id = 23270
        name = {"Saintly Beam", "圣光射线"}

    class FeculentFlood(ActionBase):
        """
        向目标所在方向发出土属性直线范围魔法攻击 威力：220 攻击复数敌人时，对目标之外的敌人威力降低50%

        """
        id = 23271
        name = {"Feculent Flood", "污泥泼洒"}

    class AngelsSnack(ActionBase):
        """
        恢复自身及周围队员的体力 恢复力：400 自身处于以太复制：治疗状态时 追加效果：令目标体力持续恢复 恢复力：200 持续时间：15秒 该魔法有单独计算的复唱时间，并与部分青魔法共享复唱时间

        2495, 天使的点心, Angel's Snack, 体力会随时间逐渐恢复
        """
        id = 23272
        name = {"Angel's Snack", "天使的点心"}

    class ChelonianGate(ActionBase):
        """
        展开玄结界，令自身所受的伤害减轻20% 持续时间：10秒 追加效果：持续时间内如果受到超过自身最大体力30%的伤害，则对自身附加玄天武水壁 玄天武水壁效果：技能玄结界变化为玄天武水壁 效果时间内发动技能或进行移动、转身都会使玄结界立即消失 此外当玄结界消失时，玄天武水壁也会同时消失 该魔法有单独计算的复唱时间，并与部分青魔法共享复唱时间 玄天武水壁 对自身周围的敌人发动水属性范围魔法攻击 威力：500 自身处于以太复制：防护状态时 威力：1000 攻击复数敌人时，对目标之外的敌人威力降低50% 效果发动条件：玄天武水壁状态中

        2496, 玄结界, Chelonian Gate, 减轻所受到的伤害，受到一定伤害后将附加玄天武水壁状态
        """
        id = 23273
        name = {"Chelonian Gate", "玄结界"}

    class DivineCataract(ActionBase):
        """
        对自身周围的敌人发动水属性范围魔法攻击 威力：500 自身处于以太复制：防护状态时 威力：1000 攻击复数敌人时，对目标之外的敌人威力降低50% 效果发动条件：玄天武水壁状态中

        2497, 玄天武水壁, Auspicious Trance, 可以使用青魔法“玄天武水壁”
        """
        id = 23274
        name = {"Divine Cataract", "玄天武水壁"}

    class TheRoseOfDestruction(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：400 追加效果：击退10米 该魔法有单独计算的复唱时间，并与部分青魔法共享复唱时间

        """
        id = 23275
        name = {"The Rose of Destruction", "斗灵弹"}

    class BasicInstinct(ActionBase):
        """
        此技能仅限在非单人任务中，且由自己单独进行攻略时或除自身外其他小队成员均陷入无法战斗状态时才会生效 令自身的移动速度提升30%，自身攻击造成的伤害及治疗魔法的治疗量提高100%，并无视强力守护所造成的伤害降低效果 持续时间：永久 此效果在小队成员回归战斗状态后立即解除

        2498, 斗争本能, Basic Instinct, 自身攻击造成的伤害及治疗魔法的治疗量提高并且移动速度上升，无视“强力守护”造成的伤害降低效果
        """
        id = 23276
        name = {"Basic Instinct", "斗争本能"}

    class Ultravibration(ActionBase):
        """
        在自身周围产生超音波，令冻结或石化状态中的敌人必定陷入无法战斗状态 对部分敌人无效 目标等级高于自身等级时无效 该魔法有单独计算的复唱时间，并与部分青魔法共享复唱时间

        """
        id = 23277
        name = {"Ultravibration", "超振动"}

    class Blaze(ActionBase):
        """
        对目标及其周围的敌人发动冰属性范围魔法攻击 威力：220 攻击复数敌人时，对目标之外的敌人威力降低50%

        """
        id = 23278
        name = {"Blaze", "冰焰"}

    class MustardBomb(ActionBase):
        """
        对目标及其周围的敌人发动火属性范围魔法攻击 威力：220 攻击复数敌人时，对目标之外的敌人威力降低50% 追加效果：如果目标处于头晕状态中，则附加火属性持续伤害 威力：50 持续时间：15秒

        """
        id = 23279
        name = {"Mustard Bomb", "芥末爆弹"}

    class DragonForce(ActionBase):
        """
        一定时间内，将自身所受的伤害减轻20% 持续时间：15秒 以太复制：防护状态下的伤害减轻变为40% 该魔法有单独计算的复唱时间，并与部分青魔法共享复唱时间

        306, 龙之力, Inner Dragon, 得到了龙眼的力量
        2500, 龙之力, Dragon Force, 受到的伤害降低
        """
        id = 23280
        name = {"Dragon Force", "龙之力"}

    class AetherialSpark(ActionBase):
        """
        向目标所在方向发出无属性直线范围魔法攻击 威力：50 追加效果：无属性持续伤害 威力：50 持续时间：15秒

        """
        id = 23281
        name = {"Aetherial Spark", "以太火花"}

    class HydroPull(ActionBase):
        """
        对自身周围的敌人发动水属性范围魔法攻击 威力：220 攻击复数敌人时，对第一个之外的敌人威力降低50% 追加效果：把敌人吸引到身边

        """
        id = 23282
        name = {"Hydro Pull", "水力吸引"}

    class MaledictionOfWater(ActionBase):
        """
        向自身前方发出水属性直线范围魔法攻击 威力：200 攻击复数敌人时，对第一个之外的敌人威力降低50% 追加效果：将范围内的敌人与小队成员击退10米 目标身中部分弱化效果或处于非战斗状态时无效

        """
        id = 23283
        name = {"Malediction of Water", "水脉诅咒"}

    class ChocoMeteor(ActionBase):
        """
        对目标及其周围的敌人发动无属性范围魔法攻击 威力：200 如果小队中存在自己的专属陆行鸟，则技能威力上升 专属陆行鸟在小队时威力：300 攻击复数敌人时，对目标之外的敌人威力降低50%

        """
        id = 23284
        name = {"Choco Meteor", "陆行鸟陨石"}

    class MatraMagic(ActionBase):
        """
        对目标发动连续8次无属性魔法攻击 威力：50 自身处于以太复制：进攻状态时 威力：100 该魔法有单独计算的复唱时间，并与部分青魔法共享复唱时间

        """
        id = 23285
        name = {"Matra Magic", "马特拉魔术"}

    class PeripheralSynthesis(ActionBase):
        """
        向目标所在方向发出无属性直线范围物理攻击 威力：220 追加效果：附加头晕 持续时间：5秒 短时间内对同一目标重复使用时，每次可令目标头晕的时间都会减少，直至完全无效 令目标陷入头晕状态时威力上升 令目标陷入头晕状态时威力：400 攻击复数敌人时，对目标之外的敌人威力降低50%

        """
        id = 23286
        name = {"Peripheral Synthesis", "生成外设"}

    class BothEnds(ActionBase):
        """
        对自身周围的敌人发动无属性范围物理攻击 威力：600 与部分青魔法共享复唱时间

        """
        id = 23287
        name = {"Both Ends", "如意大旋风"}

    class PhantomFlurry(ActionBase):
        """
        持续向自身前方发出扇形范围攻击 每秒对范围内的敌人造成伤害 威力：200 持续时间：5秒 持续时间内再次使用时，向自身前方发出无属性扇形范围攻击 威力：600 攻击复数敌人时，对第一个之外的敌人威力降低50% 效果时间内发动鬼宿脚以外的技能或进行移动、转身都会使鬼宿脚立即消失

        2502, 鬼宿脚, Phantom Flurry, 正在踢出鬼宿脚
        """
        id = 23288
        name = {"Phantom Flurry", "鬼宿脚"}

    class PhantomFlurry(ActionBase):
        """
        持续向自身前方发出扇形范围攻击 每秒对范围内的敌人造成伤害 威力：200 持续时间：5秒 持续时间内再次使用时，向自身前方发出无属性扇形范围攻击 威力：600 攻击复数敌人时，对第一个之外的敌人威力降低50% 效果时间内发动鬼宿脚以外的技能或进行移动、转身都会使鬼宿脚立即消失

        2502, 鬼宿脚, Phantom Flurry, 正在踢出鬼宿脚
        """
        id = 23289
        name = {"Phantom Flurry", "鬼宿脚"}

    class Nightbloom(ActionBase):
        """
        对周围的敌人发动无属性范围魔法攻击 威力：400 攻击复数敌人时，对第一个之外的敌人威力降低50% 追加效果：对目标附加无属性持续伤害状态 威力：75 持续时间：60秒 与部分青魔法共享复唱时间

        """
        id = 23290
        name = {"Nightbloom", "月下彼岸花"}

    class Stotram(ActionBase):
        """
        对周围的敌人发动无属性范围魔法攻击 威力：140 自身处于以太复制：治疗状态时效果变为 恢复自身及周围队员的体力 恢复力：300

        """
        id = 23416
        name = {"Stotram", "赞歌"}
