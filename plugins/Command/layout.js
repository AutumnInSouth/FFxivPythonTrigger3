styles = `
.input-with-select .el-input {
    width: 130px;
}
.input-with-select .el-input-group__prepend {
    background-color: #fff;
}
`
module.exports = vue.defineComponent({
    name: 'commands',
    setup(props) {
        const {plugin} = vue.toRefs(props);
        const commands = vue.ref({})
        const select = vue.ref("")
        const input = vue.ref("")
        const style = document.createElement('style')
        style.setAttribute('type', 'text/css')
        style.innerHTML = styles
        const head = document.getElementsByTagName('head')[0]

        const process = () => plugin.value.run_single('process_command', [`${select.value} ${input.value}`])
        const scripts = vue.ref([])

        const update_scripts = () => plugin.value.run_single('list_script').then(data => scripts.value = data)
        const stop_script = (script_id) => plugin.value.run_single('stop_script', [script_id])

        vue.onMounted(() => {
            head.appendChild(style)
            plugin.value.run_single('command_list').then(data => commands.value = data)
            plugin.value.subscribe('update_scripts', (_, data) => scripts.value = data)
            update_scripts()
        })
        vue.onBeforeUnmount(() => {
            head.removeChild(style)
            plugin.value.all_unsubscribe()
        })

        return {commands, select, input, process, update_scripts, scripts, stop_script}
    },
    props: ['plugin'],
    template: `
<div>
    <el-input v-model="input" class="input-with-select" placeholder="请输入内容" clearable>
        <template v-slot:prepend>
            <el-select placeholder="指令" v-model="select">
                <el-option v-for="(v,k) in commands" :key="k" :label="k" :value="k"/>
            </el-select>
        </template>
        <template v-slot:append>
            <el-button @click="process" icon="el-icon-caret-right"/>
        </template>
    </el-input>
    
    <el-table :data="scripts" style="width: 100%">
        <el-table-column prop="id" label="id">
            <template v-slot:header>
                <el-button @click="update_scripts">scripts reload</el-button>
            </template>
        </el-table-column>
        <el-table-column prop="name" label="name"/>
        <el-table-column prop="argus" label="argus"/>
        <el-table-column prop="is_alive" label="is_alive"/>
         <el-table-column fixed="right" label="操作" width="100">
          <template  v-slot="{row}">
            <el-button @click="stop_script(row.id)" type="text" size="small">停止</el-button>
          </template>
        </el-table-column>
    </el-table>
</div>
`
})
