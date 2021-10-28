module.exports = vue.defineComponent({
    name: 'XivNetwork',
    props: ['plugin'],
    setup(props) {
        const {plugin} = vue.toRefs(props);
        const opcodes = vue.reactive([])
        const discover_log = vue.ref([])

        function on_discover() {

        }

        vue.onMounted(() => {
            plugin.run_single('get_key_to_code').then(data => data.forEach(opcodes.push))
            plugin.value.subscribe('discover', on_discover);
        })
        vue.onBeforeUnmount(plugin.value.all_unsubscribe)
        return {plugin, opcodes, discover_log}
    },
    template: `
<div>
    <fpt-bind-item attr="discover_mode" :plugin="plugin" v-slot="{value}">
        <el-form-item label="测试模式">
            <el-switch v-model="value.value">
        </el-form-item>
    </fpt-bind-item>
</div>
`
})
