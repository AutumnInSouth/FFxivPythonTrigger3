module.exports = vue.defineComponent({
    name: 'WanaHome',
    props: ['plugin'],
    setup(props) {
        const {plugin} = vue.toRefs(props);
        const logs = vue.ref();
        const on_log = (_, log) => logs.value.log(utils.format_fpt_log(log), log.level)
        const empty_house = vue.ref([]);
        const go_to_data = vue.reactive({
            territory_id: 0,
            ward_id: 0,
            house_id: 0,
        });
        const go_to = () => {
            plugin.value.run_single('goto', [], {
                territory_id: go_to_data.territory_id,
                ward_id: go_to_data.ward_id - 1,
                house_id: go_to_data.house_id - 1,
            })
        }
        vue.onMounted(() => {
            plugin.value.subscribe('log', on_log);
            plugin.value.subscribe('empty_house', (_, data) => empty_house.value = data).then(() => {
                plugin.value.run_single('update_client')
            });

        })
        vue.onBeforeUnmount(() => {
            plugin.value.all_unsubscribe()
        })
        return {logs, plugin, empty_house, go_to_data, go_to}
    },
    template: `
<el-form :inline="true" :model="go_to_data" >
  <el-select v-model="go_to_data.territory_id" placeholder="地图">
      <el-option :label="k" :value="v" v-for="(v,k) in {'海': 339, '沙': 341, '森': 340, '白': 641}"></el-option>
    </el-select>
  <el-form-item label="房区">
    <el-input v-model="go_to_data.ward_id"/>
  </el-form-item>
  <el-form-item label="房号">
    <el-input v-model="go_to_data.house_id"/>
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="go_to">传送</el-button>
  </el-form-item>
</el-form>
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
