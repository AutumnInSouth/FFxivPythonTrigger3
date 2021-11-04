module.exports = vue.defineComponent({
    name: 'Pmb',
    props: ['plugin'],
    setup(props) {
        const {plugin} = vue.toRefs(props);
        const market_list = vue.ref([])
        const item_id = vue.ref(0)
        const item_list = vue.reactive([])
        const game_data = plugin.game_data()
        const input = vue.ref('')
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
        const buy = (idx) => plugin.value.run_single('buy', [item_list.value[idx]]).then(
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
            for (const [key, name] of Object.entries(game_data.item_names))
                if (name.includes(input.value) || key.includes(input.value)) {
                    item_list.value.push({key: key, name: name})
                    if (item_list.value.length >= 100) break
                }
        }
        return {market_list, item_id, item_list, query, buy, game_data, filter_item}
    },
    template: `
<el-container>
    <el-aside width="300px">
        <el-input v-model="input" placeholder="物品名称/id" clearable>
            <template v-slot:append>
                <el-button @click="filter_item" icon="el-icon-caret-search"/>
            </template>
        </el-input>
        <el-badge v-for="(i_name,i_id) in item_list" :key="i_id" :value="i_id" class="m-3" type="primary">
            <el-button class="w-100" size="small">{{i_name}}</el-button>
        </el-badge>
    </el-aside>
    <el-container v-if="item_id">
        <el-header>
            {{game_data.item_names[item_id]}}
        </el-header>
        <el-main>
            main
        </el-main>
    </el-container>
    <el-main v-else>
        <el-empty description="请选择物品进行搜索"/>
    </el-main>
</el-container>
`
})