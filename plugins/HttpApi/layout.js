module.exports = vue.defineComponent({
    name: 'HttpApi',
    props: ['plugin'],
    setup(props) {
        const {plugin} = vue.toRefs(props);
        const logs = vue.ref([]);
        const config = vue.reactive({'start_default': false, 'port': 2019, 'host': '127.0.0.1'});
        const work = vue.ref(false);
        const on_log = (_, log) => logs.value.push(log)
        const update = () => plugin.value.run_single('get_config').then(data => {
            console.log(data)
            Object.assign(config, data.config)
            work.value = data.work
        })
        const stop_server = () => {
            const loading = element.ElLoading.service({
                lock: true, text: '关闭http api 服务器中...',
                spinner: 'el-icon-loading', background: 'rgba(255,255,255,0.71)'
            })
            plugin.value.run_single('layout_stop_server').then(
                _ => element.ElNotification.success({title: `http api 服务器关闭成功`}),
                err => element.ElNotification.error({title: `http api 服务器关闭失败`, message: err.data}),
            ).then(update).then(loading.close)
        }
        const start_server = () => {
            const loading = element.ElLoading.service({
                lock: true, text: '启动http api 服务器中...',
                spinner: 'el-icon-loading', background: 'rgba(255,255,255,0.71)'
            })
            plugin.value.run_single('layout_start_server').then(
                _ => {
                    element.ElNotification.success({title: `http api 服务器启动中`});
                    work.value = true
                },
                err => element.ElNotification.error({title: `http api 服务器启动失败`, message: err.data}),
            ).then(() => setTimeout(update, 1000)).then(loading.close)
        }

        vue.onMounted(() => {
            plugin.value.subscribe('log', on_log);
            update()
        })
        vue.onBeforeUnmount(() => {
            plugin.value.all_unsubscribe()
        })
        vue.watch(() => config.host, (new_v) => plugin.value.run_single('set_config', ['host', new_v]))
        vue.watch(() => config.port, (new_v) => plugin.value.run_single('set_config', ['port', parseInt(new_v)]))
        vue.watch(() => config.start_default, (new_v) => plugin.value.run_single('set_config', ['start_default', new_v]))
        return {logs, config, work, stop_server, start_server}
    },
    template: `
<div class="terminal">
当前状态：{{work?'运行中':'未运行'}}
<el-button v-if="!work" type="success" @click="start_server" round>启动</el-button>
<el-button v-else type="danger" @click="stop_server" round>停止</el-button>
<el-divider/>
<el-form :inline="true" :model="config">
  <el-form-item label="监听host">
    <el-input :disabled="work" v-model="config.host"/>
  </el-form-item>
  <el-form-item label="监听端口">
    <el-input :disabled="work" type="number" v-model.number="config.port"/>
  </el-form-item>
  <el-form-item label="自启动">
    <el-switch v-model="config.start_default">
</el-switch>
  </el-form-item>
</el-form>
<fpt-log-lines class="h-50" :logs ="logs"/>
</div>
`
})
