const float_fmt = (num) => {
    if (typeof num !== 'number') num = parseFloat(num);
    return num.toFixed(2);
}
const zpad = (num, pad_len) => ('0'.repeat(pad_len) + num).slice(-pad_len);

const loading_action = {
    'name': "loading...",
    'cast_type': "loading...",
    'effect_range': -1,
    'x_axis_modifier': -1,
    'omen': "loading...",
    'new_omen': "loading..."
}

const action_btn = vue.defineComponent({
    name: 'ActionBtn',
    props: ['aid', 'adata'],
    template: `
<el-popover width="400" trigger="click">
    <el-descriptions border>
        <el-descriptions-item label="id">
            {{aid}}
        </el-descriptions-item>
        <el-descriptions-item label="name">
            {{adata[aid].name}}
        </el-descriptions-item>
        <el-descriptions-item label="cast_type">
            {{adata[aid].cast_type}}
        </el-descriptions-item>
        <el-descriptions-item label="effect_range">
            {{adata[aid].effect_range}}
        </el-descriptions-item>
        <el-descriptions-item label="x_axis_modifier">
            {{adata[aid].x_axis_modifier}}
        </el-descriptions-item>
        <el-descriptions-item label="omen">
            {{adata[aid].omen}}
        </el-descriptions-item>
        <el-descriptions-item label="new_omen">
            {{adata[aid].new_omen}}
        </el-descriptions-item>
    </el-descriptions>
    <template v-slot:reference>
        <el-button>
            {{adata[aid].name}}
            (0x{{aid.toString(16)}})
        </el-button>
    </template>
</el-popover>
`
})


