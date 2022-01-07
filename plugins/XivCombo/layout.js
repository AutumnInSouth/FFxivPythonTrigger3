module.exports = vue.defineComponent({
    name: 'XivCombo',
    props: ['plugin'],
    setup(props) {
        const {plugin} = vue.toRefs(props);
        const all_combo = vue.ref({})
        const actions_data = vue.ref({})
        const job_actions = vue.reactive({})
        const combo_select = vue.ref()
        const init_cnt = vue.ref(0)
        const select_combo = (action_id, combo_id) => {
            if (combo_select.value.value.value[action_id] === combo_id)
                delete combo_select.value.value.value[action_id]
            else combo_select.value.value.value[action_id] = combo_id
        }

        const style = document.createElement('style')
        style.setAttribute('type', 'text/css')
        style.innerHTML = `
.XivCombo .el-collapse-item__header, .XivCombo .el-collapse-item__wrap{
    background-color: transparent;
}
`
        const head = document.getElementsByTagName('head')[0]

        vue.onMounted(() => {
            head.appendChild(style)
            plugin.value.run_single('get_all_combo').then(data => {
                all_combo.value = data
                init_cnt.value += 1
            })
            plugin.value.run_single('get_actions_data').then(data => {
                actions_data.value = data
                for (const [action_id_str, {name, category}] of Object.entries(data)) {
                    if (!(category in job_actions)) job_actions[category] = []
                    job_actions[category].push(parseInt(action_id_str))
                }
                init_cnt.value += 1
            })
        })

        vue.onBeforeUnmount(() => {
            head.removeChild(style)
        })

        return {all_combo, select_combo, combo_select, plugin, init_cnt, actions_data, job_actions}
    },
    template: `
<div class="XivCombo">
    <fpt-bind-item v-if='init_cnt>=2' :default_value="{}" ref="combo_select" attr="combo_select" :plugin="plugin" v-slot="{value}">
        <el-collapse accordion>
            <el-collapse-item :title="job" v-for="(actions,job) in job_actions" :key="job">
                <div v-for="action_id in actions" :key="action_id" class="my-3 p-3 border rounded bg-twhite">
                    {{actions_data[action_id].name}}：
                    <el-button v-for="(combo,combo_id) in all_combo[action_id]" size="small"
                        :type="value.value[action_id]===combo_id?'success':'info'"
                        @click="select_combo(action_id,combo_id)">
                        {{combo.title}}
                    </el-button>
                </div>
            </el-collapse-item>
        </el-collapse>
    </fpt-bind-item>
</div>
`
})
