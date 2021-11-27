module.exports = vue.defineComponent({
    name: "XivCombat",
    props: ['plugin'],
    setup(props) {
        const {plugin} = props;
        const dps_data = vue.ref({'zone': 0, 'members': []})
        const ttk_data = vue.ref([])
        let interval = 0;
        vue.onMounted(() => interval = setInterval(() => {
            plugin.run_single('layout_team_dps').then((data) => dps_data.value = data)
            plugin.run_single('layout_enemies_ttk').then((data) => ttk_data.value = data)
        }, 1000));
        vue.onBeforeUnmount(() => clearInterval(interval));
        return {plugin, dps_data, ttk_data}
    },
    template: `
{{dps_data}}<br/>
{{ttk_data}}
`

})