module.exports = vue.defineComponent({
    name: 'OmenReflect',
    props: ['plugin'],
    components: {'action-btn': action_btn,},
    setup(props) {
        const {plugin} = vue.toRefs(props);
        const action_data = vue.reactive({});
        const actors = vue.reactive({});
        const history = vue.ref([]);
        let start_time = 0;
        const history_page = vue.ref(1);
        const history_page_size = vue.ref(10);
        const show_relative_time = vue.ref(false);
        const filter_history = vue.reactive({'source': [], 'action': [],})
        const source_names = vue.ref([]);
        const action_names = vue.computed(() => [...new Set(Object.values(action_data).map(a => a.name))]);

        const filtered_history = vue.computed(() => {
            let data = history.value
            if (filter_history.action.length) data = data.filter(h => filter_history.action.includes(action_data[h.cast.action].name));
            if (filter_history.source.length) data = data.filter(h => filter_history.source.includes(h.source.name));
            return data;
        })

        const shown_history = vue.computed(() => {
            const page_start = (history_page.value - 1) * history_page_size.value;
            return filtered_history.value.slice(page_start, page_start + history_page_size.value);
        });

        const reset = () => {
            filter_history.source = [];
            filter_history.action = [];
            history.value = [];
            source_names.value = [];
            start_time = 0;
            for (key in action_data) delete action_data[key]
        };

        const actor_cast_progress = (actor) => `${float_fmt(actor.info.cast_time)}s/${float_fmt(actor.casting.cast.duration)}s`;

        const date_fmt = (epoch) => {
            if (show_relative_time.value) {
                const dif_ms = epoch - start_time;
                const sec = Math.floor(dif_ms / 1000);
                const min = Math.floor(sec / 60);
                return `${zpad(min, 2)}:${zpad(sec % 60, 2)}.${Math.floor(dif_ms % 1000 / 100)}`;
            } else {
                const d = new Date(epoch);
                return `${zpad(d.getHours(), 2)}:${zpad(d.getMinutes(), 2)}:${zpad(d.getSeconds(), 2)}`;
            }
        }

        let countdown = null;

        const update_actors_cast_progress = () => {
            if (countdown) clearTimeout(countdown);
            let need_continue = false;
            const current_time = (new Date()).getTime();
            for (const [actor_id, actor] of Object.entries(actors)) {
                const new_cast_time = Math.max((current_time - actor.casting.epoch), 0)/ 1000;
                const duration = parseFloat(actor.casting.cast.duration);
                actor.info.cast_time = Math.min(new_cast_time, duration);
                actor.info.progress = Math.min(new_cast_time / duration * 100, 100);
                if (new_cast_time >= duration + 1) delete actors[actor_id];
                else need_continue = true;
            }
            countdown = need_continue ? setTimeout(update_actors_cast_progress, 100) : null;
        }


        vue.onMounted(() => {
            plugin.value.subscribe('actor_cast', (_, data) => {
                const action_id = data.cast.action
                if (!(action_id in action_data)) {
                    action_data[action_id] = {
                        'name': "loading...",
                        'cast_type': "loading...",
                        'effect_range': -1,
                        'x_axis_modifier': -1,
                        'omen': "loading...",
                        'new_omen': "loading..."
                    };
                    plugin.value.run_single('layout_get_action_data', [action_id]).then(data => action_data[action_id] = data);
                }
                actors[data.source.id] = {'casting': data, 'info': {'progress': 0, 'cast_time': 0}};
                history.value.unshift(data);
                if (start_time === 0) start_time = data.epoch;
                if (!source_names.value.includes(data.source.name)) source_names.value.push(data.source.name);
                if (countdown === null) update_actors_cast_progress();
            });
            update_actors_cast_progress();
        })

        vue.onBeforeUnmount(() => {
            plugin.value.all_unsubscribe;
            clearTimeout(countdown);
        })
        return {
            plugin,
            action_data,
            actors,
            history,
            history_page,
            history_page_size,
            filter_history,
            source_names,
            action_names,
            reset,
            actor_cast_progress,
            date_fmt,
            show_relative_time,
            shown_history,
            filtered_history,
            float_fmt
        }
    },
    template: `
<el-container class="OmenReflect">
    <el-header>   
        <el-form :inline="true">
            <el-form-item label="show_player_skill_omen">
                <fpt-bind-item attr="show_player_skill_omen" :plugin="plugin" v-slot="{value}">
                    <el-switch v-model="value.value"/>
                </fpt-bind-item>
            </el-form-item>
            <el-form-item label="enable">
                <fpt-bind-item attr="enable_record" :plugin="plugin" v-slot="{value}">
                    <el-switch v-model="value.value"/>
                </fpt-bind-item>
            </el-form-item>
            <el-form-item label="show_relative_time">
                <el-switch v-model="show_relative_time"/>
            </el-form-item>
            <el-form-item label="clear data">
                <el-button type="danger" size="mini" @click="reset" circle icon="el-icon-delete"/>
            </el-form-item>
        </el-form>
    </el-header>
    <el-main>
        <el-tabs>
            <el-tab-pane label="current" class="px-2">
                <div v-for="(actor,actor_id) in actors" :key="actor_id" class="p-3">
                     <el-descriptions v-if="actor.casting" :column="4" border>
                        <template v-slot:title>
                            {{actor.casting.source.name}}(0x{{parseInt(actor_id).toString(16)}})
                        </template>
                        <el-descriptions-item label="action">
                            <action-btn :aid="actor.casting.cast.action" :adata="action_data"/>
                        </el-descriptions-item>
                        <el-descriptions-item label="target">
                            <a v-if="actor.casting.target.id == 0xe0000000">-</a>
                            <a v-else-if="actor.casting.target.id == actor.casting.source.id">self</a>
                            <a v-else>{{actor.casting.target.name}}(0x{{actor.casting.target.id.toString(16)}})</a>
                        </el-descriptions-item>
                        <el-descriptions-item label="position">
                            {{float_fmt(actor.casting.cast.position.x)}},
                            {{float_fmt(actor.casting.cast.position.y)}},
                            {{float_fmt(actor.casting.cast.position.z)}}
                            （{{float_fmt(actor.casting.cast.position.r)}}）
                        </el-descriptions-item>
                        <el-descriptions-item label="delay">
                            {{actor.casting.cast.delay}}
                        </el-descriptions-item>
                        <el-descriptions-item :span="2" label="progress">
                            <el-progress
                            v-if="actor.casting"
                            :format="()=>actor_cast_progress(actor,actor_id)" 
                            :stroke-width="24" 
                            style="min-width: 500px"
                            :percentage="actor.info.progress"/>
                        </el-descriptions-item>
                    </el-descriptions>
                </div>
            </el-tab-pane>
            <el-tab-pane class="bg-white rounded-bottom p-2" label="history">
                <el-form  :model="filter_history" :inline="true">
                    <el-form-item label="source" >
                        <el-select-v2 style="min-width: 300px" v-model="filter_history.source" :options="source_names.map(n => ({value: n, label:n}))" filterable multiple clearable/>
                    </el-form-item>
                    <el-form-item label="action">
                        <el-select-v2 style="min-width: 300px" v-model="filter_history.action" :options="action_names.map(n => ({value: n, label:n}))" filterable multiple clearable/>
                    </el-form-item>
                </el-form>
                 <el-pagination v-model:currentPage="history_page" :page-size="history_page_size" layout="prev,pager,next,jumper" :total="filtered_history.length"/>
                 <el-table :data="shown_history">
                    <el-table-column prop="epoch" label="时间">
                        <template v-slot="{row}">
                            {{date_fmt(row.epoch)}}
                        </template>
                    </el-table-column>
                    <el-table-column prop="source" label="来源">
                        <template v-slot="{row}">
                            {{row.source.name}}(0x{{row.source.id.toString(16)}})
                        </template>
                    </el-table-column>
                    <el-table-column prop="cast.action" label="动作">
                        <template v-slot="{row}">
                            <action-btn :aid="row.cast.action" :adata="action_data"/>
                        </template>
                    </el-table-column>
                    <el-table-column prop="target" label="目标">
                        <template v-slot="{row}">
                            <a v-if="row.target.id == 0xe0000000">-</a>
                            <a v-else-if="row.target.id == row.source.id">self</a>
                            <a v-else>{{row.target.name}}(0x{{row.target.id.toString(16)}})</a>
                        </template>
                    </el-table-column>
                    <el-table-column prop="cast.position" label="目标地点">
                        <template v-slot="{row}">
                            {{float_fmt(row.cast.position.x)}},
                            {{float_fmt(row.cast.position.y)}},
                            {{float_fmt(row.cast.position.z)}}
                            （{{float_fmt(row.cast.position.r)}}）
                        </template>
                    </el-table-column>
                    <el-table-column prop="cast.duration" label="时长">
                         <template v-slot="{row}">
                            {{float_fmt(row.cast.duration)}}
                        </template>
                    </el-table-column>
                    <el-table-column prop="cast.delay" label="延迟">
                    </el-table-column>
                </el-table>
            </el-tab-pane>
        </el-tabs>
        
    </el-main>
</el-container>
    `
});
