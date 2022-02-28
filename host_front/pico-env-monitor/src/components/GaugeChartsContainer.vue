<template>
    <b-container>
        <b-row align-h="center">
            <b-col cols="12">
                <b-button v-if="!isTimerOn" variant="primary" @click="start">Auto Reload On</b-button>
                <b-button v-if="isTimerOn" variant="danger" @click="stop">Auto Reload Off</b-button>
            </b-col>
            <b-col cols="12" sm="6">
              <gauge v-if="isLoaded" class="mx-auto"
                heading="TEMPERATURE"
                fontSize="1em"
                :min="0"
                :max="40"
                :dp="2"
                :value="tempData"
                unit="℃"
                activeFill= "lightseagreen"
                inactiveFill= "lightseagreen"
                :minThreshold="15"
                :maxThreshold="30"
                minThresholdFill="gold"
                maxThresholdFill="orangered"
              />
            </b-col>
            <b-col cols="12" sm="6">
              <gauge v-if="isLoaded" class="mx-auto"
                heading="HUMIDITY"
                fontSize="1em"
                :min="0"
                :max="100"
                :dp="2"
                :value="humidData"
                unit="%"
                activeFill= "lightseagreen"
                inactiveFill= "lightseagreen"
                :minThreshold="40"
                :maxThreshold="60"
                minThresholdFill="orangered"
                maxThresholdFill="gold"
              />
            </b-col>
            <b-col cols="12" sm="12"></b-col>
            <b-col cols="12" sm="6">
                <!-- heading="ATMOSPHERIC PRESSURE" -->
              <gauge v-if="isLoaded" class="mx-auto"
                heading="ATM PRESS"
                fontSize="1em"
                :min="800"
                :max="1200"
                :dp="2"
                :value="atomData"
                unit="hPa"
                activeFill= "lightseagreen"
                inactiveFill= "lightseagreen"
                :minThreshold="900"
                :maxThreshold="1100"
                minThresholdFill="gold"
                maxThresholdFill="gold"
              />
            </b-col>
            <b-col cols="12" sm="6">
              <gauge v-if="isLoaded" class="mx-auto"
                heading="CO2"
                fontSize="1em"
                :min="400"
                :max="3000"
                :dp="2"
                :value="co2Data"
                unit="ppm"
                activeFill= "gold"
                inactiveFill= "gold"
                :minThreshold="1500"
                :maxThreshold="2500"
                minThresholdFill="lightseagreen"
                maxThresholdFill="orangered"
              />
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
import Gauge from '@chrisheanan/vue-gauge/src/components/Gauge.vue';

export default {
  name: 'GaugeChartsContainer',
  components: {
    Gauge
  },
  data() {
    return {
      exampleValue: 50,
      isLoaded: false,
      isTimerOn: false,
      interval: 10,
      timer: null,
      tempData: null,
      humidData: null,
      atomData: null,
      co2Data: null,
    }
  },
  async mounted () {
    // this.isLoaded = false
    await this.$store.dispatch('setDataAsync')
    .catch( e => console.log(e))
    .then( () =>{
      this.tempData = this.$store.state.tempData.datasets[0].data.slice(-1)[0]
      this.humidData = this.$store.state.humidData.datasets[0].data.slice(-1)[0]
      this.atomData = this.$store.state.atomData.datasets[0].data.slice(-1)[0]
      this.co2Data = this.$store.state.co2Data.datasets[0].data.slice(-1)[0]
      // console.log(this.tempData.labels)
      // console.log(this.tempData.datasets[0].data.slice(-1)[0])
    })
    this.isLoaded = true
  },
  methods: {
    async reload (){
      // this.isLoaded = false
      await this.$store.dispatch('setDataAsync')
      .catch( e => console.log(e))
      .then( () =>{
        this.tempData = this.$store.state.tempData.datasets[0].data.slice(-1)[0]
        this.humidData = this.$store.state.humidData.datasets[0].data.slice(-1)[0]
        this.atomData = this.$store.state.atomData.datasets[0].data.slice(-1)[0]
        this.co2Data = this.$store.state.co2Data.datasets[0].data.slice(-1)[0]
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