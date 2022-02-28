<template>
    <b-container>
        <b-row align-h="center">
            <b-col cols="12">
                <b-button v-if="!isTimerOn" variant="primary" @click="start">Auto Reload On</b-button>
                <b-button v-if="isTimerOn" variant="danger" @click="stop">Auto Reload Off</b-button>
            </b-col>
            <b-col cols="12" sm="6">
                <line-chart v-if="isLoaded" :chartData="tempData"
                :options="tempOptions"/>
            </b-col>
            <b-col cols="12" sm="6">
                <line-chart v-if="isLoaded" :chartData="humidData"
                :options="humidOptions"/>
            </b-col>
            <b-col cols="12" sm="12"></b-col>
            <b-col cols="12" sm="6">
                <line-chart v-if="isLoaded" :chartData="atomData"
                :options="atomOptions"/>
            </b-col>
            <b-col cols="12" sm="6">
                <line-chart v-if="isLoaded" :chartData="co2Data"
                :options="co2Options"/>
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
import LineChart from './Chart.vue'

export default {
  name: 'LineChartsContainer',
    components: { 
        LineChart,
    },
    data () {
        return {
            isLoaded: false,
            isTimerOn: false,
            interval: 10,
            timer: null,
            tempData: null,
            humidData: null,
            atomData: null,
            co2Data: null,
            tempOptions: this.$store.state.tempOptions,    
            humidOptions: this.$store.state.humidOptions,
            atomOptions: this.$store.state.atomOptions,
            co2Options: this.$store.state.co2Options,
        }
    },
    async mounted () {
        // this.isLoaded = false
        await this.$store.dispatch('setDataAsync')
        .catch( e => console.log(e))
        .then( () =>{
            this.tempData = this.$store.state.tempData
            this.humidData = this.$store.state.humidData
            this.atomData = this.$store.state.atomData
            this.co2Data = this.$store.state.co2Data
        })
        this.isLoaded = true
    },
    methods: {
        async reload (){
            // this.isLoaded = false
            await this.$store.dispatch('setDataAsync')
            .catch( e => console.log(e))
            .then( () =>{
                this.tempData = this.$store.state.tempData
                this.humidData = this.$store.state.humidData
                this.atomData = this.$store.state.atomData
                this.co2Data = this.$store.state.co2Data
            })
            this.isLoaded = true
        },
        start () {
            this.reload()
            this.timer = setInterval(()=>{
                this.reload()
            }, this.interval*1000)
            this.isTimerOn = true
        },
        stop (){
            clearInterval(this.timer)
            this.isTimerOn = false
        },
    }
}
</script>