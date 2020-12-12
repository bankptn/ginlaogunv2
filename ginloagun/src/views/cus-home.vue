<template>
    <v-container fluid class="main" id="home">
        
            <v-row justify="center" align="center">
                <v-form
                    class="cardBody"
                >
                    <div class="tableCol">
                        <v-card style=" border-radius: 30px;" @click="onClickBar" v-for="bar in bars" :key="bar.id" class="col">
                            {{ bar.name }}
                        </v-card>
                    </div>
                </v-form>
            </v-row>
        
    </v-container>

</template>

<script>
export default {
    name: "Home",
    data() {
        return {
            bars:[
                {
                    id:"1",
                    name:"Refeel Bar & Bistro",
                },
                {
                    id:"2",
                    name:"C-minor",
                },
                {
                    id:"3",
                    name:"Zyn music bar & hashery",
                },
                {
                    id:"4",
                    name:"2gether bar & restaurant",
                }
            ]
        }
    },
    methods: {
        onClickBar () {
            this.$router.push({name:"Signup"})
        }
    },
}
</script>

<style scoped>
.main {
    /* display: flex; */
    background: url(../assets/home.svg) ;
    min-height: 100vh;
    background-position: center;
    background-repeat: no-repeat;
    background-size: 145%;
}

.bg {
    height: 100%;
    
}

.tableCol {
    margin-top: 90px;
  display: grid;
  grid-template-columns: auto auto;
  background-color: #454545;
  border-radius: 50px;
  padding: 10px;
  /* height: 50vh;
  width: 180vh; */
}

.col {
  background-color: rgba(255, 255, 255, 0.8);
  border-radius: 20px;
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
