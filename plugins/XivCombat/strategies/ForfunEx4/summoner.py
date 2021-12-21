from math import radians
from time import perf_counter

from XivCombat.utils import a, s
from XivCombat.strategies import *
from XivCombat import define
from XivCombat.multi_enemy_selector import Rectangle, Sector, select, FarCircle


# pet_name是我自己定义的字典名，这个字典的主要用途通过召唤兽的ID去找到对应召唤兽的名字，这样从data中获取到的id可以转换成名字进行一些比对，
# 可读性更好
pet_name = {
    0: 'NoPet',
    23: 'Carbuncle',
    1: 'Ruby',   # TODO: 红宝石兽，真实ID未填入
    2: 'Topaz',  # TODO: 黄宝石兽，真实ID未填入
    3: 'Emerald',# TODO: 绿宝石兽，真实ID未填入
    27: 'IfritEgi',
    28: 'TitanEgi',
    29: 'GarudaEgi',
    7: 'Ifrit',  # TODO: 大火神，真实ID未填入
    8: 'Titan',  # TODO: 大土神，真实ID未填入
    9: 'Garuda', # TODO: 大风神，真实ID未填入
    10: 'Bahamut',
    14: 'Firebird'
}

# 我自己定义的字典，目的是通过buff（aura）的名字找到对应的buff id，也主要为了增强可读性
# TODO: 三个buffID未填入
summoner_auras = {
    'Further Ruin': 2701,
    'Titan\'s Favor': -1,
    'Garuda\'s Favor': -2,
    'Ifrit\'s Favor': -3
}

# AOE的形状，召唤的所有AOE都是以距离25以内的某目标为圆心，半径5的一个圆圈
# 这里area_shape是我定义的对象名，FarCircle是一个函数调用。函数调用表示程序暂停继续向下执行，而是携带一些参数跳到一个子过程
# 参考：https://www.runoob.com/python/python-functions.html，解释了何为函数以及怎么样调用这个函数
# 带有等号的句子是一个赋值语句，等号左边是一个变量名，右边是一个表达式。所有表达式都有一个运算结果，你可以想象：
# product = 2 * 3这就是一个赋值语句，右边的2*3就是一个表达式，它的运算结果是6，所以这一条赋值语句就是把值6赋给了product这个变量
# 函数调用也是一个表达式，这个表达式的值是运行到return语句时，return关键词后面的值；如果没有return语句，那么这个表达式的值为None
# None是Python所预定义的一个对象， 有关函数调用表达式的值，有如下例子：
'''
这是一个函数定义，以def开头，max是函数名，A和B叫做形式参数，这个函数的作用描述如下：
'我叫max，我是一个函数，我被调用时，调用者必须给我两个数字。
不管这两个数字叫什么，在我这个max函数里就叫他们A和B。
我利用了一段if-else，把A和B中较大的那个给了调用者。'
def max(A, B):
  if A < B:
    return B
  else:
    return A

下面这条语句是一个赋值语句，左侧是一个对象名，右侧是max这个函数的函数调用，这条语句描述如下：
'我叫test = max(shifu_remain, jinfu_remain)， 我是一个语句。执行到我的时候，我总是去计算等号右边的表达式的值。
我看到等号右边是一个函数，这个函数名字叫max，我找到了max的定义就在上面几行。max告诉我，只要我给他两个数字，他就能给我其中较大的那个。
于是我给了它两个数字，一个数字叫shifu_remain，另一个叫jinfu_remain，分别表示士风和阵风buff的剩余时间。这两个叫做实际参数。
我不知道max怎么做的，但反正他给了我两个中较大的那个值。
我拿到了这个值并把它保存一个叫test的对象里面，为了未来其他语句能够方便地使用，而不用再去麻烦max老哥。'
请注意，函数调用时候的参数传递存在顺序，第一个shifu_remain对应到max函数里的A，jinfu_remain对应到B，所有的参数都必须位置一一对应。
test = max(shifu_remain, jinfu_remain)
'''
# 既然FairCircle是一个函数调用，我们需要做的是找到它的函数定义，发现它是在最顶上的XivCombat.multi_enemy_selector这个模块里面引入进来的，
# 我们就可以去
# '前面省略/plugins/XivCombat/multi_enemy_selector.py'
# 这个文件中找到它的定义，请注意你的文件结构树
# 顺便一提当前文件是
# '前面省略/plugins/XivCombat/strategies/ForfunEx4/summoner.py'
area_shape = FarCircle(25, 5)

