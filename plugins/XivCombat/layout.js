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
<el-form label-position="left" label-width="200px">
    <fpt-bind-item attr="enable_record" :plugin="plugin" v-slot="{value}">
        <el-form-item label="enable_record">
             <el-switch v-model="value.value" />
        </el-form-item>
    </fpt-bind-item>
    <el-divider/>
</el-form>
{{dps_data.zone}}<el-button @click="plugin.run_single('layout_new_monitor')">new</el-button>
<el-table :data="dps_data.members" style="width: 100%" :default-sort = "{prop: 'dps', order: 'descending'}" >
    <el-table-column prop="job" label="职业" sortable width="200"/>
    <el-table-column prop="name" label="名字"/>
    <el-table-column prop="dps" label="dps" width="200" sortable/>
    <el-table-column prop="dpsm" label="dpsm" width="200" sortable/>
</el-table>
<el-divider></el-divider>
<el-table :data="ttk_data" style="width: 100%" :default-sort = "{prop: 'ttk', order: 'ascending'}" >
    <el-table-column prop="name" label="名字"/>
    <el-table-column prop="ttk" label="ttk" sortable/>
</el-table>
`

})
