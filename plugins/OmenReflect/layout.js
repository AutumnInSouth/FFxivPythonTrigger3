const filter_obj = (obj, predicate) => Object.keys(obj)
    .filter(key => predicate(obj[key]))
    .reduce((res, key) => (res[key] = obj[key], res), {});
const date_fmt = (epoch) => {
    const d = new Date(epoch);
    return `${d.getHours()}:${d.getMinutes()}:${d.getSeconds()}`;
}
const float_fmt = (num) => {
    if (typeof num !== 'number') num = parseFloat(num);
    return num.toFixed(2);
}
module.exports = vue.defineComponent({
    name: 'OmenReflect',
    props: ['plugin'],
    setup(props) {
        const {plugin} = vue.toRefs(props);
        const action_data = vue.reactive({});
        const actors = vue.reactive({});
        const reset_actors = () => {
            for (const id in actors) delete actors[id];
        }
        const casting_only = vue.ref(true);
        const show_history = vue.ref(0);
        const shown_actor = vue.computed(() => casting_only.value ? filter_obj(actors, (actor) => actor.casting != null) : actors);
        const actor_cast_progress = (actor) =>
            `${float_fmt(actor.cast_info.cast_time)}s/${float_fmt(actor.casting.cast.duration)}s`;


        let countdown = null;

        const update_actors_cast_progress = () => {
            if (countdown) clearTimeout(countdown);
            let need_continue = false;
            const current_time = (new Date()).getTime();
            for (const actor of Object.values(actors)) {
                if (actor.casting) {
                    const new_cast_time = (current_time - actor.casting.epoch) / 1000;
                    const duration = parseFloat(actor.casting.cast.duration);
                    actor.cast_info.cast_time = Math.min(new_cast_time, duration);
                    actor.cast_info.progress = Math.min(new_cast_time / duration * 100, 100);
                    if (new_cast_time >= duration+1) {
                        actor.history.push(actor.casting);
                        actor.casting = null;
                    } else need_continue = true;
                }
            }
            countdown = need_continue ? setTimeout(update_actors_cast_progress, 100) : null;
        }

        const style = document.createElement('style')
        style.setAttribute('type', 'text/css')
        style.innerHTML = `
.OmenReflect .el-collapse-item__header, .OmenReflect .el-collapse-item__wrap{
    background-color: transparent;
}`
        const head = document.getElementsByTagName('head')[0]

        vue.onMounted(() => {
            head.appendChild(style)
            plugin.value.subscribe('actor_cast', (_, data) => {
                const action_id = data.cast.action

                if (!(action_id in action_data)) {
                    action_data[action_id] = {
                        'name': "loading...",
                        'cast_type': "loading...",
                        'effect_range': -1,
                        'x_axis_modifier': -1,
                        'omen': "loading...",
                        'new_omen': "loading...",
                    };
                    plugin.value.run_single('layout_get_action_data', [action_id]).then(
                        data => action_data[action_id] = data
                    );
                }

                if (data.source.id in actors) {
                    const actor = actors[data.source.id];
                    if (actor.casting) actor.history.push(actor.casting);
                    actor.casting = data;
                    actor.cast_info = {
                        'progress': 0,
                        'cast_time': 0,
                    };
                } else {
                    actors[data.source.id] = {
                        'name': data.source.name,
                        'casting': data,
                        'cast_info': {
                            'progress': 0,
                            'cast_time': 0,
                        },
                        'history': [],
                    };
                }

                if (countdown === null) update_actors_cast_progress();
            });
            update_actors_cast_progress();
        })

        vue.onBeforeUnmount(() => {
            head.removeChild(style)
            clearTimeout(countdown);
            plugin.value.all_unsubscribe;
        })
        return {
            plugin,
            action_data,
            actors,
            reset_actors,
            casting_only,
            shown_actor,
            actor_cast_progress,
            show_history,
            date_fmt,
            float_fmt
        }
    },
    template: `
<el-container class="OmenReflect">
    <el-header>   
        <el-form :inline="true">
            <el-form-item label="enable">
                <fpt-bind-item attr="enable_record" :plugin="plugin" v-slot="{value}">
                    <el-switch v-model="value.value"/>
                </fpt-bind-item>
            </el-form-item>
            <el-form-item label="casting_only">
                <el-switch v-model="casting_only"/>
            </el-form-item>
            <el-form-item label="clear data">
                <el-button type="danger" size="mini" @click="reset_actors" circle icon="el-icon-delete"/>
            </el-form-item>
        </el-form>
    </el-header>
    <el-main>
        <div v-for="(actor,actor_id) in shown_actor" :key="actor_id">
            <p>
                {{actor.name}}(0x{{parseInt(actor_id).toString(16)}})
                <el-button @click="show_history = show_history==actor_id?0:actor_id">
                    show history({{actor.history.length}})
                </el-button>
            </p>
            <div class="p-3">
                <el-descriptions v-if="actor.casting" :column="4" border>
                    <el-descriptions-item label="action">
                        <el-popover
                            placement="right"
                            width="400"
                            trigger="click">
                                <el-descriptions border>
                                    <el-descriptions-item label="cast_type">
                                        {{action_data[actor.casting.cast.action].cast_type}}
                                    </el-descriptions-item>
                                    <el-descriptions-item label="effect_range">
                                        {{action_data[actor.casting.cast.action].effect_range}}
                                    </el-descriptions-item>
                                    <el-descriptions-item label="x_axis_modifier">
                                        {{action_data[actor.casting.cast.action].x_axis_modifier}}
                                    </el-descriptions-item>
                                    <el-descriptions-item label="omen">
                                        {{action_data[actor.casting.cast.action].omen}}
                                    </el-descriptions-item>
                                    <el-descriptions-item label="new_omen">
                                        {{action_data[actor.casting.cast.action].new_omen}}
                                    </el-descriptions-item>
                                </el-descriptions>
                                <template v-slot:reference>
                                    <el-button>
                                        {{action_data[actor.casting.cast.action].name}}
                                        (0x{{actor.casting.cast.action.toString(16)}})
                                    </el-button>
                                </template>
                        </el-popover>
                    </el-descriptions-item>
                    <el-descriptions-item label="target">
                        {{actor.casting.target.name}}(0x{{actor.casting.target.id.toString(16)}})
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
                        :percentage="actor.cast_info.progress"/>
                    </el-descriptions-item>
                </el-descriptions>
                <el-table v-if="show_history==actor_id" :data="actor.history">
                    <el-table-column prop="epoch" label="时间">
                        <template v-slot="{row}">
                            {{date_fmt(row.epoch)}}
                        </template>
                    </el-table-column>
                    <el-table-column prop="cast.action" label="动作">
                         <template v-slot="{row}">
                            <el-popover
                                placement="right"
                                width="400"
                                trigger="click">
                                    <el-descriptions border>
                                        <el-descriptions-item label="cast_type">
                                            {{action_data[row.cast.action].cast_type}}
                                        </el-descriptions-item>
                                        <el-descriptions-item label="effect_range">
                                            {{action_data[row.cast.action].effect_range}}
                                        </el-descriptions-item>
                                        <el-descriptions-item label="x_axis_modifier">
                                            {{action_data[row.cast.action].x_axis_modifier}}
                                        </el-descriptions-item>
                                        <el-descriptions-item label="omen">
                                            {{action_data[row.cast.action].omen}}
                                        </el-descriptions-item>
                                        <el-descriptions-item label="new_omen">
                                            {{action_data[row.cast.action].new_omen}}
                                        </el-descriptions-item>
                                    </el-descriptions>
                                    <template v-slot:reference>
                                        <el-button>
                                            {{action_data[row.cast.action].name}}
                                            (0x{{row.cast.action.toString(16)}})
                                        </el-button>
                                    </template>
                            </el-popover>
                        </template>
                    </el-table-column>
                    <el-table-column prop="target" label="目标">
                        <template v-slot="{row}">
                            {{row.target.name}}(0x{{row.target.id.toString(16)}})
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
            </div>
        </div>
    </el-main>
</el-container>
    `
});
