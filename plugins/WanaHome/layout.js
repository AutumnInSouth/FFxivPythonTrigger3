module.exports = vue.defineComponent({
    name: 'WanaHome',
    props: ['plugin'],
    setup(props) {
        const {plugin} = vue.toRefs(props);
        const logs = vue.ref();
        const on_log = (_, log) => logs.value.log(utils.format_fpt_log(log), log.level)
        const empty_house = vue.ref([]);

        vue.onMounted(() => {
            plugin.value.subscribe('log', on_log);
            plugin.value.subscribe('empty_house', (_, data) => empty_house.value = data).then(() => {
                plugin.value.run_single('update_client')
            });

        })
        vue.onBeforeUnmount(() => {
            plugin.value.all_unsubscribe()
        })
        return {logs, plugin, empty_house}
    },
    template: `
<el-button @click="plugin.run_single('full_search')">search</el-button>
<fpt-bind-item attr="auto_search_period" :plugin="plugin" v-slot="{value}">
    <el-slider v-model="value.value" :step="30" :min="0" :max="600" show-input/>
</fpt-bind-item>
<p v-for="house in empty_house">
    <el-link @click="plugin.run_single('goto',[],house.data)"
    >{{house.name}}</el-link>  {{house.price}} {{new Date(house.start*1000).toUTCString()}}
</p>
<div style="height:50%;max-height:50%">
    <log-lines ref ="logs"/>
</div>
`
})
