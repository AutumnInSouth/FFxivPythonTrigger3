module.exports = vue.defineComponent({
    name: 'Test',
    props: ['plugin'],
    setup(props) {
        const {plugin} = vue.toRefs(props);
        return {plugin}
    },
    template: `
<div>
    <fpt-bind-item attr="num" :plugin="plugin" v-slot="{value}">
    num:
        <el-input type="number" v-model.number="value.value"/>
    </fpt-bind-item>
    <fpt-bind-item attr="num2" :plugin="plugin" v-slot="{value}">
    num2:
        <el-input type="number" v-model.number="value.value"/>
    </fpt-bind-item>
</div>
`
})
