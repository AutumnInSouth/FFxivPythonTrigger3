module.exports = vue.defineComponent({
    name: "XivCombat",
    props: ['plugin'],
    setup(props) {
        const {plugin} = props;
        const dps_data = vue.ref({'zone': 0, 'members': []})
        const ttk_data = vue.ref([])
        const config_data = vue.ref({
            'job': '?',
            'current_strategy': undefined,
            'strategies': [],
            'common_config': {},
            'strategy_config': {},
        })
        const edit_config_data = vue.reactive({
            'current_strategy': undefined,
            'common_config': {},
            'strategy_config': {},
        })
        const reverse_config_data = () => {
            edit_config_data.current_strategy = config_data.value.current_strategy;
            edit_config_data.common_config = {};
            edit_config_data.strategy_config = {};
            for (const [key, value] of Object.entries(config_data.value.common_config))
                edit_config_data.common_config[key] = value.toString()
            for (const [key, value] of Object.entries(config_data.value.strategy_config))
                edit_config_data.strategy_config[key] = value.toString()
        }
        const save = () => {
            if (edit_config_data.current_strategy !== config_data.value.current_strategy)
                plugin.run_single('layout_set', [1, '', edit_config_data.current_strategy])
            for (const [key, value] of Object.entries(config_data.value.common_config))
                if (edit_config_data.common_config[key] !== value.toString())
                    plugin.run_single('layout_set', [2, key, edit_config_data.common_config[key]])
            for (const [key, value] of Object.entries(config_data.value.strategy_config))
                if (edit_config_data.strategy_config[key] !== value.toString())
                    plugin.run_single('layout_set', [3, key, edit_config_data.strategy_config[key]])

        }
        let interval = 0;
        vue.onMounted(() => {
            interval = setInterval(() => {
                plugin.run_single('layout_team_dps').then((data) => dps_data.value = data)
                plugin.run_single('layout_enemies_ttk').then((data) => ttk_data.value = data)
            }, 1000)
            plugin.subscribe('config_update', (_, data) => {
                config_data.value = data
                reverse_config_data()
            })
            setTimeout(() => plugin.run_single('layout_config_update').then(console.log), 1000)
        });
        vue.onBeforeUnmount(() => clearInterval(interval));
        return {plugin, dps_data, ttk_data, config_data, edit_config_data, reverse_config_data, save}
    },
    template: `
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
<el-divider/>
<el-form label-width="200px" class="m-3">
    <fpt-bind-item attr="enable_record" :plugin="plugin" v-slot="{value}">
        <el-form-item label="enable_record">
             <el-switch v-model="value.value" />
        </el-form-item>
    </fpt-bind-item>
    <el-divider/>
        <el-button @click="save">save</el-button>
        <el-button @click="reverse_config_data">reverse</el-button>
    <el-divider>请输入python表达式！</el-divider>
    <el-form-item :label="config_data.job">
        <el-select v-model="edit_config_data.current_strategy">
            <el-option v-for="name in config_data.strategies" :key="name" :label="name" :value="name"/>
        </el-select>
    </el-form-item>
    <el-divider/>
    <el-form-item v-for="(v,k) in edit_config_data.common_config" :key="k" :label="k">
        <input :value="v" @input="edit_config_data.common_config[k]=$event.target.value"/>
        <a> {{typeof config_data.common_config[k]}} </a>
        <i v-if="v!=config_data.common_config[k].toString()" class="el-icon-info"/>
    </el-form-item>
    <el-form-item v-for="(v,k) in edit_config_data.strategy_config" :key="k" :label="k">
        <input :value="v" @input="edit_config_data.strategy_config[k]=$event.target.value"/>
        <a>{{typeof config_data.strategy_config[k]}}</a>
        <i v-if="v!=config_data.strategy_config[k].toString()" class="el-icon-info"/>
    </el-form-item>
</el-form>
<el-divider/>

`

})
