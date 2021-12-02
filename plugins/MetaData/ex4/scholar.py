from ..base import ActionBase, StatusBase, physic, magic


class Actions:

    class Aetherflow(ActionBase):
        """
        恢复自身最大魔力的10% 追加效果：最大档数的以太超流 最大档数：3档 持续时间：永久 发动条件：自身处于战斗状态

        304, 以太超流, Aetherflow, 体内的以太流动逐渐活化
        """
        id = 166
        name = {'Aetherflow', '以太超流'}

    class EnergyDrain(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：100 追加效果：恢复伤害量一定比例的体力 同时恢复自身魔力 (source.level>=70?(source.job==28?追加效果：获得10点异想以太 :):)发动条件：以太超流

        """
        id = 167
        name = {'Energy Drain', '能量吸收'}

    class Adloquium(ActionBase):
        """
        恢复目标的体力 恢复力：300 追加效果：为目标附加能够抵御一定伤害的防护罩鼓舞 鼓舞效果：抵消相当于治疗量125%的伤害 持续时间：30秒 无法与占星术士的黑夜领域效果共存 追加效果（暴击时）：为目标附加能够抵御一定伤害的防护罩激励 激励效果：抵消相当于治疗量125%的伤害 持续时间：30秒

        """
        id = 185
        name = {'Adloquium', '鼓舞激励之策'}

    class Succor(ActionBase):
        """
        恢复自身及周围队员的体力 恢复力：180 追加效果：附加能够抵御一定伤害的防护罩 该防护罩能够抵消相当于治疗量125%的伤害 持续时间：30秒 无法与占星术士的黑夜领域效果共存

        """
        id = 186
        name = {'Succor', '士气高扬之策'}

    class SacredSoil(ActionBase):
        """
        以指定地点为中心产生减轻伤害的防护区域 (source.job==28?(source.level>=78?区域内的队员所受到的伤害会减轻10%，同时持续恢复队员体力 恢复力：100 持续时间：15秒 :区域内的队员所受到的伤害会减轻10% 持续时间：15秒 ):区域内的队员所受到的伤害会减轻10% 持续时间：15秒 )(source.level>=70?(source.job==28?追加效果：获得10点异想以太 :):)发动条件：以太超流

        298, 野战治疗阵, Sacred Soil, 产生减轻伤害的防护区域
        299, 野战治疗阵, Sacred Soil, 减轻所受到的伤害
        1944, 野战治疗阵, Sacred Soil, 减轻范围内队员所受伤害，产生能够恢复体力的区域
        2637, 野战治疗阵, Sacred Soil, 减轻范围内队员所受伤害，产生能够恢复体力的区域
        2638, 野战治疗阵, Sacred Soil, 减轻所受到的伤害
        """
        id = 188
        name = {'Sacred Soil', '野战治疗阵'}

    class Lustrate(ActionBase):
        """
        恢复目标的体力 恢复力：600 (source.level>=70?(source.job==28?追加效果：获得10点异想以太 :):)发动条件：以太超流

        """
        id = 189
        name = {'Lustrate', '生命活性法'}

    class Physick(ActionBase):
        """
        恢复目标的体力 恢复力：400

        """
        id = 190
        name = {'Physick', '医术'}

    class Embrace(ActionBase):
        """
        恢复目标的体力 恢复力：150 ※该技能无法设置到热键栏

        """
        id = 802
        name = {'Embrace', '仙光的拥抱'}

    class WhisperingDawn(ActionBase):
        """
        持续恢复周围队员的体力 恢复力：120 持续时间：21秒 ※该技能无法设置到热键栏

        315, 仙光的低语, Whispering Dawn, 体力会随时间逐渐恢复
        """
        id = 803
        name = {'Whispering Dawn', '仙光的低语'}

    class FeyIllumination(ActionBase):
        """
        一定时间内周围队员发动治疗魔法的治疗量提高10%，受到的魔法伤害减轻5% 持续时间：20秒 无法与炽天使的炽天的幻光效果共存 ※该技能无法设置到热键栏

        317, 异想的幻光, Fey Illumination, 发动治疗魔法的治疗量提高，且受到魔法攻击的伤害减少
        """
        id = 805
        name = {'Fey Illumination', '异想的幻光'}

    class Indomitability(ActionBase):
        """
        恢复自身及周围队员的体力 恢复力：400 (source.level>=70?(source.job==28?追加效果：获得10点异想以太 :):)发动条件：以太超流

        """
        id = 3583
        name = {'Indomitability', '不屈不挠之策'}

    class Broil(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：240

        """
        id = 3584
        name = {'Broil', '气炎法'}

    class DeploymentTactics(ActionBase):
        """
        令自身或目标所带的鼓舞状态向周围队员身上扩散 持续时间：扩散时状态的剩余持续时间 自身没有对目标附加鼓舞状态时无效

        """
        id = 3585
        name = {'Deployment Tactics', '展开战术'}

    class EmergencyTactics(ActionBase):
        """
        效果时间内自身发动1次带有鼓舞及激励状态的治疗魔法时，将鼓舞及激励效果转化为同等数值的体力恢复效果 持续时间：15秒

        792, 应急战术, Emergency Tactics, 下次咏唱附有鼓舞效果及激励效果的治疗魔法时，将其中的防护罩效果转化为治疗效果
        """
        id = 3586
        name = {'Emergency Tactics', '应急战术'}

    class Dissipation(ActionBase):
        """
        回收小仙女的同时为自身附加最大档数的以太超流状态 并且自身发动治疗魔法的治疗量提高20% 持续时间：30秒 但是效果时间内无法咏唱朝日召唤及夕月召唤 效果时间结束后小仙女会重新被召唤出来 发动条件：自身处于战斗状态且小仙女处于同行状态

        791, 转化, Dissipation, 发动治疗魔法的治疗量提高
        2069, 转化, Dissipation, 攻击所造成的伤害提高，自身发动的体力恢复效果恢复量提高
        """
        id = 3587
        name = {'Dissipation', '转化'}

    class Excogitation(ActionBase):
        """
        为自身或一名队员附加“体力低于50%时或持续时间结束后自动恢复”状态 恢复力：800 持续时间：45秒 (source.level>=70?(source.job==28?追加效果：获得10点异想以太 :):)发动条件：以太超流

        1220, 深谋远虑之策, Excogitation, 体力降低到一定比例或持续时间结束后便会发动恢复效果
        2182, 深谋远虑之策, Excogitation, 体力降低到一定比例或持续时间结束时自动发动恢复效果
        """
        id = 7434
        name = {'Excogitation', '深谋远虑之策'}

    class BroilIi(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：260

        """
        id = 7435
        name = {'Broil II', '魔炎法'}

    class ChainStratagem(ActionBase):
        """
        一定时间内，目标被暴击率提高10% 持续时间：15秒

        1221, 连环计, Chain Stratagem, 受到暴击的几率提高
        1406, 连环计, Chain Stratagem, 受到攻击的伤害增加
        """
        id = 7436
        name = {'Chain Stratagem', '连环计'}

    class Aetherpact(ActionBase):
        """
        命令召唤出的小仙女对自身或一名队员发动异想的融光 再次发动时则取消该状态 发动条件：异想以太10点 异想以太获得条件：自身处于战斗状态，(source.job==28?(source.level>=80?小仙女或炽天使:小仙女):小仙女)处于同行状态，消耗以太超流的技能成功生效

        """
        id = 7437
        name = {'Aetherpact', '以太契约'}

    class FeyUnion(ActionBase):
        """
        持续恢复目标的体力 恢复力：400 发动后持续消耗异想以太 且小仙女无法进行其他行动 效果发动条件：与目标的距离不超过15米 ※该技能无法设置到热键栏

        1222, 异想的融光, Fey Union, 发动持续恢复体力效果
        1223, 异想的融光, Fey Union, 受到持续恢复体力效果
        """
        id = 7438
        name = {'Fey Union', '异想的融光'}

    class DissolveUnion(ActionBase):
        """
        将异想的融光状态解除

        """
        id = 7869
        name = {'Dissolve Union', '融光解除'}

    class WhisperingDawn(ActionBase):
        """
        命令小仙女发动仙光的低语 (source.job==28?(source.level>=80?炽天使同行时，命令炽天使发动天使的低语 :):) 持续恢复周围队员的体力 恢复力：120 持续时间：21秒 发动条件：(source.job==28?(source.level>=80?小仙女或炽天使:小仙女):小仙女)处于同行状态

        315, 仙光的低语, Whispering Dawn, 体力会随时间逐渐恢复
        """
        id = 16537
        name = {'Whispering Dawn', '仙光的低语'}

    class FeyIllumination(ActionBase):
        """
        命令小仙女发动异想的幻光 (source.job==28?(source.level>=80?炽天使同行时，命令炽天使发动炽天的幻光 :):) 一定时间内周围队员发动治疗魔法的治疗量提高10%，受到的魔法伤害减轻5% 持续时间：20秒 小仙女的异想的幻光无法与炽天使的炽天的幻光效果共存 发动条件：(source.job==28?(source.level>=80?小仙女或炽天使:小仙女):小仙女)处于同行状态

        317, 异想的幻光, Fey Illumination, 发动治疗魔法的治疗量提高，且受到魔法攻击的伤害减少
        """
        id = 16538
        name = {'Fey Illumination', '异想的幻光'}

    class ArtOfWar(ActionBase):
        """
        对周围的敌人发动无属性范围魔法攻击 威力：(source.job==28?(source.level>=54?160:150):150)

        """
        id = 16539
        name = {'Art of War', '破阵法'}

    class Biolysis(ActionBase):
        """
        对目标附加无属性持续伤害状态 威力：70 持续时间：30秒

        1895, 蛊毒法, Biolysis, 体力逐渐减少
        2039, 蛊毒法, Biolysis, 自身所受的体力恢复效果降低
        """
        id = 16540
        name = {'Biolysis', '蛊毒法'}

    class BroilIii(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：290

        """
        id = 16541
        name = {'Broil III', '死炎法'}

    class Recitation(ActionBase):
        """
        效果时间内，自身发动的1次鼓舞激励之策、士气高扬之策、不屈不挠之策、深谋远虑之策可以不消耗魔力及以太超流，并且必定暴击 持续时间：15秒

        1896, 秘策, Recitation, 下一次发动的鼓舞激励之策、士气高扬之策、不屈不挠之策、深谋远虑之策，无需消耗魔力和以太超流，并且必定暴击
        """
        id = 16542
        name = {'Recitation', '秘策'}

    class FeyBlessing(ActionBase):
        """
        命令小仙女发动异想的祥光 恢复自身及周围队员的体力 恢复力：350 发动条件：小仙女处于同行状态且异想以太10点

        """
        id = 16543
        name = {'Fey Blessing', '异想的祥光'}

    class FeyBlessing(ActionBase):
        """
        恢复周围队员的体力 恢复力：350 ※该技能无法设置到热键栏

        """
        id = 16544
        name = {'Fey Blessing', '异想的祥光'}

    class SummonSeraph(ActionBase):
        """
        回收小仙女，召唤炽天使 召唤时间：22秒 炽天使在截击状态下，会对体力减少的队员使用炽天的幕帘 炽天使消失后，小仙女会重新被召唤出来 发动条件：小仙女处于同行状态

        """
        id = 16545
        name = {'Summon Seraph', '炽天召唤'}

    class Consolation(ActionBase):
        """
        命令炽天使发动慰藉 恢复周围队员的体力 恢复力：300 追加效果：为目标附加能够抵御一定伤害的防护罩 该防护罩能够抵消相当于治疗量100%的伤害 持续时间：30秒 积蓄次数：2 发动条件：炽天使处于同行状态

        """
        id = 16546
        name = {'Consolation', '慰藉'}

    class Consolation(ActionBase):
        """
        恢复周围队员的体力 恢复力：300 追加效果：为目标附加能够抵御一定伤害的防护罩 该防护罩能够抵消相当于治疗量100%的伤害 持续时间：30秒 ※该技能无法设置到热键栏

        """
        id = 16547
        name = {'Consolation', '慰藉'}

    class SeraphicVeil(ActionBase):
        """
        恢复目标的体力 恢复力：200 追加效果：为目标附加能够抵御一定伤害的防护罩 该防护罩能够抵消相当于治疗量100%的伤害 持续时间：30秒 ※该技能无法设置到热键栏

        1917, 炽天的幕帘, Seraphic Veil, 抵消一定伤害
        2040, 炽天的幕帘, Seraphic Veil, 抵消一定伤害
        """
        id = 16548
        name = {'Seraphic Veil', '炽天的幕帘'}

    class AngelsWhisper(ActionBase):
        """
        持续恢复周围队员的体力 恢复力：120 持续时间：21秒 ※该技能无法设置到热键栏

        1874, 天使的低语, Angel's Whisper, 体力会随时间逐渐恢复
        """
        id = 16550
        name = {'Angel's Whisper', '天使的低语'}

    class SeraphicIllumination(ActionBase):
        """
        一定时间内周围队员发动治疗魔法的治疗量提高10%，受到的魔法伤害减轻5% 持续时间：20秒 无法与小仙女的异想的幻光效果共存 ※该技能无法设置到热键栏

        1875, 炽天的幻光, Seraphic Illumination, 发动治疗魔法的治疗量提高，且受到魔法攻击的伤害减少
        """
        id = 16551
        name = {'Seraphic Illumination', '炽天的幻光'}

    class SummonEos(ActionBase):
        """
        召唤朝日小仙女 朝日小仙女在截击状态下，会对体力减少的队员使用仙光的拥抱

        """
        id = 17215
        name = {'Summon Eos', '朝日召唤'}

    class SummonSelene(ActionBase):
        """
        召唤夕月小仙女 夕月小仙女在截击状态下，会对体力减少的队员使用仙光的拥抱

        """
        id = 17216
        name = {'Summon Selene', '夕月召唤'}

    class Bio(ActionBase):
        """
        对目标附加无属性持续伤害状态 威力：20 持续时间：30秒

        179, 毒菌, Bio, 体力逐渐减少
        """
        id = 17864
        name = {'Bio', '毒菌'}

    class BioIi(ActionBase):
        """
        对目标附加无属性持续伤害状态 威力：40 持续时间：30秒

        189, 猛毒菌, Bio II, 体力逐渐减少
        """
        id = 17865
        name = {'Bio II', '猛毒菌'}

    class Ruin(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：160

        """
        id = 17869
        name = {'Ruin', '毁灭'}

    class RuinIi(ActionBase):
        """
        对目标发动无属性魔法攻击 威力：(source.job==28?(source.level>=72?200:(source.job==28?(source.level>=64?180:(source.job==28?(source.level>=54?160:150):150)):(source.job==28?(source.level>=54?160:150):150))):(source.job==28?(source.level>=64?180:(source.job==28?(source.level>=54?160:150):150)):(source.job==28?(source.level>=54?160:150):150)))

        """
        id = 17870
        name = {'Ruin II', '毁坏'}
