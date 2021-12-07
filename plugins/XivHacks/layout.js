const zoom_property_default = {zoom: {min: 0, max: 0}, fov: {min: 0, max: 0}, angle: {min: 0, max: 0}}
module.exports = vue.defineComponent({
    name: 'XivCombo',
    props: ['plugin'],
    setup(props) {
        const {plugin} = vue.toRefs(props);
        return {plugin, zoom_property_default}
    },
    template: `
<el-form label-position="left" label-width="200px">
    <h4>Combat</h4>
    <fpt-bind-item attr="speed_percent" :plugin="plugin" v-slot="{value}">
        <el-form-item label="move speed">
             <el-slider v-model="value.value" :step="0.05" :min="0" :max="2" show-input/>
        </el-form-item>
    </fpt-bind-item>
    <fpt-bind-item attr="swing_reduce" :plugin="plugin" v-slot="{value}">
        <el-form-item label="swing reduce">
             <el-slider v-model="value.value" :step="0.01" :min="0" :max="10" show-input/>
        </el-form-item>
    </fpt-bind-item>
    <fpt-bind-item attr="skill_animation_lock_time" :plugin="plugin" v-slot="{value}">
        <el-form-item label="skill ani lock">
             <el-slider v-model="value.value" :step="0.01" :min="0" :max="1" show-input/>
        </el-form-item>
    </fpt-bind-item>
    <fpt-bind-item attr="skill_animation_lock_local" :plugin="plugin" v-slot="{value}">
        <el-form-item label="skill ani lock local">
             <el-switch v-model="value.value" />
        </el-form-item>
    </fpt-bind-item>
    <fpt-bind-item attr="hit_box_adjust" :plugin="plugin" v-slot="{value}">
        <el-form-item label="hit box adjust">
             <el-slider v-model="value.value" :step="0.5" :min="-5" :max="5" show-input/>
        </el-form-item>
    </fpt-bind-item>
    <fpt-bind-item attr="anti_knock" :plugin="plugin" v-slot="{value}">
        <el-form-item label="anti knock">
             <el-switch v-model="value.value" />
        </el-form-item>
    </fpt-bind-item>
    <fpt-bind-item attr="ninja_stiff" :plugin="plugin" v-slot="{value}">
        <el-form-item label="ninja stiff">
             <el-switch v-model="value.value" />
        </el-form-item>
    </fpt-bind-item>
    <fpt-bind-item attr="afix_enable" :plugin="plugin" v-slot="{value}">
        <el-form-item label="afix enable">
             <el-switch v-model="value.value" />
        </el-form-item>
    </fpt-bind-item>
    <fpt-bind-item attr="afix_distance" :plugin="plugin" v-slot="{value}">
        <el-form-item label="afix effective distance">
             <el-slider v-model="value.value" :step="0.1" :min="0" :max="10" show-input/>
        </el-form-item>
    </fpt-bind-item>
    <fpt-bind-item attr="moving_swing_enable" :plugin="plugin" v-slot="{value}">
        <el-form-item label="moving swing enable">
             <el-switch v-model="value.value" />
        </el-form-item>
    </fpt-bind-item>
    <fpt-bind-item attr="moving_swing_time" :plugin="plugin" v-slot="{value}">
        <el-form-item label="moving swing time">
             <el-slider v-model="value.value" :step="0.1" :min="0" :max="5" show-input/>
        </el-form-item>
    </fpt-bind-item>
    <fpt-bind-item attr="moving_no_fall" :plugin="plugin" v-slot="{value}">
        <el-form-item label="moving no fall">
             <el-switch v-model="value.value" />
        </el-form-item>
    </fpt-bind-item>
    <fpt-bind-item attr="moving_z_modify" :plugin="plugin" v-slot="{value}">
        <el-form-item label="moving z modify">
             <el-slider v-model="value.value" :step="0.5" :min="-20" :max="20" show-input/>
        </el-form-item>
    </fpt-bind-item>
    <fpt-bind-item attr="no_misdirect" :plugin="plugin" v-slot="{value}">
        <el-form-item label="no misdirect">
             <el-switch v-model="value.value" />
        </el-form-item>
    </fpt-bind-item>
    <el-divider/>
    <h4>Zoom</h4>
    <fpt-bind-item attr="zoom_cam_distance_reset"  :plugin="plugin" v-slot="{value}">
        <el-form-item label="cam distance reset">
            <el-switch v-model="value.value" />
        </el-form-item>
    </fpt-bind-item>
    <fpt-bind-item attr="zoom_cam_no_collision" :plugin="plugin" v-slot="{value}">
        <el-form-item label="cam no collision">
            <el-switch v-model="value.value" />
        </el-form-item>
    </fpt-bind-item>
    <fpt-bind-item :default_value="zoom_property_default" attr="zoom_property" :plugin="plugin" v-slot="{value}">
        <el-form-item label="zoom">
            <el-col :span="11">
                <el-input type="number" v-model.number="value.value.zoom.min" />
            </el-col>
            <el-col class="line" :span="2">&nbsp;-&nbsp;</el-col>
            <el-col :span="11">
                <el-input type="number" v-model.number="value.value.zoom.max" />
            </el-col>
        </el-form-item>
        <el-form-item label="fov">
            <el-col :span="11">
                <el-input type="number" v-model.number="value.value.fov.min" />
            </el-col>
            <el-col class="line" :span="2">&nbsp;-&nbsp;</el-col>
            <el-col :span="11">
                <el-input type="number" v-model.number="value.value.fov.max" />
            </el-col>
        </el-form-item>
        <el-form-item label="angle">
            <el-col :span="11">
                <el-input type="number" v-model.number="value.value.angle.min" />
            </el-col>
            <el-col class="line" :span="2">&nbsp;-&nbsp;</el-col>
            <el-col :span="11">
                <el-input type="number" v-model.number="value.value.angle.max" />
            </el-col>
        </el-form-item>
    </fpt-bind-item>
    <el-button @click="plugin.run_single('apply_zoom')" class="w-100">apply zoom</el-button>
    <el-divider/>
    <fpt-bind-item attr="cutscene_skip" :plugin="plugin" v-slot="{value}">
        <el-form-item label="cutscene skip">
             <el-switch v-model="value.value" />
        </el-form-item>
    </fpt-bind-item>
    <el-divider/>
</el-form>
`
})
