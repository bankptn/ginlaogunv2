<template>
    <v-container fluid class="main" id="home">
        <v-row justify="center" align="center">
            <v-form
                class="cardBody"
            >
                <div class="tableCol">
                    <v-card style=" border-radius: 30px;" @click="onClickBar(bar.rid)" v-for="bar in bars" :key="bar.rid" class="colCard">
                        {{ bar.name }}
                    </v-card>
                </div>
            </v-form>
        </v-row>
    </v-container>
</template>

<script>
import api from "../service/api"
export default {
    name: "Home",
    data() {
        return {
            bars:[]
        }
    },
    methods: {
        onClickBar (rid) {
            this.$router.push({name:"refeel", query:{rid: rid}})
        }
    },
    async mounted() {
        var result = await api.getAllRestarunt()
        this.bars = result.data.result
    }
}
</script>

<style scoped>
.main {
    min-height: 100vh;
    background: url(../assets/home.svg) ;
    background-position: center;
    background-repeat: no-repeat;
    background-size: 145%;
}

.tableCol {
    margin-top: 90px;
  display: grid;
  grid-template-columns: auto auto;
  background-color: #454545;
  border-radius: 50px;
  padding: 10px;
  font-size: 120px;
  /* height: 50vh;
  width: 180vh; */
}

.colCard {
  background-color: rgba(255, 255, 255, 0.8);
  padding: 20px;
  margin: 20px;
  font-size: 30px;
  text-align: center;
  height: 30vh;
  width: 40vw;
}

a {
    text-decoration: none;
}
</style>
