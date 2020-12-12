<template>
  <v-container fluid class="main" id="reserve">
      <v-row justify="center" align="center">
        <v-form
            class="cardBody"
            ref="form"
            v-model="valid"
            @submit.prevent="submitReserve"
            lazy-validation
        >
            <div class="mainbg">
                <v-row>
                    <v-col cols="8" class="map">
                        <v-img src="../assets/Refeel ผังร้าน 2.svg" alt="refeel" contain />

                    <v-row>
                            <h3>Restaurant Name:</h3>
                            <v-text-field
                                readonly
                                placeholder="Restaurant Name"
                                solo
                                v-model="restaurant.name"
                            />
                        </v-row>
                        <v-row>
                            <h3>Table Remain:</h3>
                            <v-text-field
                                readonly
                                placeholder="Table Remain"
                                solo
                                v-model="restaurant.remainTable"
                            
                            />
                            
                        </v-row>    
                    </v-col>
                    <v-col cols="4">
                        <h1>Book Table</h1>
                        <br>
                        <v-row>
                            <h2>Date:</h2>
                            <!-- <v-text-field
                                label="Regular"
                                placeholder="Date"
                                solo
                            /> -->
                            <v-col cols="12" lg="6">
                        <v-menu
                            ref="menu1"
                            v-model="menu1"
                            :close-on-content-click="false"
                            transition="scale-transition"
                            offset-y
                            max-width="290px"
                            min-width="290px"
                        >
                        <template v-slot:activator="{ on, attrs }">
                            <v-text-field
                                placeholder="Time"
                                solo
                                v-model="dateFormatted"
                                label="Date"
                                hint="MM/DD/YYYY format"
                                persistent-hint
                                v-bind="attrs"
                                @blur="date = parseDate(dateFormatted)"
                                v-on="on"
                                readonly
                                name="date"
                            ></v-text-field>
                        </template>
                        <v-date-picker v-model="date" no-title @input="menu1 = false"></v-date-picker>
                        </v-menu>
                       
                    </v-col>
                        </v-row>
                        <v-row>
                            <h2>Time:</h2>
                            <!-- <v-text-field
                                label="Regular"
                                placeholder="Time"
                                solo
                            /> -->
                            
                        <v-col cols="11" sm="5">
                        <v-menu
                            ref="menu"
                            v-model="menu2"
                            :close-on-content-click="false"
                            :nudge-right="40"
                            :return-value.sync="time"
                            transition="scale-transition"
                            offset-y
                            max-width="290px"
                            min-width="290px"
                        >
                            <template v-slot:activator="{ on, attrs }">
                            <v-text-field
                                v-model="time"
                                label="Picker in menu"
                                readonly
                                v-bind="attrs"
                                v-on="on"
                                placeholder="Time"
                                solo
                                name="time"
                            ></v-text-field>
                            </template>
                            <v-time-picker
                            v-if="menu2"
                            v-model="time"
                            full-width
                            @click:minute="$refs.menu.save(time)"
                            ></v-time-picker>
                        </v-menu>
                        </v-col>

                        </v-row>
                        <v-row>
                            <h2>Number of Table:</h2>
                            <v-text-field
                                label="Regular"
                                placeholder="Number of Table"
                                solo
                                name="tableAmount"
                                v-model=reservation.tableAmount
                            />
                        </v-row>
                        <v-row>
                            <h2>Detail:</h2>
                            <v-text-field
                                label="Regular"
                                placeholder="Detail"
                                solo
                                name="detail"
                                v-model=reservation.detail
                            />
                        </v-row>
                        <v-row class="btn">
                            <v-btn class="submit" style="background-color: #95E7EE; border-radius: 20px;" type="submit">
                                Submit
                            </v-btn>
                            <v-btn class="cancel" style="background-color: #ED8C8C; border-radius: 20px;">
                                Cancel
                            </v-btn>
                        </v-row>
                        
                    </v-col>
                </v-row>
            </div>
        </v-form>
      </v-row>

  </v-container>
</template>

<script>
import api from "../service/api"
import { server } from "../service/constants"
export default {
    name:"reserve",
    data: vm => ({
        date: new Date().toISOString().substr(0, 10),
        dateFormatted: vm.formatDate(new Date().toISOString().substr(0, 10)),
        menu1: false,
        menu2: false,
        restaurant: {
                rid:"",
                name:"",
                remainTable:""
            },
        reservation: {
            ssn:"",
            rid:"",
            createDate:"",
            tableAmount:"",
            detail:""
        },
        valid: true,
        time: null,
        modal2: false,

    }),
    computed: {
      computedDateFormatted () {
        return this.formatDate(this.date)
      },
    },

    watch: {
      date () {
        this.dateFormatted = this.formatDate(this.date)
      },
    },

    async mounted() {
        const result = await api.getRemainTableByrid("r000000003")
        if (result.data !== null) {
            this.restaurant.rid = result.data.result.rid
            this.restaurant.name = result.data.result.name
            this.restaurant.remainTable = result.data.result.remainTable
        }
    },
    methods: {
        onClickSubmit() {
            console.log()
            this.$router.push({name:"refeel"})
        },
        submitReserve (){
            this.reservation.createDate = this.dateFormatted + " " + this.time
            this.reservation.ssn = localStorage.getItem(server.USERNAME)
            this.reservation.rid = "r000000003"
            console.log(this.reservation)
            this.$store.dispatch({ 
                type: "reserve",
                ssn : this.reservation.ssn,
                rid : this.reservation.rid,
                createDate : this.reservation.createDate,
                tableAmount : this.reservation.tableAmount,
                detail : this.reservation.detail,
            })
        },
        formatDate (date) {
            if (!date) return null

            const [year, month, day] = date.split('-')
            return `${month}/${day}/${year}`
        },
        parseDate (date) {
            if (!date) return null

            const [month, day, year] = date.split('/')
            return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
        },
    }

}
</script>

<style scoped>
.main {
    min-height: 100vh;
    background: url(../assets/home.svg);
    background-position: center;
    background-repeat: no-repeat;
    background-size: 145%;
}
.cardBody {
    margin-top: 78px;
    height: 70vh;
    width: 70vw;
    background: #454545;
    border-radius: 50px;
}
.mainbg {
    padding: 45px;
    background-color: #454545;
    border-radius: 50px;
}
h1, h2, h3 {
    /* margin-left: 40px; */
    color: white;
}
.btn {
    display: flex;
    justify-content: flex-end;
}
.submit {
    margin-right: 20px;
}
h2 {
    margin-right: 2 px;
}
h3 {
    margin-right: 10px;
}
.cardBody {
    margin-top: 20px;
}
</style>