const scope_name = ["chat", "lobby", "zone"]
module.exports = vue.defineComponent({
    name: 'XivNetwork',
    props: ['plugin'],
    setup(props) {
        const {plugin} = vue.toRefs(props);
        const opcodes = vue.reactive([])
        const discover_log = vue.ref([])
        const scope_name = vue.computed((idx) => scope_name[Math.floor(idx / 2)] + " " + (idx % 2 ? 'server' : 'client'))

        vue.onMounted(() => {
            plugin.run_single('get_key_to_code').then(data => data.forEach(opcodes.push))
            plugin.value.subscribe('discover', (_, data) => discover_log.value.unshift(data));
        })
        vue.onBeforeUnmount(plugin.value.all_unsubscribe)
        return {plugin, opcodes, discover_log, scope_name}
    },
    template: `
<div>
    <el-descriptions v-for="(opcode,i) in opcodes" :key="i" :title="scope_name(i)" direction="vertical" :column="5" border>
        <el-descriptions-item v-for="(code,key) in opcode" :key="code" :label="key">
            {{code}}
        </el-descriptions-item>
    </el-descriptions>
    <fpt-bind-item attr="discover_mode" :plugin="plugin" v-slot="{value}">
        <el-form-item label="测试模式">
            <el-switch v-model="value.value">
        </el-form-item>
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
