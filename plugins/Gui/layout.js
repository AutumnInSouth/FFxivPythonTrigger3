module.exports = vue.defineComponent({
    name: 'Gui',
    props: ['plugin'],
    setup(props) {
        const {plugin} = vue.toRefs(props);
        return {plugin}
    },
    template: `
<el-form label-position="left" label-width="200px">
     <fpt-bind-item attr="font_size" :plugin="plugin" v-slot="{value}">
        <el-form-item label="font_size">
            <el-slider v-model="value.value" :step="1" :min="5" :max="20" show-input/>
        </el-form-item>
    </fpt-bind-item>
     <fpt-bind-item attr="font_path" :plugin="plugin" v-slot="{value}">
        <el-form-item label="font_path">
             <input style="width: 100%" v-model="value.value" />
        </el-form-item>
    </fpt-bind-item>
     <fpt-bind-item attr="separate_thread" :plugin="plugin" v-slot="{value}">
        <el-form-item label="separate_thread">
             <el-switch v-model="value.value" />
        </el-form-item>
    </fpt-bind-item>
</el-form>
    `
});
