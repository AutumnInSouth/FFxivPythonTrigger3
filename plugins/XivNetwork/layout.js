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

        vue.onMounted(() => {
            plugin.value.run_single('get_key_to_code').then(data => {
                data.forEach(_d => opcodes.value.push({'codes': _d, 'idx': opcodes.value.length}))
            })
            plugin.value.subscribe('discover', (_, data) => discover_log.value.unshift(data));
        })
        vue.onBeforeUnmount(plugin.value.all_unsubscribe)
        return {plugin, opcodes, discover_log, scope_name, used_opcodes}
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
    </fpt-bind-item>
    <el-table :data="discover_log" style="width: 100%">
        <el-table-column prop="opcode" label="opcode" width="100"/>
        <el-table-column prop="guess" label="guess key" width="200"/>
        <el-table-column prop="event" label="event"/>
        <el-table-column type="expand">
            <template v-slot="{row}">
                {{JSON.stringify(row.struct, null, 2)}}
            </template>
        </el-table-column>
    </el-table>
</div>
`
})
