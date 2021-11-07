module.exports=vue.defineComponent({
    name:"XivCombat",
    props:['plugin'],
    setup(props,context){
        const {plugin}=props;
        return {plugin}
    },
    template:`
<fpt-bind-item attr="common_config" :plugin="plugin" v-slot="{value}">
    {{value.value}}
</fpt-bind-item>
<fpt-bind-item attr="job_pairing" :plugin="plugin" v-slot="{value}">
    {{value.value}}
</fpt-bind-item>
<fpt-bind-item attr="strategy_config" :plugin="plugin" v-slot="{value}">
    {{value.value}}
</fpt-bind-item>
`

})
