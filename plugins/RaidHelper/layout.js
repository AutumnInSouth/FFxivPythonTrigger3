module.exports = vue.defineComponent({
    name: 'RaidHelper',
    props: ['plugin'],
    setup(props) {
        const {plugin} = vue.toRefs(props);
        const init_cnt = vue.ref(0)
        const all_triggers = vue.ref({});
        const map_names = vue.ref({});

        const style = document.createElement('style')
        style.setAttribute('type', 'text/css')
        style.innerHTML = `
.RaidHelper .el-collapse-item__header, .RaidHelper .el-collapse-item__wrap{
    background-color: transparent;
}
`
        const head = document.getElementsByTagName('head')[0]

        vue.onMounted(() => {
            head.appendChild(style)
            plugin.value.run_single('layout_get_triggers_list').then(data => {
                all_triggers.value = data
                init_cnt.value += 1
            })
            plugin.value.run_single('map_names').then(data => {
                map_names.value = data
                init_cnt.value += 1
            })
        })
        vue.onBeforeUnmount(() => {
            head.removeChild(style)
        })
        return {plugin, init_cnt, all_triggers, map_names}
    },
    template: `
<div class="RaidHelper">
    <el-form :inline="true">
        <el-form-item label="in game output">
            <fpt-bind-item attr="in_game_output" :plugin="plugin" v-slot="{value}">
                <el-select v-model="value.value" placeholder="in game output">
                    <el-option label="no" :value="0"></el-option>
                    <el-option label="echo" :value="1"></el-option>
                    <el-option label="party" :value="2"></el-option>
                </el-select>
            </fpt-bind-item>
        </el-form-item>
        <el-form-item label="in game output se">
            <fpt-bind-item attr="in_game_output_sound_effect" :plugin="plugin" v-slot="{value}">
                <el-select v-model="value.value" placeholder="in game output se">
                    <el-option label="no" :value="0"></el-option>
                    <el-option v-for="i in 13" :label="i" :value="i" :key="i"></el-option>
                </el-select>
            </fpt-bind-item>
        </el-form-item>
    </el-form>
    <fpt-bind-item :default_value="{}" attr="enable_triggers" :plugin="plugin" v-slot="{value}">
            <el-collapse v-if='init_cnt >= 2' accordion>
                <el-collapse-item :title="map_names[map_id]" v-for="(triggers,map_id) in all_triggers" :key="map_id">
                    <div v-for="name in triggers" :key="name" class="my-3 p-3 border rounded bg-twhite">
                    {{name}}：<el-switch v-model="value.value[map_id][name]" />
                </div>
                </el-collapse-item>
            </el-collapse>
    </fpt-bind-item>
</div>
`
});