# 这里定义了一个叫cnt_enemy的函数， 作用是根据传进来的参数data和shape选择一个合适的敌人，
# 并且计算以那个敌人为目标的情况下，使用以shape为形状的AOE，能够覆盖到多少个敌人。python允许return多个值，这个函数里面就return了两个值
# 分别是 一个合适的敌人 和 以这个敌人为目标的情况下，使用以shape为形状的AOE，能够覆盖到的敌人数量
# 所以函数名cnt_enemy就是count enemy，计算敌人数量的意思
def cnt_enemy(data: 'LogicData', shape):
    target, cnt = select(data, data.valid_enemies, shape)
    if not cnt:
        return data.target, 0
    # 下面这句话的意思是，如果玩家手动设置了single这个选项为FORCE_SINGLE，也就是说玩家现在只想打单体技能，那就返回当前他选中的目标，敌人数量为1
    # 这是因为我们要通过这个函数所返回的敌人数量去判断到底使用单体技能还是AOE，如果玩家只想打单体，那函数就直接返回1，
    # 这样用它做判断的时候就会认为范围内可攻击目标只有一个，因而开始打单体技能，满足了玩家的愿望
    if data.config['single'] == define.FORCE_SINGLE:
        return data.target, 1
    # 玩家想要强制打群体技能的情况也是一样的，直接返回3
    if data.config['single'] == define.FORCE_MULTI:
        return data.target, 3
    return target, cnt


