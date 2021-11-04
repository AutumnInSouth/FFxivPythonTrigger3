module.exports = vue.defineComponent({
    name: 'Pmb',
    props: ['plugin'],
    setup(props) {
        const {plugin} = vue.toRefs(props);
        const market_list = vue.ref([])
        const item_id = vue.ref(0)
        const item_list = vue.ref([])
        const game_data = plugin.value.game_data
        const input1 = vue.ref('')
        const query = (_item_id) => {
            const loading = element.ElLoading.service({
                lock: true, text: '搜索中。。。',
                spinner: 'el-icon-loading', background: 'rgba(255,255,255,0.71)'
            })
            return plugin.value.run_single('query', [_item_id]).then(
                data => {
                    item_id.value = _item_id
                    market_list.value = data
                },
                err => {
                    element.ElNotification.error({title: `搜索失败`, message: err.data})
                    console.error(err.trace)
                }
            ).then(loading.close)
        }
        const buy = (idx) => plugin.value.run_single('buy', [market_list.value[idx]]).then(
            data => {
                market_list.value.splice(idx, 1)
            },
            err => {
                element.ElNotification.error({title: `购买失败`, message: err.data})
                console.error(err.trace)
            }
        )
        const filter_item = () => {
            item_list.value = []
            for (const [key, name] of Object.entries(game_data().item_names))
                if (name.includes(input1.value) || key.includes(input1.value)) {
                    item_list.value.push({key: key, name: name})
                    if (item_list.value.length >= 100) break
                }
            console.log(item_list.value)
        }
        return {market_list, item_id, item_list,input1, query, buy, game_data, filter_item}
    },
    template: `
<el-container>
    <el-aside width="300px">
        <el-input v-model="input1" placeholder="物品名称/id" clearable>
            <template v-slot:append>
                <el-button @click="filter_item" icon="el-icon-search"/>
            </template>
        </el-input>
        <el-badge v-for="item in item_list" :key="item.key" :value="item.key" class="m-3 w-75" type="primary">
            <el-button @click="query(parseInt(item.key))" class="w-100" size="small">{{item.name}}</el-button>
        </el-badge>
    </el-aside>
    <el-container v-if="item_id">
        <el-header>
            {{game_data().item_names[item_id]}}
        </el-header>
        <el-main>
            <div v-for="(item,i) in market_list" :key="i" class="m-2 w-100">
                <el-button @click="buy(i)" class="w-100">
                    {{game_data().item_names[item_id]}}<a v-if="item.is_hq">&#xe03c</a>--
                    {{item.price_per_unit}}Gx{{item.total_item_count}} +{{item.total_tax}}
                    = {{item.price_per_unit*item.total_item_count+item.total_tax}}G
                    ({{item.retainer_name}})
                </el-button>
            </div>
        </el-main>
    </el-container>
    <el-main v-else>
        <el-empty description="请选择物品进行搜索"/>
    </el-main>
</el-container>
`
})
