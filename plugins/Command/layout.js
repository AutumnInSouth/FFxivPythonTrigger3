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
        const log_lines = vue.ref([])
        const commands = vue.ref({})
        const select = vue.ref("")
        const input = vue.ref("")
        const style = document.createElement('style')
        style.setAttribute('type', 'text/css')
        style.innerHTML = styles
        const head = document.getElementsByTagName('head')[0]

        const on_log = (_, evt) => log_lines.value.push(
            `[${new Date(evt.timestamp * 1000).toUTCString()}|${evt.level}|${evt.module}] ${evt.msg}`
        )

        const process = () => plugin.value.run_single('process_command', [`${select.value} ${input.value}`])

        vue.onMounted(() => {
            head.appendChild(style)
            plugin.value.run_single('command_list').then(data => commands.value = data)
            front_rpc.front_rpc?.game_subscribe(plugin.value.pid, 'fpt_log', on_log)
        })
        vue.onBeforeUnmount(() => {
            head.removeChild(style)
            front_rpc.front_rpc?.game_unsubscribe(plugin.value.pid, 'fpt_log', on_log)
        })

        return {log_lines, commands, select, input, process}
    },
    props: ['plugin'],
    template: `
<div class="terminal">
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
    <p v-for="(line,i) in this.log_lines" :key ="i">{{line}}</p>
</div>
`
})
