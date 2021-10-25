const front_rpc = require("@/libs/rpc/front-rpc");
const app = {
    data() {
        return {
            log_lines: []
        }
    },
    props: ['plugin'],
    methods: {
        on_log(name, log_evt) {
            const msg = `[${new Date(log_evt.timestamp*1000).toUTCString()}|${log_evt.level}|${log_evt.module}] ${log_evt.msg}`
            this.logs.push(msg)
        }
    },
    mounted() {
        front_rpc?.game_subscribe(this.plugin.pid, 'fpt_log', this.on_log)
    },
    beforeUnmount() {
        front_rpc?.game_unsubscribe(this.plugin.pid, 'fpt_log', this.on_log)
    },
    template: `
<p>
    <a v-for="(line,i) in this.log_lines" :key ="i">{{line}}<br/></a>
</p>
`
};
app
