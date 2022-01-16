module.exports = vue.defineComponent({
    name: 'MoAction',
    props: ['plugin'],
    setup(props) {
        const {plugin} = vue.toRefs(props);
        return {plugin}
    },
    template: `
<el-form label-position="left" label-width="200px">
     <fpt-bind-item attr="set_mo" :plugin="plugin" v-slot="{value}">
        <el-form-item label="enable mouse over">
             <el-switch v-model="value.value" />
        </el-form-item>
    </fpt-bind-item>
     <fpt-bind-item attr="set_tt" :plugin="plugin" v-slot="{value}">
        <el-form-item label="enable target -> target">
             <el-switch v-model="value.value" />
        </el-form-item>
    </fpt-bind-item>
     <fpt-bind-item attr="ac_in_queue" :plugin="plugin" v-slot="{value}">
        <el-form-item label="ac_in_queue">
             <el-switch v-model="value.value" />
        </el-form-item>
    </fpt-bind-item>
</el-form>
    `
});
