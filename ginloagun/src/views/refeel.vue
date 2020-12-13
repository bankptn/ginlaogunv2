<template>
  <v-container fluid class="main" id="refeel">
      <v-row justify="center" align="center">
          <v-form
          class="cardBody"
          >
            <div class="mainbg">
            <v-row>
                <v-col cols="6">
                    <br>
                    <v-row>
                        <v-card style=" border-radius: 20px; background-color: white;" @click="onClick" class="inf">
                            <h2>Information</h2>
                            <h4>{{ restarunt.name }}</h4>
                            <h4>{{ restarunt.maxTable }}</h4>
                        </v-card>
                    </v-row>
                    <br>
                    <v-row>
                        <v-card style=" border-radius: 20px; " @click="onClick" class="menu">
                            <h2>Menu</h2>
                        </v-card>
                    </v-row>
                    <br>
                    <v-row>
                        <v-card style=" border-radius: 20px;" @click="onClick" class="band">
                            <h2>Band Schedule</h2>
                        </v-card>
                    </v-row>
                    <br>
                </v-col>
                <v-col cols="6">
                    <br>
                    <v-row>
                        <v-card style=" border-radius: 20px;" @click="onClick" class="promo">
                            <h2>Promotion</h2>
                        </v-card>
                    </v-row>
                    <br>
                    <v-row>
                        <v-card style=" border-radius: 20px;" @click="onClick" class="review">
                            <h2>Reviews</h2>
                        </v-card>
                    </v-row>
                    <br>
                    <v-row>
                        <v-card style=" border-radius: 20px;" @click="onClickTable(restarunt.rid)" class="table">
                            <h2>Reserve Table</h2>
                        </v-card>
                    </v-row>
                    <br>
                </v-col>
            </v-row>
            </div>
          </v-form>
      </v-row>
  </v-container>    
</template>

<script>
import api from "../service/api"
export default {
    name: "refeel",
    data() {
        return {
            rid: "",
            restarunt: {
                rid: "",
                name: "",
                maxTable: ""
            }
        }
    },
    async mounted() {
        this.rid = this.$route.query.rid
        var result = await api.getRestarunt(this.rid)
        if (result.data.status == "1") {
            this.restarunt.rid = result.data.result.rid
            this.restarunt.name = result.data.result.name
            this.restarunt.maxTable = result.data.result.tableRemain
        } else {
            this.$router.push({name:"home"})
        }
    },
    methods: {
        onClick (){
            this.$router.push({name:"Signup"})
        },
        onClickTable (rid){
            this.$router.push({name:"reserve", query:{rid: rid}})
        }
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
.cardBody {
    margin-top: 70px;
    height: 80vh;
    width: 60vw;
    color: #454545;
}
.inf {
    margin-left: 50px;
    height: 20vh;
    width: 25vw;
    background: white;
    border-radius: 50px;
}
.menu {
    margin-left: 50px;
    height: 30vh;
    width: 25vw;
    background: white;
    border-radius: 50px;
}
.band {
    margin-left: 50px;
    height: 15vh;
    width: 25vw;
    background: white;
    border-radius: 50px;
}
.promo {
    margin-left: 50px;
    height: 30vh;
    width: 25vw;
    background: white;
    border-radius: 50px;
}
.review {
    margin-left: 50px;
    height: 25vh;
    width: 25vw;
    background: white;
    border-radius: 50px;
}
.table {
    margin-left: 50px;
    height: 10vh;
    width: 25vw;
    background: white;
    border-radius: 50px;
}
.mainbg {
    background-color: #454545;
    border-radius: 50px;
}
h2 {
    color: black;
}
</style>