# 这是定义了一个叫做SummonerLogic的类，继承了Strategy这个类。类是一种实体，是一类对象的概括性描述（或曰类别），比如说人类就是每个人的类。
# 参考：https://www.runoob.com/python/python-object.html
# 这个类里面主要有两个函数global_cool_down_ability， non_global_cool_down_ability。
# 它们的返回值都是一个函数，可以是UseAbility，这个函数的作用是声明将要使用某个技能了，它接受两个参数，第一个参数是技能ID，第二个参数是目标ID。
# 只要你正确地返回了UseAbility，项目的其他部分会帮你去执行你想要的技能。
# 对于non_global_cool_down_ability，你也可以选择什么都不返回（返回None）；如果你这样做了，那么意味着什么都不做。
# Combat在运行的时候，会去检查当前剩余gcd，如果处于gcd中，则不断地调用non_global_cool_down_ability函数去插入能力技；
# 如果已经插入了2个能力技，就不再去调用non_global_cool_down_ability函数防止过多插入；
# 每个gcd中non_global_cool_down_ability函数调用次数可以达到几百次，最多只有两次会返回技能；
# 如果gcd转好了，就去执行global_cool_down_ability函数
class SummonerLogic(Strategy):
    # 下面三个是类的成员变量，它与成员函数内的变量的区别是生命周期。成员变量的生命周期就是类的生命周期，函数内本地变量的生命周期是函数作用域
    # 参考：https://www.jianshu.com/p/22a8bedc39fd
    # 此为进阶概念，也可以选择不做了解直接抄写
    name = "summoner_logic"
    job = "Summoner"
    gcd = 0  # 这个变量表示当前的总gcd

    # 函数定义，需要注意这个前面有一个缩进，是因为它定义在类中，称为类的"成员函数"。所有成员函数接受的第一个参数都是self，代表这个类对象本身
    # 此函数还接受了第二个参数data，它是被整理好的有关全部所需要的游戏逻辑的对象，里面的值会根据当前游戏状态变动。
    # 其他部分比如说:'LogicData'和后面的->等，是类型约束，不需要深入了解，也可以省略，建议这一行直接复制粘贴即可。
    # 注意！每次调用此函数的时候data里面的值会变动，它表达的是函数被调用的这个时间你的游戏数据
    # 注意！此函数只在GCD转好的时候被调用
    def global_cool_down_ability(self, data: 'LogicData') -> UseAbility | UseItem | UseCommon | None:
        # data.gcd_total获取当前人物总gcd时间，以秒为单位；但它有个怪现象——如果当前没有进入gcd，data.gcd_total的值会是0
        # 因此，直接使用data.gcd_total有时候会是莫名其妙的0，所以我用了self.gcd这个变量暂存起来非0的值，
        # self.开头意味着这是一个类
        self.gcd = data.gcd_total if data.gcd_total > 0 else self.gcd
        # data.target是当前玩家所选中的目标，我把这个值赋给名叫target的对象是为了少打字，只需要写target而不是data.target，下同
        target = data.target
        # 调用了cnt_enemy函数，定义见上
        selected, enemy_count = cnt_enemy(data, area_shape)
        # 职业量谱，量谱中含有哪些东西请参考文件
        # '前面省略/plugins/XivMemory/struct/job_gauge.py'
        # 并找到当前在写的这个职业
        gauge = data.gauge
        # 玩家身上的状态
        effects = data.effects
        # data.pet_id是当前召唤兽id，pet_name[data.pet_id]利用字典把id转换为了名字，所以current_pet是当前召唤兽名字
        current_pet = pet_name[data.pet_id]
        # 下一个连击技能的id
        combo_id = data.combo_id
        # 如果当前没有召唤兽，就召唤最基础的蓝宝石兽
        if current_pet == 'NoPet':
            # a函数把技能名称转换为技能id
            # UseAbility(技能ID，对象ID）声明了将要在id指定的对象身上使用技能id指定的技能
            # 一般情况下没人会去记住每一个技能id，看到了技能id也不会立马想起是哪个技能，所以通过a函数使用技能名称找到技能id
            return UseAbility(a('Summon Carbuncle'), target.id)

        # 如果当前是巴哈姆特或者不死鸟状态，使用三灾或毁三
        if current_pet in ['Bahamut', 'Firebird']:
            return UseAbility(a('Tri-disaster'), selected.id) if enemy_count >= 3 \
                else UseAbility(a('Ruin III'), target.id)

        # 如果召唤巴哈姆特/不死鸟的技能cd转好，就召唤巴哈姆特
        # a函数把技能名称转换为技能id
        # data[技能ID]是查询指定ID对应的技能的剩余冷却时间
        # 所以data[a(技能名称)]是查询指定技能名称的技能剩余冷却时间
        # 这里巴哈姆特和不死鸟可以通过同一个ID使用，所以就用了巴哈姆特
        if data[a('Summon Bahamut')] < self.gcd / 2:
            return UseAbility(a('Summon Bahamut'), target.id)

        # 如果 Ifrit's Favor 这个状态在玩家身上，使用火神冲第一段
        # 如果当前的连击技能是'Crimson Strike'时候，使用火神冲第二段 TODO:未检验可行性
        # 但因为火神冲第一段和第二段实际上都是星极超流'Astral Flow'这个技能，所以下面写为
        # 如果 Ifrit's Favor 这个状态在玩家身上 或者 当前的连击技能是'Crimson Strike'时候：使用'Astral Flow'
        if summoner_auras['Ifrit\'s Favor'] in effects or combo_id == a('Crimson Strike'):
            return UseAbility(a('Astral Flow'), target.id)

        # 如果量谱中还有剩余宝石，则使用'Precious Brilliance'或'Gemshine'
        if gauge.attunement > 0:
            return UseAbility(a('Precious Brilliance'), selected.id) if enemy_count >= 3 \
                else UseAbility(a('Gemshine'), target.id)

        # 如果量谱中titan_ready值为true，就使用'Summon Titan'
        # TODO: titan_ready可以用于判断小火神是不是ready了，但不确定大火神是不是依旧这样判断
        if gauge.titan_ready:
            return UseAbility(a('Summon Titan'), target.id)

        if gauge.garuda_ready:
            return UseAbility(a('Summon Garuda'), target.id)

        if gauge.ifrit_ready:
            return UseAbility(a('Summon Ifrit'), target.id)

        # 如果有'Further Ruin'这个buff在身上就打毁4
        if summoner_auras['Further Ruin'] in effects:
            return UseAbility(a('Ruin IV'), target.id)

        # 否则就打最普通的三灾或者毁三
        return UseAbility(a('Tri-disaster'), target.id) if enemy_count >= 3 \
            else UseAbility(a('Ruin III'), selected.id)

    # 函数定义，用以控制能力技的释放
    # 注意！此函数会在gcd间隙被不间断调用直到gcd转好或其中两次调用产生了返回值（也就是使用了双插能力技）
    def non_global_cool_down_ability(self, data: 'LogicData') -> UseAbility | UseItem | UseCommon | None:
        self.gcd = data.gcd_total if data.gcd_total > 0 else self.gcd
        target = data.target
        selected, enemy_count = cnt_enemy(data, area_shape)
        gauge = data.gauge
        effects = data.effects
        current_pet = pet_name[data.pet_id]

        # 如果'Titan's Favor'这个buff在身上的时候，星极超流'Astral Flow'成为一个能力技，所以放在这个函数里使用
        if summoner_auras['Titan\'s Favor'] in effects:
            return UseAbility(a('Astral Flow'), target.id)

        # 如果'Garuda's Favor'这个buff在身上，就试着双插即刻和星极超流
        # TODO：如果即刻在冷却，应该会出现问题
        if summoner_auras['Garuda\'s Favor'] in effects:
            if not data[a('Swiftcast')]:
                return UseAbility(a('Swiftcast'))
            return UseAbility(a('Astral Flow'), target.id)

        # lucid dreaming
        # 蓝量低于5000且醒梦冷却完毕的情况下使用醒梦
        if not data[7562] and data.me.current_mp < 5000: 
            return UseAbility(7562)

        # TODO: auto searing light
        # if data[a('Searing Light')] <= self.gcd / 2 and current_pet == 'Carbuncle':
        #     return UseAbility(a('Searing Light'), selected.id, wait_until=lambda: 2703 in data.refresh_cache('effects'))

        # 巴哈姆特或者不死鸟状态下，'Enkindle Bahamut'好了就用
        if current_pet in ['Bahamut', 'Firebird'] and data[a('Enkindle Bahamut')] <= self.gcd / 2:
            return UseAbility(a('Enkindle Bahamut'), target.id)

        # 巴哈姆特或者不死鸟状态下，'Astral Flow'好了就用
        if current_pet in ['Bahamut', 'Firebird'] and data[a('Astral Flow')] <= self.gcd / 2:
            return UseAbility(a('Astral Flow'), target.id)

        # 如果当前有以太超流层数，就使用痛苦核爆或者溃烂爆发
        if gauge.aether_flow_stacks > 0:
            return UseAbility(a('Painflare'), selected.id) if enemy_count >= 3 \
                else UseAbility(a('Fester'), selected.id)

        # Aetherflow related
        # 产生以太超流，这里使用16508技能id是因为召学有同名技能Energy Drain，使用技能名称会默认试图使用学者版本的导致用不出来
        if data[16508] <= self.gcd / 2:
            return UseAbility(a('Energy Siphon'), selected.id) if enemy_count >= 3 \
                else UseAbility(16508, selected.id)



