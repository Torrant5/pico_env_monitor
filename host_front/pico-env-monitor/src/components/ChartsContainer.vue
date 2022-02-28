<template>
    <b-container class="mt-1 mb-5">
        <b-row>
            <b-col cols="12" lg="3" class="my-1">
                <b-button v-if="!isGauge" variant="info" @click="chartChange">
                    Change Chart Mode</b-button>
                <b-button v-if="isGauge"  variant="info" @click="chartChange">
                    Change Gauge Mode</b-button>
            </b-col>
            <b-col v-if="isGauge" cols="12" lg="9" xl="8">
                <LineChartsContainer />
            </b-col>
            <b-col v-if="!isGauge" cols="12" lg="9" xl="8">
                <GaugeChartsContainer />
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
import LineChartsContainer from './LineChartsContainer.vue'
import GaugeChartsContainer from './GaugeChartsContainer.vue'

export default {
  name: 'ChartsContainer',
    components: { 
        LineChartsContainer,
        GaugeChartsContainer,
    },
    data () {
        return {
            isGauge: true
        }
    },
    methods:{
        chartChange () {
            this.isGauge = !this.isGauge
        }
    }
}
</script>