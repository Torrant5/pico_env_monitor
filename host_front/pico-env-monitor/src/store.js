import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(Vuex)
Vue.use(VueAxios, axios)

// const url = process.env.VUE_APP_API_BASE
const url = "./log/today.csv"

function convertCsvStringToStringArray(str) {
    return str.replace(/^\s*|\s*$/g, "")
        .split("\n").map(s => s.split(","))
        .map(s => s.map(s => s.replace(/^\s*|\s*$/g, "")))
}

const xAxesOp = [{
        scaleLabel: {
            display: true,
            labelString: 'time'
        },
        type: 'time',
        time: {
            parser: 'HH:mm:ss',
            unit: 'minute',
            stepSize: 1,
            displayFormats: {
                'hour': 'HH:mm:ss',
            }
        }
    }]


const store = new Vuex.Store({
    state: {
        tempData: {},
        humidData: {},
        atomData: {},
        co2Data: {},
        tempOptions: {
            scales: {
                xAxes: xAxesOp,
                yAxes: [{
                scaleLabel: {
                    display: true,
                    labelString: 'C'
                }}]
            }
        },    
        humidOptions: {
            scales: {
                xAxes: xAxesOp,
                yAxes: [{
                scaleLabel: {
                    display: true,
                    labelString: '%'
                }}]
            }
        },    
        atomOptions: {
            scales: {
                xAxes: xAxesOp,
                yAxes: [{
                scaleLabel: {
                    display: true,
                    labelString: 'hPa'
                }}]
            }
        },    
        co2Options: {
            scales: {
                xAxes: xAxesOp,
                yAxes: [{
                scaleLabel: {
                    display: true,
                    labelString: 'ppm'
                }}]
            }
        }
    },

    mutations: {
        setData (state, dataArr){
            // console.log(dataArr)
            var labels = dataArr.map(s => s[0])
            state.tempData = {
                labels: labels,
                datasets: [
                    {
                        label: 'Temperature',
                        backgroundColor: 'salmon',
                        data: dataArr.map(s => parseFloat(s[1]))
                    }
                ]
            }
            state.humidData = {
                labels: labels,
                datasets: [
                    {
                        label: 'Humidity',
                        backgroundColor: 'skyblue',
                        data: dataArr.map(s => parseFloat(s[2]))
                    }
                ]
            }
            state.atomData = {
                labels: labels,
                datasets: [
                    {
                        label: 'Atmospheric Pressure',
                        backgroundColor: 'darkorange',
                        data: dataArr.map(s => parseFloat(s[3]))
                    }
                ]
            }
            state.co2Data = {
                labels: labels,
                datasets: [
                    {
                        label: 'CO2',
                        backgroundColor: 'darkgreen',
                        data: dataArr.map(s => parseFloat(s[4]))
                    }
                ]
            }
        }
    },
    actions: {
        setDataAsync ({commit}){
            return axios.get(url)
                .then( res => {
                    const strArr = convertCsvStringToStringArray(res.data)
                    const dataArr = strArr.slice(1)
                    commit("setData", dataArr)
                })
        }
    }
})

export default store