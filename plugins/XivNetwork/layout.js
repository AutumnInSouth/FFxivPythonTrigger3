const _scope_name = ["chat", "lobby", "zone"]
module.exports = vue.defineComponent({
    name: 'XivNetwork',
    props: ['plugin'],
    setup(props) {
        const {plugin} = vue.toRefs(props);
        const opcodes = vue.ref([])
        const discover_log = vue.ref([])
        const scope_name = (idx) => _scope_name[Math.floor(idx / 2)] + " " + (idx % 2 ? 'server' : 'client')
        const used_opcodes = vue.computed(() => opcodes.value.filter(op => Object.keys(op.codes).length))
        const search_key = vue.ref('')
        vue.onMounted(() => {
            plugin.value.run_single('get_key_to_code').then(data => {
                data.forEach(_d => opcodes.value.push({'codes': _d, 'idx': opcodes.value.length}))
            })
            plugin.value.subscribe('discover', (_, data) => discover_log.value.unshift(data));
        })
        vue.onBeforeUnmount(plugin.value.all_unsubscribe)
        return {plugin, opcodes, discover_log, scope_name, used_opcodes, search_key}
    },
    template: `
<div>
    <el-tabs>
        <el-tab-pane v-for="opcode in used_opcodes" :key="opcode.idx" :label="scope_name(opcode.idx)">
            <el-tag class="mx-2 my-1" type="success" v-for="(code,key) in opcode.codes">{{key}}：{{code}}</el-tag>
        </el-tab-pane>
    </el-tabs>
    <fpt-bind-item attr="discover_mode" :plugin="plugin" v-slot="{value}">
        <el-form>
            <el-form-item label="测试模式">
                <el-switch v-model="value.value"/>
            </el-form-item>
        </el-form>
        <el-table style="width: 100%" :data="discover_log.filter(data=>data.guess.toLowerCase().includes(search_key.toLowerCase()))">
            <el-table-column prop="opcode" label="opcode" width="100">
            <template v-slot:header>
                <el-button type="danger" @click="discover_log = []" placeholder="输入关键字搜索">
                    清除
                </el-button>
            </template>
            <template v-slot="{row}">
                0x{{row.opcode.toString(16)}}
            </template>
            </el-table-column>
            <el-table-column prop="guess" label="guess key" width="250">
                <template v-slot:header>
                    <el-input
                      v-model="search_key"
                      size="mini"
                      placeholder="输入关键字搜索"/>
                  </template>
            </el-table-column>
            <el-table-column prop="event" label="event"/>
            <el-table-column type="expand">
                <template v-slot="{row}">
                    {{JSON.stringify(row.struct, null, 2)}}
                </template>
            </el-table-column>
        </el-table>
    </fpt-bind-item>
</div>
`
})
