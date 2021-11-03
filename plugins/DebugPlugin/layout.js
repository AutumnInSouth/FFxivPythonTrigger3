module.exports = vue.defineComponent({
    name: 'Debug',
    props: ['plugin'],
    setup(props) {
        const {plugin} = vue.toRefs(props);
        const logs = vue.ref();
        const on_log = (_, log) => logs.value.log(utils.format_fpt_log(log), log.level)

        vue.onMounted(() => {
            plugin.value.subscribe('log', on_log);
        })
        vue.onBeforeUnmount(() => {
            plugin.value.all_unsubscribe()
        })
        return {logs, }
    },
    template: `
<log-lines style="max-height:100%" ref ="logs"/>
`
})
