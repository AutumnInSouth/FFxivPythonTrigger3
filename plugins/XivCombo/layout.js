module.exports = vue.defineComponent({
    name: 'XivCombo',
    props: ['plugin'],
    setup(props) {
        const {plugin} = vue.toRefs(props);
        const all_combo = vue.ref({})
        const combo_select = vue.ref()
        const select_combo = (action_id, combo_id) => {
            if (combo_select.value.value.value[action_id]===combo_id)
                delete combo_select.value.value.value[action_id]
            else combo_select.value.value.value[action_id]=combo_id
        }
        vue.onMounted(()=>plugin.value.run_single('get_all_combo').then(data => all_combo.value = data))
        return {all_combo, select_combo, combo_select,plugin}
    },
    template: `
<div>
    <fpt-bind-item ref="combo_select" attr="combo_select" :plugin="plugin" v-slot="{value}">
        <div v-for="(combos,action_id) in all_combo" class="my-3 p-3 border rounded bg-twhite">
            {{plugin.game_data()?plugin.game_data().action_names[action_id]:action_id}}：
            <el-button v-for="(combo,combo_id) in combos" size="small"
                :type="value.value[action_id]===combo_id?'success':'info'"
                @click="select_combo(action_id,combo_id)">
                {{combo.title}}<a v-if="combo.desc"> - {{combo.desc}}</a>
            </el-button>
        </div>
    </fpt-bind-item>
</div>
`
})
