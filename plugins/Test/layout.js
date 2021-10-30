module.exports = vue.defineComponent({
    name: 'Test',
    props: ['plugin'],
    setup(props) {
        const {plugin} = vue.toRefs(props);
        return {plugin}
    },
    template: `
<div>
     <el-button @click="plugin.run_single('call')">call</el-button>
</div>
`
})
